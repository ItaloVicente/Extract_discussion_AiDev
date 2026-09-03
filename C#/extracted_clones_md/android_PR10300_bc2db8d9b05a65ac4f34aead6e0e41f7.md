# 🔍 Clone Analysis | Project: android | PR: #10300

- **Commit SHA:** `56bc425b58bc5c4222fff8f9b8f7a8071bf25d84`
- **Clone Fingerprint:** `bc2db8d9b05a65ac4f34aead6e0e41f7`
- **Categoria:** `unique_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `src/Xamarin.Android.Build.Tasks/Tasks/GenerateLayoutBindings.BindingGenerator.cs`
**Lines:** 294 to 303

```text
public void WriteComment (State state, ICollection<string> lines)
			{
				if (lines == null)
					return;

				EnsureArgument (state, nameof (state));
				foreach (string line in lines) {
					WriteComment (state, line);
				}
			}
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/Xamarin.Android.Build.Tasks/Tasks/GenerateLayoutBindings.BindingGenerator.cs`
**Lines:** 311 to 320

```text
public void WriteDocComment (State state, ICollection<string> lines)
			{
				if (lines == null)
					return;

				EnsureArgument (state, nameof (state));
				foreach (string line in lines) {
					WriteComment (state, line);
				}
			}
```

