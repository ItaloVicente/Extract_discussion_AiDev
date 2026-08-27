# precisa do clones_classified, git_repos, search_results e metadata
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import subprocess
from tqdm import tqdm

# === Configurações ===
CLONES_CLASSIFIED_DIR = "clones_classified"
SEARCH_RESULTS_DIR = "search_results"
METADATA_DIR = "metadata"
GIT_REPOS_DIR = "git_repos"
OUTPUT_MD_DIR = "extracted_clones_md"  # Mudou de txt para md
EXCEL_OUTPUT = "Clone_Code_Classification.xlsx"

os.makedirs(OUTPUT_MD_DIR, exist_ok=True)


def get_target_clones():
    """Lê os CSVs, filtra clones de 1 commit e escolhe 1 clone por PR."""
    target_clones = []
    csv_files = glob.glob(os.path.join(CLONES_CLASSIFIED_DIR, "*.csv"))

    print("🔎 Analisando CSVs de classificação de clones...")
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            req_cols = {'project', 'pr', 'categoria', 'clone_fingerprint', 'start_commit', 'end_commit',
                        'total_commits'}
            if df.empty or not req_cols.issubset(df.columns):
                continue

            # FILTRO: Remover clones ini_mei_final que possuem apenas 1 commit
            mask_1_commit = (
                    (df['categoria'] == 'ini_mei_final') &
                    (df['start_commit'] == 1) &
                    (df['end_commit'] == 1) &
                    (df['total_commits'] == 1)
            )
            df = df[~mask_1_commit]

            if df.empty:
                continue

            grouped = df.groupby(['project', 'pr'])
            for (project, pr), group in grouped:
                unmerged_clones = group[~group['categoria'].str.contains('final', na=False, case=False)]

                if not unmerged_clones.empty:
                    selected_clone = unmerged_clones.iloc[0]
                else:
                    selected_clone = group.iloc[0]

                target_clones.append(selected_clone.to_dict())

        except Exception as e:
            print(f"⚠️ Erro ao ler {file}: {e}")

    return target_clones


def get_commit_data(project, pr, start_commit):
    """Busca o SHA e gera a URL de clone a partir do CSV de metadados."""
    meta_csv = os.path.join(METADATA_DIR, f"{project}.csv")
    if not os.path.exists(meta_csv):
        print(f"⚠️ Metadados não encontrados: {meta_csv}")
        return None, None

    df_meta = pd.read_csv(meta_csv)
    df_meta['number_pr'] = df_meta['number_pr'].astype(str)
    df_meta['number_commit'] = df_meta['number_commit'].astype(str)

    match = df_meta[(df_meta['number_pr'] == str(pr)) & (df_meta['number_commit'] == str(start_commit))]

    if not match.empty:
        sha = match.iloc[0]['child']
        api_url = str(match.iloc[0]['repo_url'])

        parts = api_url.rstrip("/").split("/")
        if len(parts) >= 2:
            owner, repo_name = parts[-2], parts[-1]
            clone_url = f"[https://github.com/](https://github.com/){owner}/{repo_name}.git"
        else:
            clone_url = None

        return sha, clone_url

    print(f"⚠️ SHA não encontrado para Projeto: {project} | PR: {pr} | Commit: {start_commit}")
    return None, None


def extract_code_from_repo(project, pr, sha, clone_url, rel_path, start_line, end_line):
    """Garante que o repositório existe, faz o checkout e extrai o código."""
    repo_dir = os.path.join(GIT_REPOS_DIR, project)
    file_path = os.path.join(repo_dir, rel_path)

    if not os.path.exists(repo_dir):
        if not clone_url:
            return f"*(ERRO: Pasta '{project}' não existe e não foi possível gerar a URL de clone)*"

        res_clone = subprocess.run(["git", "clone", "--filter=blob:none", clone_url, repo_dir], capture_output=True,
                                   text=True)
        if res_clone.returncode != 0:
            return f"*(ERRO GIT: Falha ao clonar o repositório {project}. Detalhe: {res_clone.stderr.strip()})*"

    res = subprocess.run(["git", "checkout", "-f", sha], cwd=repo_dir, capture_output=True, text=True)

    if res.returncode != 0:
        subprocess.run(["git", "fetch", "origin", f"pull/{pr}/head"], cwd=repo_dir, capture_output=True)
        res2 = subprocess.run(["git", "checkout", "-f", sha], cwd=repo_dir, capture_output=True, text=True)

        if res2.returncode != 0:
            return f"*(ERRO GIT: Falha ao fazer checkout do commit {sha}. Ele não existe localmente nem no PR. Detalhe: {res.stderr.strip()})*"

    if not os.path.exists(file_path):
        return f"*(ERRO: O arquivo '{rel_path}' não foi encontrado dentro do commit {sha})*"

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        snippet = "".join(lines[start_line - 1: end_line]).strip()
        if not snippet:
            return "*(AVISO: Extração ocorreu com sucesso, mas linhas estão vazias)*"
        return snippet
    except Exception as e:
        return f"*(ERRO: Falha ao ler o arquivo: {e})*"


