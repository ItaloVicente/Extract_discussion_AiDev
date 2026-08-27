import os
import glob
import pandas as pd

# === Configurações ===
LANGUAGES = ["C#", "Java", "Python", "Ruby"]
BASE_DIR = "."
EXCEL_OUTPUT = "Discussions_Summary.xlsx"  # Salva direto na raiz


def main():
    pr_dict = {}
    print("🔎 Mapeando Pull Requests nos CSVs para gerar o Excel...")

    # 1. Lê os CSVs para mapear as PRs e o status do clone
    for lang in LANGUAGES:
        search_path = os.path.join(BASE_DIR, lang, "clones_classified", "*_clone_classified.csv")
        csv_files = glob.glob(search_path)

        for file in csv_files:
            try:
                df_csv = pd.read_csv(file)
                req_cols = {'project', 'pr', 'categoria', 'start_commit', 'end_commit', 'total_commits'}

                if not df_csv.empty and req_cols.issubset(df_csv.columns):
                    # Filtro idêntico ao do script original
                    mask_to_drop = (
                            (df_csv["categoria"] == "ini_mei_final") &
                            (df_csv["start_commit"] == 1) &
                            (df_csv["end_commit"] == 1) &
                            (df_csv["total_commits"] == 1)
                    )
                    df_csv = df_csv[~mask_to_drop]

                    if df_csv.empty:
                        continue

                    grouped = df_csv.groupby(['project', 'pr'])
                    for (proj, pr_num), group in grouped:
                        has_unmerged = any('final' not in str(cat) for cat in group['categoria'])
                        key = (lang, str(proj), int(pr_num))

                        if key not in pr_dict:
                            pr_dict[key] = has_unmerged
                        elif has_unmerged:
                            pr_dict[key] = True

            except Exception as e:
                print(f"⚠️ Erro ao ler o CSV {file}: {e}")

    # 2. Prepara os dados para cada linguagem com a URL customizada
    excel_data = {lang: [] for lang in LANGUAGES}

    for (lang, project, pr_number), has_unmerged in pr_dict.items():
        # Tratamento de URL: Substitui o '#' por '%23' para não quebrar o link no navegador
        safe_lang_url = lang.replace("#", "%23")

        custom_url = f"https://github.com/ItaloVicente/Extract_discussion_AiDev/blob/main/discussion/{safe_lang_url}/{project}/{pr_number}.md"

        excel_data[lang].append({
            "Project": project,
            "PR": pr_number,
            "Has Unmerged Clone": "Yes" if has_unmerged else "No",
            "URL": custom_url,
            "Has Discussion?": ""
        })

    # 3. Gera o arquivo Excel na raiz com as abas
    print(f"\n📊 Gerando arquivo Excel na raiz: {EXCEL_OUTPUT}...")
    with pd.ExcelWriter(EXCEL_OUTPUT, engine='openpyxl') as writer:
        for lang in LANGUAGES:
            df_lang = pd.DataFrame(excel_data[lang])

            # Cria a aba vazia com as colunas caso não exista projetos para a linguagem
            if df_lang.empty:
                df_lang = pd.DataFrame(columns=["Project", "PR", "Has Unmerged Clone", "URL", "Has Discussion?"])

            df_lang.to_excel(writer, sheet_name=lang, index=False)

    print("✅ Excel gerado com sucesso na pasta raiz!")


if __name__ == "__main__":
    main()