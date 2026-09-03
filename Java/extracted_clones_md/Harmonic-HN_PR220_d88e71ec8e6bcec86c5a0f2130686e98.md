# 🔍 Clone Analysis | Project: Harmonic-HN | PR: #220

- **Commit SHA:** `aef6095e6caae543218f6c557ae2847c40e52d1d`
- **Clone Fingerprint:** `d88e71ec8e6bcec86c5a0f2130686e98`
- **Categoria:** `ini_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `app/src/main/java/com/simon/harmonichackernews/utils/Utils.java`
**Lines:** 341 to 352

```text
public static ArrayList<String> getFilterWords(Context ctx) {
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(ctx);
        String prefText = prefs.getString("pref_filter", null);

        ArrayList<String> phrases = new ArrayList<>();
        if (!TextUtils.isEmpty(prefText)) {
            for (String phrase : prefText.split(",")) {
                phrases.add(phrase.trim());
            }
        }
        return phrases;
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `app/src/main/java/com/simon/harmonichackernews/utils/Utils.java`
**Lines:** 353 to 364

```text
public static ArrayList<String> getFilterDomains(Context ctx) {
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(ctx);
        String prefText = prefs.getString("pref_filter_domains", null);

        ArrayList<String> phrases = new ArrayList<>();
        if (!TextUtils.isEmpty(prefText)) {
            for (String phrase : prefText.split(",")) {
                phrases.add(phrase.trim());
            }
        }
        return phrases;
    }
```

