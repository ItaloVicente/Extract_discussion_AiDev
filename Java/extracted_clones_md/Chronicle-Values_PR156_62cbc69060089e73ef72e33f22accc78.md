# 🔍 Clone Analysis | Project: Chronicle-Values | PR: #156

- **Commit SHA:** `2bcd77c4cebd77f4622211d321cf48ca1fbd4882`
- **Clone Fingerprint:** `62cbc69060089e73ef72e33f22accc78`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/main/java/net/openhft/chronicle/values/IntegerFieldModel.java`
**Lines:** 399 to 414

```text
String genArrayElementGet(
            ArrayFieldModel arrayFieldModel, ValueBuilder valueBuilder,
            MethodSpec.Builder methodBuilder, Function<String, String> accessType) {
        int arrayBitOffset = valueBuilder.model.fieldBitOffset(arrayFieldModel);
        if (arrayBitOffset % 8 != 0)
            throw new UnsupportedOperationException("not implemented yet");
        int arrayByteOffset = arrayBitOffset / 8;
        int elemBitExtent = arrayFieldModel.elemBitExtent();
        if (elemBitExtent % 8 == 0) {
            genVerifiedElementOffset(arrayFieldModel, methodBuilder);
            String readOffset = format("offset + %d + elementOffset", arrayByteOffset);
            return genGet(0, elemBitExtent, readOffset, accessType);
        } else {
            throw new UnsupportedOperationException("not implemented yet");
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/main/java/net/openhft/chronicle/values/IntegerFieldModel.java`
**Lines:** 502 to 518

```text
void genArrayElementSet(
            ArrayFieldModel arrayFieldModel, ValueBuilder valueBuilder,
            MethodSpec.Builder methodBuilder, Function<String, String> accessType,
            String valueToWrite) {
        int arrayBitOffset = valueBuilder.model.fieldBitOffset(arrayFieldModel);
        if (arrayBitOffset % 8 != 0)
            throw new UnsupportedOperationException("not implemented yet");
        int arrayByteOffset = arrayBitOffset / 8;
        int elemBitExtent = arrayFieldModel.elemBitExtent();
        if (elemBitExtent % 8 == 0) {
            genVerifiedElementOffset(arrayFieldModel, methodBuilder);
            String ioOffset = format("offset + %d + elementOffset", arrayByteOffset);
            genSet(methodBuilder, 0, elemBitExtent, ioOffset, accessType, valueToWrite);
        } else {
            throw new UnsupportedOperationException("not implemented yet");
        }
    }
```

