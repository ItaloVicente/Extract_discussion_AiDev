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
    """Lê as pastas locais e retorna uma lista única de dicionários com os dados da PR."""
    pr_list = []
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

                    # Extrair pares únicos
                    unique_pairs = df_csv[['project', 'pr']].drop_duplicates()
                    for _, row in unique_pairs.iterrows():
                        pr_list.append({
                            "lang": lang,
                            "project": str(row['project']),
                            "pr_number": int(row['pr'])
                        })
            except Exception as e:
                print(f"⚠️ Erro ao ler o CSV {file}: {e}")

    unique_pr_list = [dict(t) for t in {tuple(d.items()) for d in pr_list}]
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

    print("🚀 Iniciando extração e formatação de discussões...")

    for item in tqdm(prs_to_process, desc="Gerando arquivos Markdown"):
        lang = item['lang']
        project = item['project']
        pr_number = item['pr_number']

        matched_pr = df_pr[
            (df_pr['number'] == pr_number) &
            (df_pr['repo_url'].str.contains(f"/{project}(?:/|$)", regex=True, case=False, na=False))
            ]

        if matched_pr.empty:
            continue

        pr_row = matched_pr.iloc[0]

        md_content = create_markdown_content(
            project, pr_number, pr_row,
            df_pr_comments, df_pr_reviews, df_pr_rev_comments
        )

        save_dir = os.path.join(OUTPUT_BASE_DIR, lang, project)
        os.makedirs(save_dir, exist_ok=True)

        file_path = os.path.join(save_dir, f"{pr_number}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)

    print(f"\n🎉 Processo concluído! Arquivos salvos na pasta '{OUTPUT_BASE_DIR}/'.")


if __name__ == "__main__":
    main()