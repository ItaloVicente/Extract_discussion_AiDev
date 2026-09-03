# 🔍 Clone Analysis | Project: java-util | PR: #169

- **Commit SHA:** `fdf62a1fcc8e6e41602261078d80fb166590ba25`
- **Clone Fingerprint:** `6c5e508da95786ebadf083e123cbd21c`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/main/java/com/cedarsoftware/util/cache/LockingLRUCacheStrategy.java`
**Lines:** 246 to 255

```text
public void clear() {
        lock.lock();
        try {
            head.next = tail;
            tail.prev = head;
            cache.clear();
        } finally {
            lock.unlock();
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/main/java/com/cedarsoftware/util/TTLCache.java`
**Lines:** 369 to 379

```text
public void clear() {
        cacheMap.clear();
        lock.lock();
        try {
            // Reset the linked list
            head.next = tail;
            tail.prev = head;
        } finally {
            lock.unlock();
        }
    }
```

