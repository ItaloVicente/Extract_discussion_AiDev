# 🔍 Clone Analysis | Project: java-util | PR: #250

- **Commit SHA:** `896eb635b5e3319d81fdbfad3064c2105e261c50`
- **Clone Fingerprint:** `7e7daf2f09c5ffc4a3fccdfcf2c5f37b`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/test/java/com/cedarsoftware/util/UrlUtilitiesTest.java`
**Lines:** 53 to 58

```text
private static void writeResponse(HttpExchange exchange, int code, String body) throws IOException {
        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(code, bytes.length);
        exchange.getResponseBody().write(bytes);
        exchange.close();
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/test/java/com/cedarsoftware/util/UrlInvocationHandlerTest.java`
**Lines:** 37 to 42

```text
private static void writeResponse(HttpExchange exchange, int code, String body) throws IOException {
        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(code, bytes.length);
        exchange.getResponseBody().write(bytes);
        exchange.close();
    }
```

