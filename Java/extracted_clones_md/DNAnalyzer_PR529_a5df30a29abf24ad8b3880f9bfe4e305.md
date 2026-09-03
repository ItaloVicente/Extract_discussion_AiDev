# 🔍 Clone Analysis | Project: DNAnalyzer | PR: #529

- **Commit SHA:** `b25afa03186c166f827966514fb7867d6fc609b3`
- **Clone Fingerprint:** `a5df30a29abf24ad8b3880f9bfe4e305`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/main/java/DNAnalyzer/api/DNAnalyzerApiController.java`
**Lines:** 556 to 570

```text
private String formatAsJson(String output) {
    StringBuilder json = new StringBuilder();
    json.append("{\"results\": [");

    String[] lines = output.split("\n");
    for (int i = 0; i < lines.length; i++) {
      json.append("\"").append(lines[i].replace("\"", "\\\"")).append("\"");
      if (i < lines.length - 1) {
        json.append(",");
      }
    }

    json.append("]}");
    return json.toString();
  }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/main/java/DNAnalyzer/web/AnalyzerController.java`
**Lines:** 159 to 173

```text
private String formatAsJson(String output) {
    StringBuilder json = new StringBuilder();
    json.append("{\"results\": [");

    String[] lines = output.split("\n");
    for (int i = 0; i < lines.length; i++) {
      json.append("\"").append(lines[i].replace("\"", "\\\"")).append("\"");
      if (i < lines.length - 1) {
        json.append(",");
      }
    }

    json.append("]}");
    return json.toString();
  }
```

