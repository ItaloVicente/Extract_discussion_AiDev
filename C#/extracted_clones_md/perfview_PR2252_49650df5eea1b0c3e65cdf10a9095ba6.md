# 🔍 Clone Analysis | Project: perfview | PR: #2252

- **Commit SHA:** `af3bc1d7d293f785b69a667cbd77f0731f69b801`
- **Clone Fingerprint:** `49650df5eea1b0c3e65cdf10a9095ba6`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `src/TraceEvent/TraceLog.cs`
**Lines:** 7812 to 7821

```text
private unsafe CallStackIndex GetStackIndexForStackEvent32(uint* addresses, int addressCount, TraceProcess process, CallStackIndex start)
        {
            for (var it = &addresses[addressCount]; it-- != addresses;)
            {
                CodeAddressIndex codeAddress = codeAddresses.GetOrCreateCodeAddressIndex(process, *it);
                start = InternCallStackIndex(codeAddress, start);
            }

            return start;
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/TraceEvent/TraceLog.cs`
**Lines:** 7823 to 7832

```text
private unsafe CallStackIndex GetStackIndexForStackEvent64(ulong* addresses, int addressCount, TraceProcess process, CallStackIndex start)
        {
            for (var it = &addresses[addressCount]; it-- != addresses;)
            {
                CodeAddressIndex codeAddress = codeAddresses.GetOrCreateCodeAddressIndex(process, *it);
                start = InternCallStackIndex(codeAddress, start);
            }

            return start;
        }
```

