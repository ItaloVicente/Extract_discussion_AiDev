# 🔍 Clone Analysis | Project: perfview | PR: #2222

- **Commit SHA:** `d06e2c0c06ecc6034d4515fdb9c8e375dffd8535`
- **Clone Fingerprint:** `6fbedbf5825ca7dbc62d12fe18acb6b0`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `src/TraceEvent/TraceEventSession.cs`
**Lines:** 2634 to 2646

```text
private static unsafe void CopyStringToPtr(char* toPtr, string str)
        {
            fixed (char* fromPtr = str)
            {
                int i = 0;
                while (i < str.Length)
                {
                    toPtr[i] = fromPtr[i];
                    i++;
                }
                toPtr[i] = '\0';   // Null terminate
            }
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/TraceEvent/ETWKernelControl.cs`
**Lines:** 314 to 326

```text
private unsafe static void CopyStringToPtr(char* toPtr, string str)
        {
            fixed (char* fromPtr = str)
            {
                int i = 0;
                while (i < str.Length)
                {
                    toPtr[i] = fromPtr[i];
                    i++;
                }
                toPtr[i] = '\0';   // Null terminate.
            }
        }
```

