# 🔍 Clone Analysis | Project: data-api-builder | PR: #2727

- **Commit SHA:** `dacc617a743cd791561e35a9827d9510966681f9`
- **Clone Fingerprint:** `0418724abdc2da7f1446a391b2f79f57`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `src/Service.Tests/SqlTests/GraphQLMutationTests/DwSqlGraphQLMutationTests.cs`
**Lines:** 85 to 104

```text
public override async Task InsertMutationWithOnlyTypenameInSelectionSet()
        {
            string graphQLMutationName = "createbook";
            string graphQLMutation = @"
                mutation {
                    createbook(item: { id: 1, title: ""Awesome Book"", publisher_id: 1234 }) {
                        __typename
                    }
                }
            ";

            JsonElement actual = await ExecuteGraphQLRequestAsync(graphQLMutation, graphQLMutationName, isAuthenticated: true);
            string expected = @"
              {
                ""__typename"": ""DbOperationResult""
              }
            ";

            SqlTestHelper.PerformTestEqualJsonStrings(expected, actual.ToString());
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/Service.Tests/SqlTests/GraphQLMutationTests/GraphQLMutationTestBase.cs`
**Lines:** 520 to 539

```text
public virtual async Task InsertMutationWithOnlyTypenameInSelectionSet()
        {
            string graphQLMutationName = "createbook";
            string graphQLMutation = @"
                mutation {
                    createbook(item: { title: ""Awesome Book"", publisher_id: 1234 }) {
                        __typename
                    }
                }
            ";

            JsonElement actual = await ExecuteGraphQLRequestAsync(graphQLMutation, graphQLMutationName, isAuthenticated: true);
            string expected = @"
              {
                ""__typename"": ""book""
              }
            ";

            SqlTestHelper.PerformTestEqualJsonStrings(expected, actual.ToString());
        }
```

