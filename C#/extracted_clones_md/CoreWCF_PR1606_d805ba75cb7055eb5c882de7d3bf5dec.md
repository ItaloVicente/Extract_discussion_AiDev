# 🔍 Clone Analysis | Project: CoreWCF | PR: #1606

- **Commit SHA:** `636aade66de57e07648e7addf5dd8f447ff5c57a`
- **Clone Fingerprint:** `d805ba75cb7055eb5c882de7d3bf5dec`
- **Categoria:** `unique_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `src/CoreWCF.Http/tests/DependencyInjection/ServiceTypeErrorMessageTests.cs`
**Lines:** 83 to 95

```text
public void Configure(IApplicationBuilder app)
            {
                app.UseServiceModel(builder =>
                {
                    // This will fail because ServiceWithNoDefaultConstructor is not in DI and has no default constructor
                    // Using ServiceOptions to enable exception detail in faults so we can verify the error message
                    builder.AddService<ServiceWithNoDefaultConstructor>(options =>
                    {
                        options.DebugBehavior.IncludeExceptionDetailInFaults = true;
                    });
                    builder.AddServiceEndpoint<ServiceWithNoDefaultConstructor, ITestService>(new BasicHttpBinding(), "/testservice");
                });
            }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/CoreWCF.Http/tests/DependencyInjection/ServiceTypeErrorMessageTests.cs`
**Lines:** 114 to 126

```text
public void Configure(IApplicationBuilder app)
            {
                app.UseServiceModel(builder =>
                {
                    // This will fail because SingletonServiceWithNoDefaultConstructor is not in DI and has no default constructor
                    // Using ServiceOptions to enable exception detail in faults so we can verify the error message
                    builder.AddService<SingletonServiceWithNoDefaultConstructor>(options =>
                    {
                        options.DebugBehavior.IncludeExceptionDetailInFaults = true;
                    });
                    builder.AddServiceEndpoint<SingletonServiceWithNoDefaultConstructor, ITestService>(new BasicHttpBinding(), "/testservice");
                });
            }
```

