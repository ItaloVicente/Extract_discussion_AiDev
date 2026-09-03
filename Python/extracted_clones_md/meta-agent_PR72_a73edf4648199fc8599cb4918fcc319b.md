# 🔍 Clone Analysis | Project: meta-agent | PR: #72

- **Commit SHA:** `d4131a16b8c67378ab27bdf41f35d657faaf4750`
- **Clone Fingerprint:** `a73edf4648199fc8599cb4918fcc319b`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `tests/unit/test_sandbox_manager.py`
**Lines:** 165 to 175

```text
def test_invalid_command(monkeypatch, tmp_path):
    fake_client = MagicMock()
    fake_client.ping.return_value = None
    monkeypatch.setattr(sm.docker, "from_env", lambda: fake_client)
    manager = SandboxManager()
    code_dir = tmp_path / "code"
    code_dir.mkdir()
    with pytest.raises(ValueError):
        manager.run_code_in_sandbox(code_dir, ["python; rm -rf /"])
```

---

## 🧑‍💻 Clone Par 2
**File:** `tests/unit/test_sandbox_manager.py`
**Lines:** 176 to 186

```text
def test_invalid_resources(monkeypatch, tmp_path):
    fake_client = MagicMock()
    fake_client.ping.return_value = None
    monkeypatch.setattr(sm.docker, "from_env", lambda: fake_client)
    manager = SandboxManager()
    code_dir = tmp_path / "code"
    code_dir.mkdir()
    with pytest.raises(ValueError):
        manager.run_code_in_sandbox(code_dir, ["python"], cpu_shares=-1)
```

