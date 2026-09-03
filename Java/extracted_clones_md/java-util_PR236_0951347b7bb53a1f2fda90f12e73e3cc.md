# 🔍 Clone Analysis | Project: java-util | PR: #236

- **Commit SHA:** `3e281b41d416e258068533b18e5d406942dcdd26`
- **Clone Fingerprint:** `0951347b7bb53a1f2fda90f12e73e3cc`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/test/java/com/cedarsoftware/util/TestUtilTest.java`
**Lines:** 75 to 94

```text
public void testIsReleaseModeTrue()
    {
        String original = System.getProperty("performRelease");
        System.setProperty("performRelease", "true");
        try
        {
            assertTrue(TestUtil.isReleaseMode());
        }
        finally
        {
            if (original == null)
            {
                System.clearProperty("performRelease");
            }
            else
            {
                System.setProperty("performRelease", original);
            }
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/test/java/com/cedarsoftware/util/TestUtilTest.java`
**Lines:** 97 to 116

```text
public void testIsReleaseModeExplicitFalse()
    {
        String original = System.getProperty("performRelease");
        System.setProperty("performRelease", "false");
        try
        {
            assertFalse(TestUtil.isReleaseMode());
        }
        finally
        {
            if (original == null)
            {
                System.clearProperty("performRelease");
            }
            else
            {
                System.setProperty("performRelease", original);
            }
        }
    }
```

