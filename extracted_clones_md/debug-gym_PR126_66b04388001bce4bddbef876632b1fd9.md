# 🔍 Clone Analysis | Project: debug-gym | PR: #126

- **Commit SHA:** `8cc9b992f0fbe31191af9a55f1e3af20760b9ef7`
- **Clone Fingerprint:** `66b04388001bce4bddbef876632b1fd9`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `analysis/figure_9.py`
**Lines:** 87 to 114

```text
def analyze_froggy_results_with_seeds(base_model_name, seeds=[0, 1, 2]):
    """
    Analyzes and averages results across different seeds for a base model name

    Args:
        base_model_name (str): Base path without seed (e.g. '../exps/swe-bench/rewrite_o3-mini')
        seeds (list): List of seeds to average over

    Returns:
        pd.DataFrame: DataFrame containing averaged results by task
    """
    all_dfs = []

    for seed in seeds:
        model_path = f"{base_model_name}_{seed}"
        try:
            df = analyze_froggy_results(model_path)
        except:
            continue
        df["seed"] = seed
        all_dfs.append(df)

    # Combine all DataFrames
    combined_df = pd.concat(all_dfs)

    return combined_df
```

---

## 🧑‍💻 Clone Par 2
**File:** `analysis/figure_12.py`
**Lines:** 160 to 190

```text
def analyze_froggy_results_with_seeds(base_model_name, seeds=[0, 1, 2]):
    """
    Analyzes and averages results across different seeds for a base model name

    Args:
        base_model_name (str): Base path without seed (e.g. '../exps/swe-bench/rewrite_o3-mini')
        seeds (list): List of seeds to average over

    Returns:
        pd.DataFrame: DataFrame containing averaged results by task
    """
    all_dfs = []

    for seed in seeds:
        model_path = f"{base_model_name}_{seed}"
        try:
            df = analyze_froggy_results(model_path)
        except:
            continue
        df["seed"] = seed
        all_dfs.append(df)

    # Combine all DataFrames
    combined_df = pd.concat(all_dfs)

    # Group by task and calculate means
    averaged_df = combined_df.groupby("task").agg({"success": "mean"}).reset_index()

    return combined_df
```

