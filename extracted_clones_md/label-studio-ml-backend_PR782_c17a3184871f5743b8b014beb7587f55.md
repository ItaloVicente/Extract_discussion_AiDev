# 🔍 Clone Analysis | Project: label-studio-ml-backend | PR: #782

- **Commit SHA:** `452859ec856ea78a8e58e24e5447f039d4984827`
- **Clone Fingerprint:** `c17a3184871f5743b8b014beb7587f55`
- **Categoria:** `ini_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `label_studio_ml/examples/watsonx_llm/model_wsgi.py`
**Lines:** 92 to 106

```text
def parse_kwargs():
        param = dict()
        for k, v in args.kwargs:
            if v.isdigit():
                param[k] = int(v)
            elif v == 'True' or v == 'true':
                param[k] = True
            elif v == 'False' or v == 'false':
                param[k] = False
            elif isfloat(v):
                param[k] = float(v)
            else:
                param[k] = v
        return param
```

---

## 🧑‍💻 Clone Par 2
**File:** `label_studio_ml/examples/grounding_dino/_wsgi.py`
**Lines:** 85 to 99

```text
def parse_kwargs():
        param = dict()
        for k, v in args.kwargs:
            if v.isdigit():
                param[k] = int(v)
            elif v == 'True' or v == 'true':
                param[k] = True
            elif v == 'False' or v == 'false':
                param[k] = False
            elif isfloat(v):
                param[k] = float(v)
            else:
                param[k] = v
        return param
```

