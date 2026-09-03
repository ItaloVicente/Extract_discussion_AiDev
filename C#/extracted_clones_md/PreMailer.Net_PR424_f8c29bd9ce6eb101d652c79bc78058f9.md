# 🔍 Clone Analysis | Project: PreMailer.Net | PR: #424

- **Commit SHA:** `bfeec2b10eef3af293db6b60233f30118164f26c`
- **Clone Fingerprint:** `f8c29bd9ce6eb101d652c79bc78058f9`
- **Categoria:** `unique_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `PreMailer.Net/PreMailer.Net.Tests/Issue410Tests.cs`
**Lines:** 9 to 23

```text
public void MoveCssInline_PreservesImportantInInlineStyles()
        {
            string input = @"<style> 
.test {
 color:red;
 }
 </style>
<body>
<p class=""test"" style=""font-weight: bold !important;"">test</p>
</body>";

            var result = PreMailer.MoveCssInline(input);

            Assert.Contains("font-weight: bold !important", result.Html);
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `PreMailer.Net/PreMailer.Net.Tests/PreMailerTests.cs`
**Lines:** 192 to 206

```text
public void MoveCssInline_ImportantFlag_PreservesImportantInInlineStylesForDifferentProperties()
		{
			string input = @"<style> 
.test {
 color:red;
 }
 </style>
<body>
<p class=""test"" style=""font-weight: bold !important;"">test</p>
</body>";

			var premailedOutput = PreMailer.MoveCssInline(input);

			Assert.Contains("font-weight: bold !important", premailedOutput.Html);
		}
```

