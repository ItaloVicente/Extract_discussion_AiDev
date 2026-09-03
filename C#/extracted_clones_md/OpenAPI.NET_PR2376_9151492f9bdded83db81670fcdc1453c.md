# 🔍 Clone Analysis | Project: OpenAPI.NET | PR: #2376

- **Commit SHA:** `73ec5a7489040c8fb68ea8bf69f68c3da7f61fe6`
- **Clone Fingerprint:** `9151492f9bdded83db81670fcdc1453c`
- **Categoria:** `unique_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `test/Microsoft.OpenApi.Tests/Models/References/OpenApiSchemaReferenceTests.cs`
**Lines:** 127 to 151

```text
public async Task SerializeSchemaReferenceAsV31JsonWorks(bool produceTerseOutput)
        {
            // Arrange
            var reference = new OpenApiSchemaReference("Pet", null)
            {
                Title = "Reference Title",
                Description = "Reference Description",
                Summary = "Reference Summary",
                ReadOnly = true,
                WriteOnly = false,
                Deprecated = true,
                Default = JsonValue.Create("reference default"),
                Examples = new List<JsonNode> { JsonValue.Create("reference example") }
            };

            var outputStringWriter = new StringWriter(CultureInfo.InvariantCulture);
            var writer = new OpenApiJsonWriter(outputStringWriter, new OpenApiJsonWriterSettings { Terse = produceTerseOutput });

            // Act
            reference.SerializeAsV31(writer);
            await writer.FlushAsync();

            // Assert
            await Verifier.Verify(outputStringWriter).UseParameters(produceTerseOutput);
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `test/Microsoft.OpenApi.Tests/Models/References/OpenApiSchemaReferenceTests.cs`
**Lines:** 156 to 180

```text
public async Task SerializeSchemaReferenceAsV3JsonWorks(bool produceTerseOutput)
        {
            // Arrange
            var reference = new OpenApiSchemaReference("Pet", null)
            {
                Title = "Reference Title",
                Description = "Reference Description",
                Summary = "Reference Summary",
                ReadOnly = true,
                WriteOnly = false,
                Deprecated = true,
                Default = JsonValue.Create("reference default"),
                Examples = new List<JsonNode> { JsonValue.Create("reference example") }
            };

            var outputStringWriter = new StringWriter(CultureInfo.InvariantCulture);
            var writer = new OpenApiJsonWriter(outputStringWriter, new OpenApiJsonWriterSettings { Terse = produceTerseOutput });

            // Act
            reference.SerializeAsV3(writer);
            await writer.FlushAsync();

            // Assert
            await Verifier.Verify(outputStringWriter).UseParameters(produceTerseOutput);
        }
```

