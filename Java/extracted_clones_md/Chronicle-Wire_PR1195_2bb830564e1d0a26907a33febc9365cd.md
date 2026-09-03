# 🔍 Clone Analysis | Project: Chronicle-Wire | PR: #1195

- **Commit SHA:** `e97e2de534bdcc6d8dee8588ec0785166e00bd81`
- **Clone Fingerprint:** `2bb830564e1d0a26907a33febc9365cd`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/test/java/net/openhft/chronicle/wire/MarshallableOutBuilderTest.java`
**Lines:** 115 to 136

```text
public void http() throws IOException, InterruptedException {
        InetSocketAddress address = new InetSocketAddress(0);
        HttpServer server = HttpServer.create(address, 0);
        int port = server.getAddress().getPort();
        BlockingQueue<String> queue = new LinkedBlockingQueue<>();
        server.createContext("/echo", new Handler(queue));
        server.start();
        try {
            @SuppressWarnings("deprecation")
            final URL url = new URL("http://localhost:" + port + "/echo");
            writeMessages(url);
            assertEquals(
                    "{\"mid\":\"mid\",\"next\":1,\"echo\":\"echo-1\"}\n",
                    queue.poll(1, TimeUnit.SECONDS));
            assertEquals(
                    "{\"mid2\":\"mid2\",\"next2\":\"word\",\"echo\":\"echo-2\"}\n",
                    queue.poll(1, TimeUnit.SECONDS));
            assertNull(queue.poll(1, TimeUnit.MILLISECONDS));
        } finally {
            server.stop(1);
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/test/java/net/openhft/chronicle/wire/MarshallableOutBuilderTest.java`
**Lines:** 141 to 162

```text
public void http2() throws IOException, InterruptedException {
        InetSocketAddress address = new InetSocketAddress(0);
        HttpServer server = HttpServer.create(address, 0);
        int port = server.getAddress().getPort();
        BlockingQueue<String> queue = new LinkedBlockingQueue<>();
        server.createContext("/echo", new Handler(queue));
        server.start();
        try {
            @SuppressWarnings("deprecation")
            final URL url = new URL("http://localhost:" + port + "/echo/append");
            writeMessages(url);
            assertEquals(
                    "{\"mid\":\"mid\",\"next\":1,\"echo\":\"echo-1\"}\n",
                    queue.poll(1, TimeUnit.SECONDS));
            assertEquals(
                    "{\"mid2\":\"mid2\",\"next2\":\"word\",\"echo\":\"echo-2\"}\n",
                    queue.poll(1, TimeUnit.SECONDS));
            assertNull(queue.poll(1, TimeUnit.MILLISECONDS));
        } finally {
            server.stop(1);
        }
    }
```

