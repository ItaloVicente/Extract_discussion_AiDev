# 🔍 Clone Analysis | Project: java-util | PR: #294

- **Commit SHA:** `9c7b3fc9b27ccd084d4e59ba797448095b2fbd8c`
- **Clone Fingerprint:** `85a88d6cebdeec3bc1ba2c01fb4b242f`
- **Categoria:** `unique_final`

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

