# 🔍 Clone Analysis | Project: Chronicle-Bytes | PR: #673

- **Commit SHA:** `b3dd1e32af359576359a16d66a423dd8dd32730e`
- **Clone Fingerprint:** `42196b41d1b08bb0f9e1f3a3e3b25429`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `src/main/java/net/openhft/chronicle/bytes/internal/ChunkedMappedFile.java`
**Lines:** 302 to 324

```text
protected void performRelease() {
        try {
            synchronized (stores) {
                for (int i = 0; i < stores.size(); i++) {
                    final MappedBytesStore mbs = stores.get(i);
                    if (mbs != null && RETAIN) {
                        // this MappedFile is the only referrer to the MappedBytesStore at this point,
                        // so ensure that it is released
                        try {
                            mbs.release(this);
                        } catch (ClosedIllegalStateException e) {
                            Jvm.debug().on(getClass(), e);
                        }
                    }
                    // Dereference released entities
                    stores.set(i, null);
                }
            }
        } finally {
            closeQuietly(raf);
            setClosed();
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/main/java/net/openhft/chronicle/bytes/internal/SingleMappedFile.java`
**Lines:** 218 to 234

```text
protected void performRelease() {
        try {
            final MappedBytesStore mbs = store;
            if (mbs != null && RETAIN) {
                // this MappedFile is the only referrer to the MappedBytesStore at this point,
                // so ensure that it is released
                try {
                    mbs.release(this);
                } catch (ClosedIllegalStateException e) {
                    Jvm.debug().on(getClass(), e);
                }
            }
        } finally {
            closeQuietly(raf);
            setClosed();
        }
    }
```

