# 🔍 Clone Analysis | Project: Harmonic-HN | PR: #216

- **Commit SHA:** `3423d9759f97a7bc64501022961c7f593fd991de`
- **Clone Fingerprint:** `d88e71ec8e6bcec86c5a0f2130686e98`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `app/src/main/java/com/simon/harmonichackernews/utils/Utils.java`
**Lines:** 289 to 300

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
**Lines:** 301 to 312

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

