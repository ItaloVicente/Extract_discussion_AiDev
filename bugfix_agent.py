import os
import pandas as pd
from datasets import load_dataset

EXCEL_FILE = "Final_Merged_Analysis.xlsx"


def fix_agent_in_excel():
    if not os.path.exists(EXCEL_FILE):
        print(f"🚨 Erro: Arquivo {EXCEL_FILE} não encontrado.")
        return

    print("⏳ Baixando metadados do Hugging Face (pull_request) para acessar a coluna 'agent'...")
    df_pr_hf = load_dataset("hao-li/AIDev", "pull_request", split="train").to_pandas()

    print(f"🔗 Corrigindo os nomes dos Agentes na planilha {EXCEL_FILE}...")

    all_sheets = pd.read_excel(EXCEL_FILE, sheet_name=None)

    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
        for lang, df in all_sheets.items():
            if df.empty or 'Project' not in df.columns:
                df.to_excel(writer, sheet_name=lang, index=False)
                continue

            df['Project'] = df['Project'].astype(str).str.strip()
            df['PR'] = df['PR'].astype(str).str.strip()

            agents_list = []

            for _, row in df.iterrows():
                proj = row['Project']
                pr_num = row['PR']

                matched_pr = df_pr_hf[
                    (df_pr_hf['number'] == int(pr_num)) &
                    (df_pr_hf['repo_url'].str.contains(f"/{proj}(?:/|$)", regex=True, case=False, na=False))
                    ]

                # CORREÇÃO CRÍTICA: Lendo o campo 'agent' ao invés de 'user'
                if not matched_pr.empty and 'agent' in matched_pr.columns:
                    agent_name = matched_pr.iloc[0]['agent']
                else:
                    agent_name = 'Desconhecido'

                agents_list.append(agent_name)

            if 'AI_Agent' in df.columns:
                df['AI_Agent'] = agents_list
            else:
                pr_idx = df.columns.get_loc('PR') + 1
                df.insert(pr_idx, 'AI_Agent', agents_list)

            df.to_excel(writer, sheet_name=lang, index=False)
            print(f"  ✅ Aba '{lang}' corrigida com sucesso.")


def main():
    fix_agent_in_excel()
    print("\n✅ Correção finalizada. A coluna 'AI_Agent' agora usa a classificação limpa!")


if __name__ == "__main__":
    main()