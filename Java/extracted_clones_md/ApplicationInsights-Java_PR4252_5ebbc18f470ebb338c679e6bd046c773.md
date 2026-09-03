# 🔍 Clone Analysis | Project: ApplicationInsights-Java | PR: #4252

- **Commit SHA:** `5bddd893cb369ff9d6f5c1106c48eca2312e967d`
- **Clone Fingerprint:** `5ebbc18f470ebb338c679e6bd046c773`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `smoke-tests/framework/src/main/java/com/microsoft/applicationinsights/smoketest/SmokeTestExtension.java`
**Lines:** 687 to 699

```text
public static Predicate<Envelope> getMetricPredicate(String name) {
    Objects.requireNonNull(name, "name");
    return input -> {
      if (input == null) {
        return false;
      }
      if (!input.getData().getBaseType().equals("MetricData")) {
        return false;
      }
      MetricData md = getBaseData(input);
      return name.equals(md.getMetrics().get(0).getName());
    };
  }
```

---

## 🧑‍💻 Clone Par 2
**File:** `smoke-tests/framework/src/main/java/com/microsoft/applicationinsights/smoketest/SmokeTestExtension.java`
**Lines:** 724 to 736

```text
public static Predicate<Envelope> getStandardMetricPredicate(String metricId) {
    Objects.requireNonNull(metricId, "metricId");
    return input -> {
      if (input == null) {
        return false;
      }
      if (!input.getData().getBaseType().equals("MetricData")) {
        return false;
      }
      MetricData md = getBaseData(input);
      return metricId.equals(md.getProperties().get("_MS.MetricId"));
    };
  }
```

