# 🔍 Clone Analysis | Project: perfview | PR: #2269

- **Commit SHA:** `9004c22d7034529a3b8ebe04838bd00c91d1cccd`
- **Clone Fingerprint:** `104b94fab99d93be4ba951b4d0ca23e0`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `src/TraceEvent/TraceLog.cs`
**Lines:** 11268 to 11276

```text
public static CodeAddressIndex IntructionPointerCodeAddressIndex(this SampledProfileTraceData anEvent)
        {
            TraceLog log = anEvent.Source as TraceLog;
            if (null == log)
            {
                throw new InvalidOperationException("Attempted to use TraceLog support on a non-TraceLog TraceEventSource.");
            }
            return log.GetCodeAddressIndexAtEvent(anEvent.InstructionPointer, anEvent);
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/TraceEvent/TraceLog.cs`
**Lines:** 11307 to 11315

```text
public static CodeAddressIndex IntructionPointerCodeAddressIndex(this PMCCounterProfTraceData anEvent)
        {
            TraceLog log = anEvent.Source as TraceLog;
            if (null == log)
            {
                throw new InvalidOperationException("Attempted to use TraceLog support on a non-TraceLog TraceEventSource.");
            }
            return log.GetCodeAddressIndexAtEvent(anEvent.InstructionPointer, anEvent);
        }
```

