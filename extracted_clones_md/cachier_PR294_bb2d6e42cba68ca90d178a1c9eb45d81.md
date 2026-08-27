# 🔍 Clone Analysis | Project: cachier | PR: #294

- **Commit SHA:** `9a2ed39bfe508b909df7ea30bcee299707e55043`
- **Clone Fingerprint:** `bb2d6e42cba68ca90d178a1c9eb45d81`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/cachier/cores/redis.py`
**Lines:** 189 to 201

```text
def wait_on_entry_calc(self, key: str) -> Any:
        """Wait on the entry with keys being calculated and returns result."""
        time_spent = 0
        while True:
            time.sleep(REDIS_SLEEP_DURATION_IN_SEC)
            time_spent += REDIS_SLEEP_DURATION_IN_SEC
            key, entry = self.get_entry_by_key(key)
            if entry is None:
                raise RecalculationNeeded()
            if not entry._processing:
                return entry.value
            self.check_calc_timeout(time_spent)
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/cachier/cores/mongo.py`
**Lines:** 132 to 143

```text
def wait_on_entry_calc(self, key: str) -> Any:
        time_spent = 0
        while True:
            time.sleep(MONGO_SLEEP_DURATION_IN_SEC)
            time_spent += MONGO_SLEEP_DURATION_IN_SEC
            key, entry = self.get_entry_by_key(key)
            if entry is None:
                raise RecalculationNeeded()
            if not entry._processing:
                return entry.value
            self.check_calc_timeout(time_spent)
```

