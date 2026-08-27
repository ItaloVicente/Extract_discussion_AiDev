import os
import glob
import pandas as pd

INPUT_EXCEL = "Clone_Code_Classification.xlsx"
OUTPUT_EXCEL = "Clone_Code_Classification_Fixed.xlsx"

LANGUAGES = ["C#", "Java", "Python", "Ruby"]


def detect_language(project_name, md_filename):
    """Descobre a linguagem baseada na estrutura de pastas ou lendo a extensão do código no Markdown."""
    # Tentativa 1: Verifica a estrutura de pastas do projeto (se existir)
    for lang in LANGUAGES:
        if glob.glob(f"{lang}/clones_classified/{project_name}_*.csv"):
            return lang

    # Tentativa 2: Lê o Markdown gerado e identifica a extensão do arquivo original extraído
    md_path = os.path.join("extracted_clones_md", md_filename)
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if ".py`" in content or ".py\n" in content: return "Python"
            if ".java`" in content or ".java\n" in content: return "Java"
            if ".cs`" in content or ".cs\n" in content: return "C#"
            if ".rb`" in content or ".rb\n" in content: return "Ruby"

    return "Outros"  # Fallback caso não identifique


def main():
    if not os.path.exists(INPUT_EXCEL):
        print(f"🚨 Arquivo {INPUT_EXCEL} não encontrado!")
        return

    print(f"📖 Lendo o arquivo {INPUT_EXCEL}...")
    df = pd.read_excel(INPUT_EXCEL)

    fixed_urls = []
    detected_langs = []

    print("🔍 Limpando URLs e mapeando linguagens...")
    for _, row in df.iterrows():
        project = str(row['Project'])
        pr = str(row['PR'])
        fingerprint = str(row['Clone_Fingerprint'])

        # 1. Reconstrói a URL limpa (uma string pura para não quebrar o link)
        filename = f"{project}_PR{pr}_{fingerprint}.md"
        clean_url = f"https://github.com/ItaloVicente/Extract_discussion_AiDev/blob/main/extracted_clones_md/{filename}"
        fixed_urls.append(clean_url)

        # 2. Detecta a linguagem
        lang = detect_language(project, filename)
        detected_langs.append(lang)

    # Atualiza o DataFrame
    df['URL_Clone_Code'] = fixed_urls
    df['Language'] = detected_langs

    # 3. Gera o novo Excel separado por abas
    print(f"\n📊 Separando por abas e gerando {OUTPUT_EXCEL}...")
    with pd.ExcelWriter(OUTPUT_EXCEL, engine='openpyxl') as writer:
        for lang in df['Language'].unique():
            # Filtra pela linguagem e remove a coluna de apoio 'Language' para ficar limpo
            df_lang = df[df['Language'] == lang].drop(columns=['Language'])
            df_lang.to_excel(writer, sheet_name=lang, index=False)

    print(f"✅ Feito! Novo arquivo gerado: {OUTPUT_EXCEL}")


if __name__ == "__main__":
    main()