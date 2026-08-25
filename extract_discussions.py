import os
import glob
import pandas as pd
from datasets import load_dataset
from tqdm import tqdm

# === Configurações de Diretórios ===
LANGUAGES = ["C#", "Java", "Python", "Ruby"]
BASE_DIR = "."  # Altere se os CSVs estiverem em outro diretório
OUTPUT_BASE_DIR = "discussion"


def load_and_index_hf_datasets():
    print("⏳ Carregando banco de dados do Hugging Face (hao-li/AIDev)...")

    # Carregando tabelas e convertendo para Pandas
    df_pr = load_dataset("hao-li/AIDev", "pull_request", split="train").to_pandas()
    df_pr_comments = load_dataset("hao-li/AIDev", "pr_comments", split="train").to_pandas()
    df_pr_reviews = load_dataset("hao-li/AIDev", "pr_reviews", split="train").to_pandas()
    df_pr_rev_comments = load_dataset("hao-li/AIDev", "pr_review_comments", split="train").to_pandas()

    print("🗂️ Indexando tabelas para buscas super rápidas...")

    # Preenchendo NaNs para evitar quebra no Markdown
    df_pr['body'] = df_pr['body'].fillna("*(Sem descrição fornecida)*")
    df_pr_comments['body'] = df_pr_comments['body'].fillna("")
    df_pr_reviews['body'] = df_pr_reviews['body'].fillna("")
    df_pr_rev_comments['body'] = df_pr_rev_comments['body'].fillna("")

    return df_pr, df_pr_comments, df_pr_reviews, df_pr_rev_comments


def get_unique_prs_from_csvs():
    """Lê as pastas locais e mapeia se a PR possui clones não mergeados."""
    pr_dict = {}
    print("🔎 Mapeando Pull Requests nos CSVs locais...")

    for lang in LANGUAGES:
        search_path = os.path.join(BASE_DIR, lang, "clones_classified", "*_clone_classified.csv")
        csv_files = glob.glob(search_path)

        for file in csv_files:
            try:
                df_csv = pd.read_csv(file)
                req_cols = {'project', 'pr', 'categoria', 'start_commit', 'end_commit', 'total_commits'}

                if not df_csv.empty and req_cols.issubset(df_csv.columns):
                    # FILTRO: Identifica clones de tiro único (1, 1, 1) rotulados como ini_mei_final
                    mask_to_drop = (
                            (df_csv["categoria"] == "ini_mei_final") &
                            (df_csv["start_commit"] == 1) &
                            (df_csv["end_commit"] == 1) &
                            (df_csv["total_commits"] == 1)
                    )

                    # Aplica a negação da máscara
                    df_csv = df_csv[~mask_to_drop]

                    if df_csv.empty:
                        continue

                    # Agrupa por PR para analisar todos os clones dela
                    grouped = df_csv.groupby(['project', 'pr'])
                    for (proj, pr_num), group in grouped:
                        # Se ALGUMA categoria não tiver a palavra 'final', então o clone não chegou ao merge
                        has_unmerged = any('final' not in str(cat) for cat in group['categoria'])

                        key = (lang, str(proj), int(pr_num))
                        if key not in pr_dict:
                            pr_dict[key] = has_unmerged
                        else:
                            # Se já existe, atualiza para True se encontrar algum não mergeado
                            if has_unmerged:
                                pr_dict[key] = True

            except Exception as e:
                print(f"⚠️ Erro ao ler o CSV {file}: {e}")

    # Converte o dicionário auxiliar para a lista final
    unique_pr_list = [
        {
            "lang": k[0],
            "project": k[1],
            "pr_number": k[2],
            "has_unmerged_clone": "Yes" if v else "No"
        }
        for k, v in pr_dict.items()
    ]

    print(f"✅ Encontradas {len(unique_pr_list)} Pull Requests únicas para extração.")
    return unique_pr_list


