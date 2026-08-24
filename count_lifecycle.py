import pandas as pd
from pathlib import Path
import glob

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

BASE_DIR = Path(".")

LANGUAGES = [
    "Java",
    "Ruby",
    "Python",
    "C#"
]

OUTPUT = "summary_pr_by_category_by_language.csv"

required_cols = {
    "project",
    "pr",
    "categoria",
    "start_commit",
    "end_commit",
    "total_commits"
}

all_summaries = []

# ==========================================================
# PROCESSAR CADA LINGUAGEM
# ==========================================================

for language in LANGUAGES:

    clone_dir = BASE_DIR / language / "clones_classified"

    if not clone_dir.exists():
        print(f"⚠️ Pasta não encontrada: {clone_dir}")
        continue

    csv_files = glob.glob(str(clone_dir / "*_clone_classified.csv"))

    print(f"\n📚 {language}: {len(csv_files)} arquivos")

    all_data = []

    for f in csv_files:
        try:
            df = pd.read_csv(f)

            if df.empty:
                continue

            if required_cols.issubset(df.columns):
                all_data.append(df[list(required_cols)])
            else:
                print(f"⚠️ Colunas ausentes em {f}")

        except pd.errors.EmptyDataError:
            continue

        except Exception as e:
            print(f"Erro em {f}: {e}")

    if not all_data:
        continue

    combined_df = pd.concat(all_data, ignore_index=True)

    # ======================================================
    # Corrigir categoria unique_ini_mei_final
    # ======================================================

    mask = (
        (combined_df["categoria"] == "ini_mei_final") &
        (combined_df["start_commit"] == 1) &
        (combined_df["end_commit"] == 1) &
        (combined_df["total_commits"] == 1)
    )

    combined_df.loc[mask, "categoria"] = "unique_ini_mei_final"

    # ======================================================
    # CONTAR PRS ÚNICAS POR CATEGORIA
    # ======================================================

    unique_pr_categories = combined_df[
        ["project", "pr", "categoria"]
    ].drop_duplicates()

    counts = (
        unique_pr_categories["categoria"]
        .value_counts()
        .reset_index()
    )

    counts.columns = ["categoria", "quantidade"]
    counts.insert(0, "linguagem", language)

    all_summaries.append(counts)

# ==========================================================
# SALVAR
# ==========================================================

if all_summaries:

    final_df = pd.concat(all_summaries, ignore_index=True)

    final_df.to_csv(OUTPUT, index=False)

    print("\nResumo final:")
    print(final_df)

    print(f"\n✅ Salvo em {OUTPUT}")

else:
    print("Nenhum dado encontrado.")