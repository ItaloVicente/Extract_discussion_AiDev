import os
import pandas as pd

# === Configurações dos Arquivos ===
CLONES_EXCEL = "Clone_Code_Classification_Fixed.xlsx"
DISCUSSIONS_EXCEL = "Discussions_Summary.xlsx"
OUTPUT_EXCEL = "Final_Merged_Analysis.xlsx"

LANGUAGES = ["C#", "Java", "Python", "Ruby"]


def main():
    if not os.path.exists(CLONES_EXCEL) or not os.path.exists(DISCUSSIONS_EXCEL):
        print("🚨 ERRO: Os arquivos base não foram encontrados na raiz.")
        print(f"Verifique se '{CLONES_EXCEL}' e '{DISCUSSIONS_EXCEL}' existem.")
        return

    print("🔗 Iniciando o merge das URLs (Clones + Discussões)...")

    with pd.ExcelWriter(OUTPUT_EXCEL, engine='openpyxl') as writer:
        for lang in LANGUAGES:
            print(f"Processando aba: {lang}...")

            try:
                # 1. Lê a aba específica em ambos os arquivos
                df_clones = pd.read_excel(CLONES_EXCEL, sheet_name=lang)
                df_disc = pd.read_excel(DISCUSSIONS_EXCEL, sheet_name=lang)

                # Se as abas estiverem vazias, apenas recria a aba vazia no destino
                if df_clones.empty:
                    df_clones.to_excel(writer, sheet_name=lang, index=False)
                    continue

                # 2. Padroniza as chaves de busca (Project e PR) para string, evitando erros de tipo
                df_clones['Project'] = df_clones['Project'].astype(str).str.strip()
                df_clones['PR'] = df_clones['PR'].astype(str).str.strip()

                df_disc['Project'] = df_disc['Project'].astype(str).str.strip()
                df_disc['PR'] = df_disc['PR'].astype(str).str.strip()

                # 3. Pega apenas as colunas que importam do Excel de discussões
                # Renomeia a coluna 'URL' da discussão para não conflitar
                df_disc_subset = df_disc[['Project', 'PR', 'URL', 'Has Discussion?']].copy()
                df_disc_subset.rename(columns={'URL': 'URL_Discussion'}, inplace=True)

                # 4. Faz o Merge (Procura as linhas onde Project e PR batem)
                # Remove duplicatas no df_disc para evitar duplicação de linhas no merge
                df_disc_subset = df_disc_subset.drop_duplicates(subset=['Project', 'PR'])

                merged_df = pd.merge(df_clones, df_disc_subset, on=['Project', 'PR'], how='left')

                # 5. Salva na aba correspondente
                merged_df.to_excel(writer, sheet_name=lang, index=False)

            except Exception as e:
                print(f"⚠️ Aviso: Não foi possível processar a aba {lang}. Detalhe: {e}")

    print(f"\n✅ Merge finalizado com sucesso! Arquivo gerado: {OUTPUT_EXCEL}")


if __name__ == "__main__":
    main()