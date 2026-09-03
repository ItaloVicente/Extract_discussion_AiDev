# 🔍 Clone Analysis | Project: java-util | PR: #243

- **Commit SHA:** `9a12551c3bf4d41a41bb37bf8ffba4bab914cc90`
- **Clone Fingerprint:** `d7d883c46a6bb22e3b0d10f037b5b1cb`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/test/java/com/cedarsoftware/util/TrackingMapTest.java`
**Lines:** 288 to 302

```text
public void testInformAdditionalUsage() throws Exception {
        TrackingMap<String, Object> map = new TrackingMap<>(new CaseInsensitiveMap<String, Object>());
        map.put("first", "firstValue");
        map.put("second", "secondValue");
        map.put("third", "thirdValue");
        Collection<String> additionalUsage = new HashSet<>();
        additionalUsage.add("FiRsT");
        additionalUsage.add("ThirD");
        map.informAdditionalUsage(additionalUsage);
        map.remove("first");
        map.expungeUnused();
        assertEquals(1, map.size());
        assertEquals(map.get("thiRd"), "thirdValue");
        assertFalse(map.isEmpty());
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/test/java/com/cedarsoftware/util/TrackingMapTest.java`
**Lines:** 305 to 319

```text
public void testInformAdditionalUsage1() throws Exception {
        TrackingMap<String, Object> map = new TrackingMap<>(new CaseInsensitiveMap<String, Object>());
        map.put("first", "firstValue");
        map.put("second", "secondValue");
        map.put("third", "thirdValue");
        TrackingMap<String, Object> additionalUsage = new TrackingMap<>(map);
        additionalUsage.get("FiRsT");
        additionalUsage.get("ThirD");
        map.informAdditionalUsage(additionalUsage);
        map.remove("first");
        map.expungeUnused();
        assertEquals(1, map.size());
        assertEquals(map.get("thiRd"), "thirdValue");
        assertFalse(map.isEmpty());
    }
```

