# 🔍 Clone Analysis | Project: Java-Thread-Affinity | PR: #142

- **Commit SHA:** `cecc3585a45f99f1eb7afc7b9260c46b0c913da3`
- **Clone Fingerprint:** `c7926b4b9aa91edf11b2af62fcc0ce8d`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `affinity/src/main/java/net/openhft/affinity/impl/SolarisJNAAffinity.java`
**Lines:** 61 to 70

```text
public int getThreadId() {
        Integer tid = THREAD_ID.get();
        if (tid == null) {
            tid = CLibrary.INSTANCE.pthread_self();
            //The tid assumed to be an unsigned 24 bit, see net.openhft.lang.Jvm.getMaxPid()
            tid = tid & 0xFFFFFF;
            THREAD_ID.set(tid);
        }
        return tid;
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `affinity/src/main/java/net/openhft/affinity/impl/OSXJNAAffinity.java`
**Lines:** 61 to 70

```text
public int getThreadId() {
        Integer tid = THREAD_ID.get();
        if (tid == null) {
            tid = CLibrary.INSTANCE.pthread_self();
            //The tid assumed to be an unsigned 24 bit, see net.openhft.lang.Jvm.getMaxPid()
            tid = tid & 0xFFFFFF;
            THREAD_ID.set(tid);
        }
        return tid;
    }
```

