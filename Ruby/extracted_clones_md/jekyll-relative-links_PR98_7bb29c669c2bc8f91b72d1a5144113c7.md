# 🔍 Clone Analysis | Project: jekyll-relative-links | PR: #98

- **Commit SHA:** `33917fe6612e9406b9aafc2687f0fae2a76b308c`
- **Clone Fingerprint:** `7bb29c669c2bc8f91b72d1a5144113c7`
- **Categoria:** `unique_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `lib/jekyll-relative-links/filter.rb`
**Lines:** 40 to 47

```text
def path_from_root(relative_path, url_base)
      is_absolute = relative_path.start_with? "/"

      relative_path.delete_prefix!("/")
      base = is_absolute ? "" : url_base
      absolute_path = File.expand_path(relative_path, base)
      absolute_path.sub(%r!\A#{Regexp.escape(Dir.pwd)}/!, "")
    end
```

---

## 🧑‍💻 Clone Par 2
**File:** `lib/jekyll-relative-links/generator.rb`
**Lines:** 106 to 113

```text
def path_from_root(relative_path, url_base)
      is_absolute = relative_path.start_with? "/"

      relative_path.sub!(%r!\A/!, "")
      base = is_absolute ? "" : url_base
      absolute_path = File.expand_path(relative_path, base)
      absolute_path.sub(%r!\A#{Regexp.escape(Dir.pwd)}/!, "")
    end
```

