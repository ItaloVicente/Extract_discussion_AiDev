# 🔍 Clone Analysis | Project: java-util | PR: #185

- **Commit SHA:** `1a0eda8832167c414d6270fea3b6df2ebc2228a9`
- **Clone Fingerprint:** `85a88d6cebdeec3bc1ba2c01fb4b242f`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/test/java/com/cedarsoftware/util/EncryptionTest.java`
**Lines:** 44 to 50

```text
public void testConstructorIsPrivate() throws Exception {
        Constructor<EncryptionUtilities> con = EncryptionUtilities.class.getDeclaredConstructor();
        assertEquals(Modifier.PRIVATE, con.getModifiers() & Modifier.PRIVATE);
        con.setAccessible(true);

        assertNotNull(con.newInstance());
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/test/java/com/cedarsoftware/util/ReflectionUtilsTest.java`
**Lines:** 104 to 110

```text
public void testConstructorIsPrivate() throws Exception {
        Constructor<ReflectionUtils> con = ReflectionUtils.class.getDeclaredConstructor();
        assertEquals(Modifier.PRIVATE, con.getModifiers() & Modifier.PRIVATE);
        con.setAccessible(true);

        assertNotNull(con.newInstance());
    }
```

