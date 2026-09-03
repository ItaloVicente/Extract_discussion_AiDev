# 🔍 Clone Analysis | Project: java-util | PR: #356

- **Commit SHA:** `dd338b70cfbabe78fcd91893bdfdcaa7278dfa34`
- **Clone Fingerprint:** `78d4ab83b32cdaf515fe0a84617d44b9`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/test/java/com/cedarsoftware/util/MultiKeyMapTest.java`
**Lines:** 222 to 251

```text
void testSingleElementArrayKeysFlattenInCaseInsensitiveMap3() {
        CaseInsensitiveMap<Object, String> map = new CaseInsensitiveMap<>(Collections.emptyMap(), new MultiKeyMap<>(true));

        map.put("a", "alpha");
        map.put("b", "beta");
        map.put("c", "gamma");
        map.put(new String[]{"a", "b", "c"}, "[alpha, beta, gamma]");
        map.put(CollectionUtilities.listOf("a", "b", "c"), "collection: [alpha, beta, gamma]");

        assert map.size() == 4;  // Individual keys and array/collection keys are different when flattened
        assertEquals("alpha", map.get("A"));                    // different case
        assertEquals("beta", map.get("B"));                     // different case
        assertEquals("gamma", map.get("C"));                    // different case
        assertEquals("collection: [alpha, beta, gamma]", map.get(new String[]{"A", "B", "C"}));      // different case

        assert map.containsKey("A");
        assert map.containsKey("B");
        assert map.containsKey("C");
        assert map.containsKey(new String[]{"A", "B", "C"});
        assert map.containsKey(CollectionUtilities.listOf("A", "B", "C"));

        map.remove("A");
        assert map.size() == 3;
        map.remove("B");
        assert map.size() == 2;
        map.remove("C");
        assert map.size() == 1;
        map.remove(new String[]{"A", "B", "C"});
        assert map.isEmpty();
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/test/java/com/cedarsoftware/util/MultiKeyMapTest.java`
**Lines:** 254 to 284

```text
void testSingleElementArrayKeysNoFlattenInCaseInsensitiveMap3() {
        CaseInsensitiveMap<Object, String> map = new CaseInsensitiveMap<>(Collections.emptyMap(), new MultiKeyMap<>(false));

        map.put("a", "alpha");
        map.put("b", "beta");
        map.put("c", "gamma");
        map.put(new String[]{"a", "b", "c"}, "[alpha, beta, gamma]");
        map.put(CollectionUtilities.listOf("a", "b", "c"), "collection: [alpha, beta, gamma]");

        assert map.size() == 4;  // All keys are different when not flattened: "a", "b", "c", array, collection
        assertEquals("alpha", map.get("A"));                    // different case
        assertEquals("beta", map.get("B"));                     // different case
        assertEquals("gamma", map.get("C"));                    // different case
        assertEquals(null, map.get(new String[]{"A", "B", "C"}));  // Array key was overwritten by collection
        assertEquals("collection: [alpha, beta, gamma]", map.get(CollectionUtilities.listOf("A", "B", "C")));

        assert map.containsKey("A");
        assert map.containsKey("B");
        assert map.containsKey("C");
        assert map.containsKey(new String[]{"A", "B", "C"});
        assert map.containsKey(CollectionUtilities.listOf("A", "B", "C"));

        map.remove("A");
        assert map.size() == 3;
        map.remove("B");
        assert map.size() == 2;
        map.remove("C");
        assert map.size() == 1;
        map.remove(new String[]{"A", "B", "C"});
        assert map.isEmpty();
    }
```

