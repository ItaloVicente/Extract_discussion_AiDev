import os
import glob
import pandas as pd

# === Configurações ===
LANGUAGES = ["C#", "Java", "Python", "Ruby"]
OUTPUT_EXCEL = "Final_Merged_Analysis.xlsx"


def get_discussion_flags(lang):
    """Varre os CSVs da linguagem para mapear se a PR tem clone não mergeado."""
    pr_dict = {}
    search_path = os.path.join(lang, "clones_classified", "*_clone_classified.csv")
    csv_files = glob.glob(search_path)

    for file in csv_files:
        try:
            df_csv = pd.read_csv(file)
            req_cols = {'project', 'pr', 'categoria', 'start_commit', 'end_commit', 'total_commits'}

            if not df_csv.empty and req_cols.issubset(df_csv.columns):
                # Filtra clones de tiro único (ini_mei_final com 1 commit)
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
                    # Se não tem 'final' na categoria, o clone não foi mergeado
                    has_unmerged = any('final' not in str(cat) for cat in group['categoria'])
                    key = (str(proj), str(pr_num))

                    if key not in pr_dict:
                        pr_dict[key] = has_unmerged
                    elif has_unmerged:
                        pr_dict[key] = True
        except Exception as e:
            print(f"⚠️ Erro ao ler o CSV {file}: {e}")

    return pr_dict


def main():
    print("🔗 Iniciando a unificação e padronização das URLs baseada na nova estrutura...")

    with pd.ExcelWriter(OUTPUT_EXCEL, engine='openpyxl') as writer:
        for lang in LANGUAGES:
            print(f"Processando linguagem: {lang}...")

            # O Excel base agora fica dentro da pasta da linguagem
            excel_path = os.path.join(lang, "Clone_Code_Classification.xlsx")

            if not os.path.exists(excel_path):
                print(f"⚠️ Arquivo não encontrado: {excel_path}. Criando aba vazia.")
                # Cria aba vazia para linguagens que ainda não foram processadas (ex: C#, Ruby)
                pd.DataFrame(columns=[
                    "Project", "PR", "Commit_SHA", "Clone_Fingerprint", "Start_Commit",
                    "End_Commit", "Total_Commits", "Categoria", "Distancia", "Duracao",
                    "URL_Clone_Code", "URL_Discussion", "Has Unmerged Clone", "Code_Classification"
                ]).to_excel(writer, sheet_name=lang, index=False)
                continue

            try:
                df = pd.read_excel(excel_path)

                # Padroniza tipos para evitar bugs no cruzamento (tudo vira string)
                df['Project'] = df['Project'].astype(str).str.strip()
                df['PR'] = df['PR'].astype(str).str.strip()
                if 'Clone_Fingerprint' in df.columns:
                    df['Clone_Fingerprint'] = df['Clone_Fingerprint'].astype(str).str.strip()

                # 1. Recupera as flags de discussão recalculando direto da fonte (CSVs)
                discussion_flags = get_discussion_flags(lang)

                # 2. Constrói as URLs corrigidas
                safe_lang = lang.replace("#", "%23")
                urls_clone = []
                urls_disc = []
                has_unmerged_list = []

                for _, row in df.iterrows():
                    proj = row['Project']
                    pr_num = row['PR']
                    fingerprint = row.get('Clone_Fingerprint', '')

                    # Nova Rota Clone Code: {lang}/extracted_clones_md/...
                    md_filename = f"{proj}_PR{pr_num}_{fingerprint}.md"
                    url_clone = f"https://github.com/ItaloVicente/Extract_discussion_AiDev/blob/main/{safe_lang}/extracted_clones_md/{md_filename}"
                    urls_clone.append(url_clone)

                    # Nova Rota Discussão: discussion/{lang}/{project}/{pr}.md
                    url_disc = f"https://github.com/ItaloVicente/Extract_discussion_AiDev/blob/main/discussion/{safe_lang}/{proj}/{pr_num}.md"
                    urls_disc.append(url_disc)

                    # Puxa o status da PR
                    key = (proj, pr_num)
                    unmerged = discussion_flags.get(key, False)
                    has_unmerged_list.append("Yes" if unmerged else "No")

                # Injeta os dados no DataFrame
                df['URL_Clone_Code'] = urls_clone
                df['URL_Discussion'] = urls_disc
                df['Has Unmerged Clone'] = has_unmerged_list

                # Reordena as colunas (URLs pro final, mas antes do espaço de classificação)
                cols = df.columns.tolist()
                for col in ['URL_Clone_Code', 'URL_Discussion', 'Has Unmerged Clone']:
                    if col in cols: cols.remove(col)

                if 'Code_Classification' in cols:
                    cols.remove('Code_Classification')
                    cols.extend(['URL_Clone_Code', 'URL_Discussion', 'Has Unmerged Clone', 'Code_Classification'])
                else:
                    cols.extend(['URL_Clone_Code', 'URL_Discussion', 'Has Unmerged Clone'])

                df = df[cols]

                # Salva na aba da linguagem
                df.to_excel(writer, sheet_name=lang, index=False)
                print(f"✅ Aba '{lang}' processada e linkada com sucesso.")

            except Exception as e:
                print(f"🚨 Erro crítico ao processar {excel_path}: {e}")

    print(f"\n✅ Concluído! O arquivo foi salvo na raiz como: {OUTPUT_EXCEL}")


if __name__ == "__main__":
    main()