import os
import glob
import pandas as pd
from datasets import load_dataset

LANGUAGES = ["C#", "Java", "Python", "Ruby"]
EXCEL_FILE = "Final_Merged_Analysis.xlsx"


def fix_markdown_files():
    print("🛠️ 1/2: Corrigindo a formatação de código nos arquivos Markdown...")
    # Mapeia as linguagens das pastas para a sintaxe suportada no Markdown
    lang_map = {'C#': 'csharp', 'Java': 'java', 'Python': 'python', 'Ruby': 'ruby'}

    for lang in LANGUAGES:
        md_dir = os.path.join(lang, "extracted_clones_md")
        if not os.path.exists(md_dir):
            continue

        md_files = glob.glob(os.path.join(md_dir, "*.md"))
        mk_lang = lang_map.get(lang, 'text')

        count = 0
        for file_path in md_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Substitui o bloco "```text" pelo bloco da linguagem "```python", etc.
            if "```text" in content:
                new_content = content.replace("```text", f"```{mk_lang}")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

        if count > 0:
            print(f"  -> {count} arquivos atualizados na pasta {lang}")


def add_agent_to_excel():
    if not os.path.exists(EXCEL_FILE):
        print(f"🚨 Erro: Arquivo {EXCEL_FILE} não encontrado para atualizar a planilha.")
        return

    print("\n⏳ 2/2: Baixando metadados do Hugging Face para identificar Agentes...")
    df_pr_hf = load_dataset("hao-li/AIDev", "pull_request", split="train").to_pandas()

    print(f"🔗 Injetando a coluna 'AI_Agent' na planilha {EXCEL_FILE}...")

    # Lê todas as abas (linguagens) de uma vez
    all_sheets = pd.read_excel(EXCEL_FILE, sheet_name=None)

    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
        for lang, df in all_sheets.items():
            if df.empty or 'Project' not in df.columns:
                df.to_excel(writer, sheet_name=lang, index=False)
                continue

            # Garante que os tipos são strings para a busca
            df['Project'] = df['Project'].astype(str).str.strip()
            df['PR'] = df['PR'].astype(str).str.strip()

            agents_list = []

            for _, row in df.iterrows():
                proj = row['Project']
                pr_num = row['PR']

                # Busca a PR no dataset do Hugging Face
                matched_pr = df_pr_hf[
                    (df_pr_hf['number'] == int(pr_num)) &
                    (df_pr_hf['repo_url'].str.contains(f"/{proj}(?:/|$)", regex=True, case=False, na=False))
                    ]

                agent_name = matched_pr.iloc[0].get('user', 'Desconhecido') if not matched_pr.empty else 'Desconhecido'
                agents_list.append(agent_name)

            # Insere a coluna AI_Agent logo depois de PR (ou atualiza se já existir)
            if 'AI_Agent' in df.columns:
                df['AI_Agent'] = agents_list
            else:
                pr_idx = df.columns.get_loc('PR') + 1
                df.insert(pr_idx, 'AI_Agent', agents_list)

            df.to_excel(writer, sheet_name=lang, index=False)
            print(f"  ✅ Aba '{lang}' atualizada com sucesso.")


def main():
    fix_markdown_files()
    add_agent_to_excel()
    print("\n✅ Bugfix finalizado. Todos os arquivos foram atualizados mantendo os dados originais!")


if __name__ == "__main__":
    main()