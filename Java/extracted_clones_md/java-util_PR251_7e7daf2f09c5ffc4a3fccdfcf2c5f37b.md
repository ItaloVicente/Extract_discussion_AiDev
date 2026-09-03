# 🔍 Clone Analysis | Project: java-util | PR: #251

- **Commit SHA:** `4f3d0d8187e5ff69f5ffab36b733862965cc52b9`
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
**Lines:** 38 to 43

```text
private static void writeResponse(HttpExchange exchange, int code, String body) throws IOException {
        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
        exchange.sendResponseHeaders(code, bytes.length);
        exchange.getResponseBody().write(bytes);
        exchange.close();
    }
```

