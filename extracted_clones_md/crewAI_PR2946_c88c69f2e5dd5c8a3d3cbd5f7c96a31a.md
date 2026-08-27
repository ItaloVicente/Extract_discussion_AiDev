# 🔍 Clone Analysis | Project: crewAI | PR: #2946

- **Commit SHA:** `1cfa3f8b2d10101fdf3d707b42fbb8836fc3c2c8`
- **Clone Fingerprint:** `c88c69f2e5dd5c8a3d3cbd5f7c96a31a`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `tests/telemetry/test_telemetry_disable.py`
**Lines:** 17 to 25

```text
def test_telemetry_environment_variables(env_var, value, expected_ready):
    """Test telemetry state with different environment variable configurations."""
    Telemetry._instance = None
    with patch.dict(os.environ, {env_var: value}):
        with patch("crewai.telemetry.telemetry.TracerProvider"):
            telemetry = Telemetry()
            assert telemetry.ready is expected_ready
```

---

## 🧑‍💻 Clone Par 2
**File:** `tests/telemetry/test_telemetry.py`
**Lines:** 23 to 31

```text
def test_telemetry_environment_variables(env_var, value, expected_ready):
    """Test telemetry state with different environment variable configurations."""
    Telemetry._instance = None
    with patch.dict(os.environ, {env_var: value}):
        with patch("crewai.telemetry.telemetry.TracerProvider"):
            telemetry = Telemetry()
            assert telemetry.ready is expected_ready
```

