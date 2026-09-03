# 🔍 Clone Analysis | Project: reflex-web | PR: #1435

- **Commit SHA:** `4844bf68763b79b57802185a93447d296e9cec81`
- **Clone Fingerprint:** `bc49cb39c98356a64a31af1f652dbe33`
- **Categoria:** `ini_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `pcweb/templates/docpage/blocks/code.py`
**Lines:** 10 to 21

```text
def code_block(code: str, language: str):
    return rx.box(
        rx._x.code_block(
            code,
            language=language,
            class_name="code-block",
            can_copy=True,
        ),
        class_name="relative mb-4",
    )
```

---

## 🧑‍💻 Clone Par 2
**File:** `pcweb/templates/docpage/blocks/code.py`
**Lines:** 23 to 34

```text
def code_block_dark(code: str, language: str):
    return rx.box(
        rx._x.code_block(
            code,
            language=language,
            class_name="code-block",
            can_copy=True,
        ),
        class_name="relative",
    )
```

