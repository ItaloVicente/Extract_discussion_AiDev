# 🔍 Clone Analysis | Project: debug-gym | PR: #161

- **Commit SHA:** `0e3ceda6aae9098482e1e535c97553a8017c2068`
- **Clone Fingerprint:** `1a9c575a0fbd6068ae35aa804eb1d1b0`
- **Categoria:** `mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `tests/gym/tools/test_pdb.py`
**Lines:** 15 to 22

```text
def is_docker_running():
    try:
        subprocess.check_output(["docker", "ps"])
        return True
    except Exception:
        return False
```

---

## 🧑‍💻 Clone Par 2
**File:** `tests/gym/test_terminal.py`
**Lines:** 21 to 28

```text
def is_docker_running():
    try:
        subprocess.check_output(["docker", "ps"])
        return True
    except Exception:
        return False
```

