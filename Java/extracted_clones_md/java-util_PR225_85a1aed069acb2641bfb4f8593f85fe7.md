# 🔍 Clone Analysis | Project: java-util | PR: #225

- **Commit SHA:** `8a67cae18f473dbf1e30121860a0f760903502e4`
- **Clone Fingerprint:** `85a1aed069acb2641bfb4f8593f85fe7`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/test/java/com/cedarsoftware/util/ConverterLegacyApiTest.java`
**Lines:** 56 to 67

```text
void convert2_goodData(ConversionFunction func, Object input, Object expected) {
        Object result = func.apply(input);
        if (expected instanceof AtomicBoolean) {
            assertThat(((AtomicBoolean) result).get()).isEqualTo(((AtomicBoolean) expected).get());
        } else if (expected instanceof AtomicInteger) {
            assertThat(((AtomicInteger) result).get()).isEqualTo(((AtomicInteger) expected).get());
        } else if (expected instanceof AtomicLong) {
            assertThat(((AtomicLong) result).get()).isEqualTo(((AtomicLong) expected).get());
        } else {
            assertThat(result).isEqualTo(expected);
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/test/java/com/cedarsoftware/util/ConverterLegacyApiTest.java`
**Lines:** 162 to 175

```text
void convertTo_goodData(ConversionFunction func, Object input, Object expected) {
        Object result = func.apply(input);
        if (expected instanceof AtomicBoolean) {
            assertThat(((AtomicBoolean) result).get()).isEqualTo(((AtomicBoolean) expected).get());
        } else if (expected instanceof AtomicInteger) {
            assertThat(((AtomicInteger) result).get()).isEqualTo(((AtomicInteger) expected).get());
        } else if (expected instanceof AtomicLong) {
            assertThat(((AtomicLong) result).get()).isEqualTo(((AtomicLong) expected).get());
        } else if (result instanceof Calendar) {
            assertThat(((Calendar) result).getTime()).isEqualTo(((Calendar) expected).getTime());
        } else {
            assertThat(result).isEqualTo(expected);
        }
    }
```

