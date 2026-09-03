# 🔍 Clone Analysis | Project: azure-functions-core-tools | PR: #4480

- **Commit SHA:** `bd7e1b694cb4707ace63cb846dce47dfe78644c1`
- **Clone Fingerprint:** `320dc4176fd2f2ed7096104ff6f43c4b`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `test/Azure.Functions.Cli.Tests/ActionsTests/ResolveActionTests.cs`
**Lines:** 84 to 94

```text
public void ThrowErrorOnIncorrectCommandLine(string args)
        {
            var fileSystem = Substitute.For<IFileSystem>();
            fileSystem.File.Exists(Arg.Any<string>()).Returns(true);
            FileSystemHelpers.Instance = fileSystem;

            var container = InitializeContainerForTests();
            var app = new ConsoleApp(args.Split(' ').ToArray(), typeof(Program).Assembly, container);

            Assert.Throws<CliArgumentsException>(app.Parse);
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `test/Cli/Func.Unit.Tests/ActionsTests/ResolveActionTests.cs`
**Lines:** 84 to 94

```text
public void ThrowErrorOnIncorrectCommandLine(string args)
        {
            var fileSystem = Substitute.For<IFileSystem>();
            fileSystem.File.Exists(Arg.Any<string>()).Returns(true);
            FileSystemHelpers.Instance = fileSystem;

            var container = InitializeContainerForTests();
            var app = new ConsoleApp(args.Split(' ').ToArray(), typeof(Program).Assembly, container);

            Assert.Throws<CliArgumentsException>(app.Parse);
        }
```

