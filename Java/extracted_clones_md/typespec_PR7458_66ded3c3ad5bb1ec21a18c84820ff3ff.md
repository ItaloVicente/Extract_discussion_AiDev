# 🔍 Clone Analysis | Project: typespec | PR: #7458

- **Commit SHA:** `42adf21f00b936ed8100b6f165b1bafe7471b60c`
- **Clone Fingerprint:** `66ded3c3ad5bb1ec21a18c84820ff3ff`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `packages/http-client-java/generator/http-client-generator-test/src/main/java/azure/resourcemanager/operationtemplates/OperationTemplatesManager.java`
**Lines:** 195 to 203

```text
public Configurable withDefaultPollInterval(Duration defaultPollInterval) {
            this.defaultPollInterval
                = Objects.requireNonNull(defaultPollInterval, "'defaultPollInterval' cannot be null.");
            if (this.defaultPollInterval.isNegative()) {
                throw LOGGER
                    .logExceptionAsError(new IllegalArgumentException("'defaultPollInterval' cannot be negative"));
            }
            return this;
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `packages/http-client-java/generator/http-client-generator-test/src/main/java/azure/resourcemanager/resources/ResourcesManager.java`
**Lines:** 203 to 211

```text
public Configurable withDefaultPollInterval(Duration defaultPollInterval) {
            this.defaultPollInterval
                = Objects.requireNonNull(defaultPollInterval, "'defaultPollInterval' cannot be null.");
            if (this.defaultPollInterval.isNegative()) {
                throw LOGGER
                    .logExceptionAsError(new IllegalArgumentException("'defaultPollInterval' cannot be negative"));
            }
            return this;
        }
```

