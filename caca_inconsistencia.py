import pandas as pd
from pathlib import Path
import glob

BASE_DIR = Path(".")

LANGUAGES = [
    "Java",
    "Ruby",
    "Python",
    "C#"
]

for language in LANGUAGES:

    clone_dir = BASE_DIR / language / "clones_classified"

    if not clone_dir.exists():
        continue

    csvs = glob.glob(str(clone_dir / "*_clone_classified.csv"))

    dfs = []

    for csv in csvs:
        try:
            df = pd.read_csv(csv)

            if df.empty:
                continue

            # mesma correção do seu script
            mask = (
                (df["categoria"] == "ini_mei_final") &
                (df["start_commit"] == 1) &
                (df["end_commit"] == 1) &
                (df["total_commits"] == 1)
            )

            df.loc[mask, "categoria"] = "unique_ini_mei_final"

            dfs.append(df)

        except Exception:
            pass

    if not dfs:
        continue

    df = pd.concat(dfs, ignore_index=True)

    print(f"\n====== {language} ======")

    # categorias presentes em cada PR
    grouped = (
        df.groupby(["project", "pr"])["categoria"]
        .unique()
        .reset_index()
    )

    total_reviews = len(grouped)

    unique_reviews = 0
    invalid_reviews = []

    for _, row in grouped.iterrows():

        categorias = set(row["categoria"])

        if "unique_ini_mei_final" in categorias:

            if len(categorias) == 1:
                unique_reviews += 1
            else:
                invalid_reviews.append({
                    "project": row["project"],
                    "pr": row["pr"],
                    "categorias": sorted(categorias)
                })

    print(f"Total de reviews: {total_reviews}")
    print(f"Reviews unique_ini_mei_final: {unique_reviews}")
    print(f"Reviews NÃO unique_ini_mei_final: {total_reviews - unique_reviews}")

    if invalid_reviews:
        print("\n⚠️ Reviews inconsistentes encontradas:")
        for r in invalid_reviews:
            print(r)
    else:
        print("\n✅ Nenhuma inconsistência encontrada.")