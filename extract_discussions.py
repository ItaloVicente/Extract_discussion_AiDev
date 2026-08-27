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

    df_pr = load_dataset("hao-li/AIDev", "pull_request", split="train").to_pandas()
    df_pr_comments = load_dataset("hao-li/AIDev", "pr_comments", split="train").to_pandas()
    df_pr_reviews = load_dataset("hao-li/AIDev", "pr_reviews", split="train").to_pandas()
    df_pr_rev_comments = load_dataset("hao-li/AIDev", "pr_review_comments", split="train").to_pandas()

    print("🗂️ Indexando tabelas para buscas super rápidas...")

    df_pr['body'] = df_pr['body'].fillna("*(Sem descrição fornecida)*")
    df_pr_comments['body'] = df_pr_comments['body'].fillna("")
    df_pr_reviews['body'] = df_pr_reviews['body'].fillna("")
    df_pr_rev_comments['body'] = df_pr_rev_comments['body'].fillna("")

    return df_pr, df_pr_comments, df_pr_reviews, df_pr_rev_comments


def get_unique_prs_from_csvs():
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
                        else:
                            if has_unmerged:
                                pr_dict[key] = True

            except Exception as e:
                print(f"⚠️ Erro ao ler o CSV {file}: {e}")

    unique_pr_list = [
        {"lang": k[0], "project": k[1], "pr_number": k[2], "has_unmerged_clone": "Yes" if v else "No"}
        for k, v in pr_dict.items()
    ]

    print(f"✅ Encontradas {len(unique_pr_list)} Pull Requests únicas para extração.")
    return unique_pr_list


def create_markdown_content(project, pr_number, pr_row, comments_df, reviews_df, rev_comments_df):
    """Monta a estrutura do arquivo Markdown em ordem puramente cronológica."""

    pr_id = pr_row['id']
    pr_url = pr_row.get('html_url', 'URL não disponível')

    # 1. Filtragem relacional
    pr_comments = comments_df[comments_df['pr_id'] == pr_id]
    pr_reviews = reviews_df[reviews_df['pr_id'] == pr_id]
    review_ids = pr_reviews['id'].tolist()
    pr_rev_comments = rev_comments_df[rev_comments_df['pull_request_review_id'].isin(review_ids)]

    # 2. Empacotamento de Eventos para Ordenação Temporal
    events = []

    def parse_date(date_val):
        """Converte string para timestamp seguro, jogando NaNs para o início do tempo."""
        dt = pd.to_datetime(date_val, errors='coerce')
        if pd.isna(dt):
            return pd.Timestamp.min
        return dt

    # 2.1 Adiciona o Body da PR
    pr_date = pr_row.get('created_at', pr_row.get('updated_at', None))
    events.append({
        'type': 'PR BODY',
        'timestamp': parse_date(pr_date),
        'date_str': str(pr_date) if pd.notna(pr_date) else 'Data desconhecida',
        'author': pr_row.get('user', 'Desconhecido'),
        'body': str(pr_row['body']).strip(),
        'extra': {}
    })

    # 2.2 Adiciona Comentários Gerais
    for _, row in pr_comments.iterrows():
        c_date = row.get('created_at', row.get('updated_at', None))
        events.append({
            'type': 'COMENTÁRIO GERAL',
            'timestamp': parse_date(c_date),
            'date_str': str(c_date) if pd.notna(c_date) else 'Data desconhecida',
            'author': row.get('user', 'Desconhecido'),
            'body': str(row['body']).strip(),
            'extra': {}
        })

    # 2.3 Adiciona Reviews (Geralmente usam submitted_at)
    for _, row in pr_reviews.iterrows():
        r_date = row.get('submitted_at', row.get('created_at', None))
        events.append({
            'type': f"REVISÃO: {row.get('state', 'Sem Status')}",
            'timestamp': parse_date(r_date),
            'date_str': str(r_date) if pd.notna(r_date) else 'Data desconhecida',
            'author': row.get('user', 'Desconhecido'),
            'body': str(row['body']).strip(),
            'extra': {}
        })

    # 2.4 Adiciona Comentários de Linha
    for _, row in pr_rev_comments.iterrows():
        l_date = row.get('created_at', row.get('updated_at', None))
        events.append({
            'type': 'COMENTÁRIO DE LINHA',
            'timestamp': parse_date(l_date),
            'date_str': str(l_date) if pd.notna(l_date) else 'Data desconhecida',
            'author': row.get('user', 'Desconhecido'),
            'body': str(row['body']).strip(),
            'extra': {
                'path': row.get('path', 'Arquivo desconhecido'),
                'position': row.get('position', 'Posição desconhecida')
            }
        })

    # 3. Ordenação Cronológica Definitiva
    events.sort(key=lambda x: x['timestamp'])

    # 4. Construção da String Markdown
    md = f"# Discussões da PR #{pr_number} | Projeto: {project}\n\n"
    md += f"**🔗 Link da PR:** [{pr_url}]({pr_url})\n\n"

    md += "## 📊 Resumo de Interações\n\n"
    md += "| Origem da Tabela | Quantidade de Registros |\n"
    md += "| :--- | :--- |\n"
    md += f"| `pull_request` (Body) | 1 |\n"
    md += f"| `pr_comments` | {len(pr_comments)} |\n"
    md += f"| `pr_reviews` | {len(pr_reviews)} |\n"
    md += f"| `pr_review_comments` | {len(pr_rev_comments)} |\n\n"

    md += "---\n\n"
    md += "## 🕒 Linha do Tempo da Conversa\n\n"

    # Renderiza os eventos ordenados
    for ev in events:
        author = ev['author']
        date_str = ev['date_str'].replace("T", " ").replace("Z", "")  # Limpa formatação ISO
        ev_type = ev['type']
        body = ev['body']

        # Ícones baseados no tipo
        icon = "📝" if "BODY" in ev_type else "💬" if "GERAL" in ev_type else "🛠️" if "REVISÃO" in ev_type else "📍"

        md += f"### {icon} [{ev_type}] por **{author}** em {date_str}\n\n"

        # Se for comentário de linha, adiciona o path
        if "LINHA" in ev_type:
            path = ev['extra'].get('path', '')
            pos = ev['extra'].get('position', '')
            md += f"**Arquivo:** `{path}` (Linha/Pos: {pos})\n\n"

        # Trata o Body da mensagem
        if body and body.lower() not in ['nan', 'none']:
            md += f"> {body.replace(chr(10), chr(10) + '> ')}\n\n"
        else:
            md += "> *(Sem comentário / Texto vazio)*\n\n"

        md += "---\n\n"

    return md


