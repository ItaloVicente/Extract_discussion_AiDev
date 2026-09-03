# 🔍 Clone Analysis | Project: azure-functions-host | PR: #11115

- **Commit SHA:** `d21cfebdaa8432ee18b7b340b215a2e24a4fef8a`
- **Clone Fingerprint:** `85e667737dd9c747a9b05be458dfd682`
- **Categoria:** `mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `test/WebJobs.Script.Tests/ManagedDependencies/ManagedDependencyOptionsSetupTest.cs`
**Lines:** 98 to 110

```text
private IConfiguration BuildHostJsonConfiguration(IEnvironment environment = null)
        {
            environment = environment ?? new TestEnvironment();
            var loggerFactory = new LoggerFactory();
            loggerFactory.AddProvider(_loggerProvider);

            var configSource = new HostJsonFileConfigurationSource(_options, environment, loggerFactory, new TestMetricsLogger());

            var configurationBuilder = new ConfigurationBuilder()
                .Add(configSource);

            return configurationBuilder.Build();
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `test/WebJobs.Script.Tests/Configuration/HostJsonFileConfigurationSourceTests.cs`
**Lines:** 268 to 280

```text
private IConfiguration BuildHostJsonConfiguration(TestMetricsLogger testMetricsLogger, IEnvironment environment = null)
        {
            environment = environment ?? new TestEnvironment();
            var loggerFactory = new LoggerFactory();
            loggerFactory.AddProvider(_loggerProvider);

            var configSource = new HostJsonFileConfigurationSource(_options, environment, loggerFactory, testMetricsLogger);

            var configurationBuilder = new ConfigurationBuilder()
                .Add(configSource);

            return configurationBuilder.Build();
        }
```

