# 🔍 Clone Analysis | Project: json-io | PR: #378

- **Commit SHA:** `190a9b5063642785f7616ea324a8b1fd17e74bbe`
- **Clone Fingerprint:** `e1e0ea9c175aa020da6e815f1ef31b5a`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/main/java/com/cedarsoftware/io/ReadOptionsBuilder.java`
**Lines:** 707 to 717

```text
public ReadOptionsBuilder addCustomOption(String key, Object value) {
        if (key == null) {
            throw new JsonIoException("Custom option key must not be null.");
        }
        if (value == null) {
            options.customOptions.remove(key);
        } else {
            options.customOptions.put(key, value);
        }
        return this;
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/main/java/com/cedarsoftware/io/WriteOptionsBuilder.java`
**Lines:** 716 to 726

```text
public WriteOptionsBuilder addCustomOption(String key, Object value) {
        if (key == null) {
            throw new JsonIoException("Custom option key must not be null.");
        }
        if (value == null) {
            options.customOptions.remove(key);
        } else {
            options.customOptions.put(key, value);
        }
        return this;
    }
```