def main():
    df_pr, df_pr_comments, df_pr_reviews, df_pr_rev_comments = load_and_index_hf_datasets()
    prs_to_process = get_unique_prs_from_csvs()

    if not prs_to_process:
        print("🚨 Nenhuma PR encontrada para processamento. Encerrando.")
        return

    excel_data = {lang: [] for lang in LANGUAGES}

    print("🚀 Iniciando extração e formatação de discussões cronológicas...")

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

        md_content = create_markdown_content(
            project, pr_number, pr_row,
            df_pr_comments, df_pr_reviews, df_pr_rev_comments
        )

        save_dir = os.path.join(OUTPUT_BASE_DIR, lang, project)
        os.makedirs(save_dir, exist_ok=True)

        file_path = os.path.join(save_dir, f"{pr_number}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        excel_data[lang].append({
            "Project": project,
            "PR": pr_number,
            "Has Unmerged Clone": has_unmerged_clone,
            "URL": pr_url,
            "Has Discussion?": ""
        })

    print("\n📊 Gerando arquivo Excel com o resumo...")
    excel_path = os.path.join(OUTPUT_BASE_DIR, "Discussions_Summary.xlsx")

    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for lang in LANGUAGES:
            df_lang = pd.DataFrame(excel_data[lang])
            if df_lang.empty:
                df_lang = pd.DataFrame(columns=["Project", "PR", "Has Unmerged Clone", "URL", "Has Discussion?"])
            df_lang.to_excel(writer, sheet_name=lang, index=False)

    print(f"✅ Arquivos Markdown salvos na pasta '{OUTPUT_BASE_DIR}/'.")
    print(f"✅ Planilha Excel salva em: {excel_path}")


if __name__ == "__main__":
    main()