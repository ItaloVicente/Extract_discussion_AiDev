# 🔍 Clone Analysis | Project: green-metrics-tool | PR: #1253

- **Commit SHA:** `8fd6aa59f3993328d6d60bf8d8df5ed24f4bb92d`
- **Clone Fingerprint:** `43e124e334ecf8e218ad021f6e5be916`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `tests/lib/test_schema_checker.py`
**Lines:** 13 to 20

```text
def test_schema_checker_valid():
    usage_scenario_name = 'schema_checker_valid.yml'
    usage_scenario_path = os.path.join(CURRENT_DIR, '../data/usage_scenarios/schema_checker/', usage_scenario_name)
    with open(usage_scenario_path, encoding='utf8') as file:
        usage_scenario = yaml.safe_load(file)
    schema_checker = SchemaChecker(validate_compose_flag=True)
    schema_checker.check_usage_scenario(usage_scenario)
```

---

## 🧑‍💻 Clone Par 2
**File:** `tests/lib/test_schema_checker.py`
**Lines:** 55 to 63

```text
def test_schema_checker_network_alias():
    usage_scenario_name = 'schema_checker_valid_network_alias.yml'
    usage_scenario_path = os.path.join(CURRENT_DIR, '../data/usage_scenarios/schema_checker/', usage_scenario_name)
    with open(usage_scenario_path, encoding='utf8') as file:
        usage_scenario = yaml.safe_load(file)
    schema_checker = SchemaChecker(validate_compose_flag=True)
    schema_checker.check_usage_scenario(usage_scenario)
```

