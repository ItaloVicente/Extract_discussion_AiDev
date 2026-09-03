# 🔍 Clone Analysis | Project: java-util | PR: #249

- **Commit SHA:** `f0b5c529cb30d83e24262fe55bbd8f9504bc8adb`
- **Clone Fingerprint:** `7e7daf2f09c5ffc4a3fccdfcf2c5f37b`
- **Categoria:** `ini_mei_final`

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

