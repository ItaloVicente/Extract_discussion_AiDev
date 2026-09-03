# 🔍 Clone Analysis | Project: java-util | PR: #231

- **Commit SHA:** `50fbe2c45b2d0c4e376970441b9add08b9b88679`
- **Clone Fingerprint:** `3f0e0fc39afbf6abc11763000a436d18`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/test/java/com/cedarsoftware/util/MathUtilitiesTest.java`
**Lines:** 110 to 135

```text
void testMinimumBigInteger()
    {
        BigInteger minBi = MathUtilities.minimum(new BigInteger("-1"), new BigInteger("0"), new BigInteger("1"));
        assertEquals(new BigInteger("-1"), minBi);
        minBi = MathUtilities.minimum(new BigInteger("-121908747902834709812347908123432423"), new BigInteger("0"), new BigInteger("9780234508972317045230477890478903240978234"));
        assertEquals(new BigInteger("-121908747902834709812347908123432423"), minBi);

        BigInteger[] bigies = new BigInteger[] {new BigInteger("1"), new BigInteger("-1")};
        assertEquals(new BigInteger("-1"), MathUtilities.minimum(bigies));

        assertEquals(new BigInteger("500"), MathUtilities.minimum(new BigInteger("500")));

        try
        {
            MathUtilities.minimum((BigInteger)null);
            fail("Should not make it here");
        }
        catch (Exception ignored) { }

        try
        {
            MathUtilities.minimum(new BigInteger("1"), null, new BigInteger("3"));
            fail("Should not make it here");
        }
        catch (Exception ignored) { }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/test/java/com/cedarsoftware/util/MathUtilitiesTest.java`
**Lines:** 221 to 246

```text
void testMaximumBigInteger()
    {
        BigInteger minBi = MathUtilities.minimum(new BigInteger("-1"), new BigInteger("0"), new BigInteger("1"));
        assertEquals(new BigInteger("-1"), minBi);
        minBi = MathUtilities.minimum(new BigInteger("-121908747902834709812347908123432423"), new BigInteger("0"), new BigInteger("9780234508972317045230477890478903240978234"));
        assertEquals(new BigInteger("-121908747902834709812347908123432423"), minBi);

        BigInteger[] bigies = new BigInteger[] {new BigInteger("1"), new BigInteger("-1")};
        assertEquals(new BigInteger("1"), MathUtilities.maximum(bigies));

        assertEquals(new BigInteger("500"), MathUtilities.maximum(new BigInteger("500")));

        try
        {
            MathUtilities.maximum((BigInteger)null);
            fail("Should not make it here");
        }
        catch (Exception ignored) { }

        try
        {
            MathUtilities.minimum(new BigInteger("1"), null, new BigInteger("3"));
            fail("Should not make it here");
        }
        catch (Exception ignored) { }
    }
```