def main():
    target_clones = get_target_clones()
    print(f"✅ {len(target_clones)} clones selecionados (1 por PR válida).")

    excel_data = []

    print("\n🚀 Iniciando extração de código dos repositórios...")
    for clone in tqdm(target_clones, desc="Extraindo clones"):
        project = clone['project']
        pr = clone['pr']
        fingerprint = clone['clone_fingerprint']
        start_commit = clone['start_commit']

        sha, clone_url = get_commit_data(project, pr, start_commit)
        if not sha: continue

        xml_name = f"nicad-result-{project}-{pr}-{start_commit}-child.xml"
        xml_path = os.path.join(SEARCH_RESULTS_DIR, xml_name)

        if not os.path.exists(xml_path):
            print(f"⚠️ XML não encontrado: {xml_name}")
            continue

        tree = ET.parse(xml_path)
        root = tree.getroot()

        blocks_to_extract = []
        for check in root.findall('check'):
            for clone_set in check.findall('set'):
                if clone_set.attrib.get('fingerprint') == str(fingerprint):
                    blocks = clone_set.findall('block')[:2]
                    for b in blocks:
                        abs_source = b.attrib.get('sourceFile')
                        rel_path = abs_source.split(f"git_repos/{project}/")[-1]

                        blocks_to_extract.append({
                            'path': rel_path,
                            'start': int(b.attrib.get('startLineNumber')),
                            'end': int(b.attrib.get('endLineNumber'))
                        })
                    break

        if not blocks_to_extract:
            print(f"⚠️ Fingerprint {fingerprint} não encontrado no XML {xml_name}")
            continue

        # ==========================================
        # CONSTRUÇÃO DO MARKDOWN BEM FORMATADO
        # ==========================================
        md_filename = f"{project}_PR{pr}_{fingerprint}.md"

        md_content = f"# 🔍 Clone Analysis | Project: {project} | PR: #{pr}\n\n"
        md_content += f"- **Commit SHA:** `{sha}`\n"
        md_content += f"- **Clone Fingerprint:** `{fingerprint}`\n"
        md_content += f"- **Categoria:** `{clone['categoria']}`\n\n"
        md_content += "---\n\n"

        for i, block in enumerate(blocks_to_extract, 1):
            code_snippet = extract_code_from_repo(project, pr, sha, clone_url, block['path'], block['start'],
                                                  block['end'])

            md_content += f"## 🧑‍💻 Clone Par {i}\n"
            md_content += f"**File:** `{block['path']}`\n"
            md_content += f"**Lines:** {block['start']} to {block['end']}\n\n"
            md_content += f"```text\n{code_snippet}\n```\n\n"

            if i < len(blocks_to_extract):
                md_content += "---\n\n"

        # 5. Salvar o arquivo Markdown
        with open(os.path.join(OUTPUT_MD_DIR, md_filename), 'w', encoding='utf-8') as f:
            f.write(md_content)

        # 6. Preencher dados para o Excel incluindo a URL do GitHub
        github_url = f"[https://github.com/ItaloVicente/Extract_discussion_AiDev/blob/main/extracted_clones_md/](https://github.com/ItaloVicente/Extract_discussion_AiDev/blob/main/extracted_clones_md/){md_filename}"

        excel_data.append({
            "Project": project,
            "PR": pr,
            "Commit_SHA": sha,
            "Clone_Fingerprint": fingerprint,
            "Start_Commit": start_commit,
            "End_Commit": clone['end_commit'],
            "Total_Commits": clone['total_commits'],
            "Categoria": clone['categoria'],
            "Distancia": clone['distancia'],
            "Duracao": clone['duracao'],
            "URL_Clone_Code": github_url,  # <-- Nova coluna apontando para o seu repositório
            "Code_Classification": ""
        })

    print("\n📊 Gerando arquivo Excel...")
    df_excel = pd.DataFrame(excel_data)
    df_excel.to_excel(EXCEL_OUTPUT, index=False)

    print(f"✅ Arquivos Markdown salvos na pasta '{OUTPUT_MD_DIR}/'.")
    print(f"✅ Planilha Excel salva em: {EXCEL_OUTPUT}")


if __name__ == "__main__":
    main()