def create_markdown_content(project, pr_number, pr_row, comments_df, reviews_df, rev_comments_df):
    """Monta a estrutura escaneável do arquivo Markdown."""

    pr_id = pr_row['id']
    pr_url = pr_row.get('html_url', 'URL não disponível')

    # 1. Filtragem relacional
    pr_comments = comments_df[comments_df['pr_id'] == pr_id]
    pr_reviews = reviews_df[reviews_df['pr_id'] == pr_id]

    review_ids = pr_reviews['id'].tolist()
    pr_rev_comments = rev_comments_df[rev_comments_df['pull_request_review_id'].isin(review_ids)]

    # 2. Contagens
    count_comments = len(pr_comments)
    count_reviews = len(pr_reviews)
    count_rev_comments = len(pr_rev_comments)

    # 3. Construção da String Markdown
    md = f"# Discussões da PR #{pr_number} | Projeto: {project}\n\n"
    md += f"**🔗 Link da PR:** [{pr_url}]({pr_url})\n\n"

    md += "## 📊 Resumo de Interações\n\n"
    md += "| Origem da Tabela | Quantidade de Registros |\n"
    md += "| :--- | :--- |\n"
    md += f"| `pull_request` (Body) | 1 |\n"
    md += f"| `pr_comments` | {count_comments} |\n"
    md += f"| `pr_reviews` | {count_reviews} |\n"
    md += f"| `pr_review_comments` | {count_rev_comments} |\n\n"

    md += "---\n\n"

    # Body Original
    md += f"## 📝 Pull Request Body (Autor: {pr_row.get('user', 'Desconhecido')})\n\n"
    md += f"> {str(pr_row['body']).replace(chr(10), chr(10) + '> ')}\n\n"
    md += "---\n\n"

    # PR Comments
    md += f"## 💬 PR Comments ({count_comments})\n\n"
    if count_comments == 0:
        md += "*Nenhum comentário geral registrado.*\n\n"
    else:
        for _, comment in pr_comments.iterrows():
            author = comment.get('user', 'Desconhecido')
            date = comment.get('created_at', 'Data desconhecida')
            md += f"**👤 {author}** comentou em {date}:\n\n"
            md += f"{comment['body']}\n\n"

    md += "---\n\n"

    # PR Reviews e Review Comments
    md += f"## 🔍 PR Reviews ({count_reviews}) e Comentários de Linha ({count_rev_comments})\n\n"
    if count_reviews == 0:
        md += "*Nenhuma revisão estruturada registrada.*\n\n"
    else:
        for _, review in pr_reviews.iterrows():
            rev_id = review['id']
            author = review.get('user', 'Desconhecido')
            state = review.get('state', 'Sem Status')
            rev_body = str(review['body']).strip()

            # Cabeçalho da Revisão
            md += f"### 🛠️ Revisão por {author} [Status: {state}]\n\n"

            # Corpo da Revisão (Lidando com os Nulos)
            md += "**Comentário Geral da Revisão:**\n"
            if rev_body and rev_body.lower() != 'nan' and rev_body.lower() != 'none':
                md += f"> {rev_body.replace(chr(10), chr(10) + '> ')}\n\n"
            else:
                md += "> *(Revisão enviada sem comentário geral)*\n\n"

            # Comentários de Linha específicos desta revisão
            line_comments = pr_rev_comments[pr_rev_comments['pull_request_review_id'] == rev_id]

            if not line_comments.empty:
                md += f"**Comentários de Linha atrelados a esta revisão ({len(line_comments)}):**\n\n"
                for _, l_comment in line_comments.iterrows():
                    l_author = l_comment.get('user', 'Desconhecido')
                    path = l_comment.get('path', 'Arquivo desconhecido')
                    position = l_comment.get('position', 'Posição desconhecida')
                    l_body = str(l_comment['body']).strip()

                    md += f"- **📍 {l_author}** em `{path}` (Linha/Pos {position}):\n"
                    md += f"  > {l_body.replace(chr(10), chr(10) + '  > ')}\n\n"
            else:
                md += "*(Nenhum comentário de linha atrelado a esta revisão)*\n\n"

            md += "---\n\n"

    return md


def main():
    df_pr, df_pr_comments, df_pr_reviews, df_pr_rev_comments = load_and_index_hf_datasets()
    prs_to_process = get_unique_prs_from_csvs()

    if not prs_to_process:
        print("🚨 Nenhuma PR encontrada para processamento. Encerrando.")
        return

    # Dicionário para armazenar os dados do Excel por linguagem
    excel_data = {lang: [] for lang in LANGUAGES}

    print("🚀 Iniciando extração e formatação de discussões...")

    for item in tqdm(prs_to_process, desc="Gerando arquivos Markdown"):
        lang = item['lang']
        project = item['project']
        pr_number = item['pr_number']
        has_unmerged_clone = item['has_unmerged_clone']

        matched_pr = df_pr[
            (df_pr['number'] == pr_number) &
            (df_pr['repo_url'].str.contains(f"/{project}(?:/|$)", regex=True, case=False, na=False))
            ]

        if matched_pr.empty:
            continue

        pr_row = matched_pr.iloc[0]
        pr_url = pr_row.get('html_url', '')

        # Gera e salva o conteúdo Markdown
        md_content = create_markdown_content(
            project, pr_number, pr_row,
            df_pr_comments, df_pr_reviews, df_pr_rev_comments
        )

        save_dir = os.path.join(OUTPUT_BASE_DIR, lang, project)
        os.makedirs(save_dir, exist_ok=True)

        file_path = os.path.join(save_dir, f"{pr_number}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        # Adiciona a linha ao buffer do Excel
        excel_data[lang].append({
            "Project": project,
            "PR": pr_number,
            "Has Unmerged Clone": has_unmerged_clone,
            "URL": pr_url,
            "Has Discussion?": ""
        })

    # ==========================================
    # GERAÇÃO DO ARQUIVO EXCEL
    # ==========================================
    print("\n📊 Gerando arquivo Excel com o resumo...")
    excel_path = os.path.join(OUTPUT_BASE_DIR, "Discussions_Summary.xlsx")

    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for lang in LANGUAGES:
            df_lang = pd.DataFrame(excel_data[lang])

            # Se não houver dados para a linguagem, cria uma aba vazia com as colunas corretas
            if df_lang.empty:
                df_lang = pd.DataFrame(columns=["Project", "PR", "Has Unmerged Clone", "URL", "Has Discussion?"])

            df_lang.to_excel(writer, sheet_name=lang, index=False)

    print(f"✅ Arquivos Markdown salvos na pasta '{OUTPUT_BASE_DIR}/'.")
    print(f"✅ Planilha Excel salva em: {excel_path}")


if __name__ == "__main__":
    main()