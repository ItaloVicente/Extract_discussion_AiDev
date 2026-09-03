# 🔍 Clone Analysis | Project: pulsar | PR: #24542

- **Commit SHA:** `b42729750fd9ad761ee02d3a2ada40a6ad44bdbc`
- **Clone Fingerprint:** `2ebff046ce777f11f7f0b86ecde7d415`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `pulsar-broker/src/main/java/org/apache/pulsar/broker/delayed/bucket/BucketDelayedDeliveryTracker.java`
**Lines:** 580 to 595

```text
protected long nextDeliveryTime() {
        // Use optimistic read for frequently called method
        long stamp = stampedLock.tryOptimisticRead();
        long result = nextDeliveryTimeUnsafe();


        if (!stampedLock.validate(stamp)) {
            stamp = stampedLock.readLock();
            try {
                result = nextDeliveryTimeUnsafe();
            } finally {
                stampedLock.unlockRead(stamp);
            }
        }
        return result;
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `pulsar-broker/src/main/java/org/apache/pulsar/broker/delayed/bucket/BucketDelayedDeliveryTracker.java`
**Lines:** 789 to 805

```text
public boolean containsMessage(long ledgerId, long entryId) {
        // Try optimistic read first for best performance
        long stamp = stampedLock.tryOptimisticRead();
        boolean result = containsMessageUnsafe(ledgerId, entryId);


        if (!stampedLock.validate(stamp)) {
            // Fall back to read lock if validation fails
            stamp = stampedLock.readLock();
            try {
                result = containsMessageUnsafe(ledgerId, entryId);
            } finally {
                stampedLock.unlockRead(stamp);
            }
        }
        return result;
    }
```

