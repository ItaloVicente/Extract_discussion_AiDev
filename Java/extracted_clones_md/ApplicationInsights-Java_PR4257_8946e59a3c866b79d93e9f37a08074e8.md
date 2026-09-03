# 🔍 Clone Analysis | Project: ApplicationInsights-Java | PR: #4257

- **Commit SHA:** `428c167333c19665baeff8bbd1703475ac725cd8`
- **Clone Fingerprint:** `8946e59a3c866b79d93e9f37a08074e8`
- **Categoria:** `unique_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `classic-sdk/core/src/main/java/com/microsoft/applicationinsights/telemetry/ExceptionTelemetry.java`
**Lines:** 100 to 115

```text
private static SeverityLevel mapFromInternalSeverityLevel(com.microsoft.applicationinsights.internal.schemav2.SeverityLevel internalSeverityLevel) {
    switch (internalSeverityLevel) {
      case Verbose:
        return SeverityLevel.Verbose;
      case Information:
        return SeverityLevel.Information;
      case Warning:
        return SeverityLevel.Warning;
      case Error:
        return SeverityLevel.Error;
      case Critical:
        return SeverityLevel.Critical;
      default:
        throw new IllegalArgumentException("Unknown internal SeverityLevel: " + internalSeverityLevel);
    }
  }
```

---

## 🧑‍💻 Clone Par 2
**File:** `classic-sdk/core/src/main/java/com/microsoft/applicationinsights/telemetry/TraceTelemetry.java`
**Lines:** 86 to 101

```text
private static SeverityLevel mapFromInternalSeverityLevel(com.microsoft.applicationinsights.internal.schemav2.SeverityLevel internalSeverityLevel) {
    switch (internalSeverityLevel) {
      case Verbose:
        return SeverityLevel.Verbose;
      case Information:
        return SeverityLevel.Information;
      case Warning:
        return SeverityLevel.Warning;
      case Error:
        return SeverityLevel.Error;
      case Critical:
        return SeverityLevel.Critical;
      default:
        throw new IllegalArgumentException("Unknown internal SeverityLevel: " + internalSeverityLevel);
    }
  }
```

