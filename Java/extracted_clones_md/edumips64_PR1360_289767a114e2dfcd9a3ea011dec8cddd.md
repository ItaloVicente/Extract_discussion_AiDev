# 🔍 Clone Analysis | Project: edumips64 | PR: #1360

- **Commit SHA:** `c720ea1fe4b8be6a9d2226262bb944b4be7c7b1c`
- **Clone Fingerprint:** `289767a114e2dfcd9a3ea011dec8cddd`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `src/main/java/org/edumips64/core/CacheSimulator.java`
**Lines:** 173 to 183

```text
public void Load(String address, int nByte) {
        try {
            long addr = Long.parseLong(Converter.hexToLong("0x" + address));
            addr += offset;
            String entry = "r " + Converter.binToHex(Converter.intToBin(64, addr)) + " " + nByte;
            dineroData.add(entry);
            processDineroTraceEntry(this.getL1DataCache(),entry);
        } catch (IrregularStringOfHexException | IrregularStringOfBitsException ex) {
            ex.printStackTrace();
        }
    }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/main/java/org/edumips64/core/CacheSimulator.java`
**Lines:** 185 to 196

```text
public void Store(String address, int nByte) {
        try {
            long addr = Long.parseLong(Converter.hexToLong("0x" + address));
            addr += offset;
            String entry = "w " + Converter.binToHex(Converter.intToBin(64, addr)) + " " + nByte;
            dineroData.add(entry);
            processDineroTraceEntry(this.getL1DataCache(),entry);
        } catch (IrregularStringOfHexException | IrregularStringOfBitsException ex) {
            ex.printStackTrace();
        }

    }
```

