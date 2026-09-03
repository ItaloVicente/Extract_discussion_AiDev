# 🔍 Clone Analysis | Project: azure-devops-migration-tools | PR: #2868

- **Commit SHA:** `b6f3da9f456a79b1a61f4982653eeb0425c4d08c`
- **Clone Fingerprint:** `d3a9fe07c8c02a1ff499b6737e0a513f`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/MigrationTools.Clients.FileSystem.Tests/Endpoints/FileSystemWorkItemEndpointTests.cs`
**Lines:** 67 to 79

```text
public void PersistWorkItemExistsTest()
        {
            FileSystemWorkItemEndpoint e1 = (FileSystemWorkItemEndpoint)Services.GetKeyedService<IEndpoint>("Source");
            CleanAndAdd(e1, 20);
            FileSystemWorkItemEndpoint e2 = (FileSystemWorkItemEndpoint)Services.GetKeyedService<IEndpoint>("Target");
            CleanAndAdd(e2, 10);

            foreach (WorkItemData item in e1.GetWorkItems())
            {
                e2.PersistWorkItem(item);
            }
            Assert.AreEqual(20, e2.Count);
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/MigrationTools.Clients.FileSystem.Tests/Endpoints/FileSystemWorkItemEndpointTests.cs`
**Lines:** 82 to 95

```text
public void PersistWorkItemWithFilterTest()
        {
            FileSystemWorkItemEndpoint e1 = (FileSystemWorkItemEndpoint)Services.GetKeyedService<IEndpoint>("Source");
            CleanAndAdd(e1, 20);
            FileSystemWorkItemEndpoint e2 = (FileSystemWorkItemEndpoint)Services.GetKeyedService<IEndpoint>("Target");
            CleanAndAdd(e2, 10);
            e1.Filter(e2.GetWorkItems());
            Assert.AreEqual(10, e1.Count);
            foreach (WorkItemData item in e1.GetWorkItems())
            {
                e2.PersistWorkItem(item);
            }
            Assert.AreEqual(20, e2.Count);
        }
```

