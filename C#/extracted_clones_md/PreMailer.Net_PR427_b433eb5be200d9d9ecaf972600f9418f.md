# 🔍 Clone Analysis | Project: PreMailer.Net | PR: #427

- **Commit SHA:** `4fb19d5d55345cf40c331d93d3c5da74a97fde5b`
- **Clone Fingerprint:** `b433eb5be200d9d9ecaf972600f9418f`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `PreMailer.Net/PreMailer.Net/Html/EmailHtmlMarkupFormatter.cs`
**Lines:** 36 to 46

```text
public override string Text(ICharacterData text)
        {
            var result = base.Text(text);
            
            foreach (var entity in EntityReplacements)
            {
                result = result.Replace(entity.Key, entity.Value);
            }
            
            return result;
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `PreMailer.Net/PreMailer.Net/Html/PreserveEntitiesHtmlMarkupFormatter.cs`
**Lines:** 28 to 38

```text
public override string Text(ICharacterData text)
        {
            var result = base.Text(text);
            
            foreach (var entity in EntityReplacements)
            {
                result = result.Replace(entity.Key, entity.Value);
            }
            
            return result;
        }
```

