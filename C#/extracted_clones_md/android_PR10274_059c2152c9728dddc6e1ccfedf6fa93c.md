# 🔍 Clone Analysis | Project: android | PR: #10274

- **Commit SHA:** `870d735acf87a3b9f37955ed6e613e6e858623bd`
- **Clone Fingerprint:** `059c2152c9728dddc6e1ccfedf6fa93c`
- **Categoria:** `ini_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `src/Xamarin.Android.Build.Tasks/Utilities/TypeMappingReleaseNativeAssemblyGeneratorCLR.cs`
**Lines:** 32 to 45

```text
public override ulong GetBufferSize (object data, string fieldName)
			{
				var map_module = EnsureType<TypeMapModule> (data);

				if (MonoAndroidHelper.StringEquals ("map", fieldName, StringComparison.Ordinal)) {
					return map_module.entry_count;
				}

				if (MonoAndroidHelper.StringEquals ("duplicate_map", fieldName, StringComparison.Ordinal)) {
					return map_module.duplicate_count;
				}

				return base.GetBufferSize (data, fieldName);
			}
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/Xamarin.Android.Build.Tasks/Utilities/TypeMappingReleaseNativeAssemblyGenerator.cs`
**Lines:** 47 to 60

```text
public override ulong GetBufferSize (object data, string fieldName)
			{
				var map_module = EnsureType<TypeMapModule> (data);

				if (MonoAndroidHelper.StringEquals ("map", fieldName, StringComparison.Ordinal)) {
					return map_module.entry_count;
				}

				if (MonoAndroidHelper.StringEquals ("duplicate_map", fieldName, StringComparison.Ordinal)) {
					return map_module.duplicate_count;
				}

				return base.GetBufferSize (data, fieldName);
			}
```

