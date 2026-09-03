# 🔍 Clone Analysis | Project: jekyll-remote-theme | PR: #106

- **Commit SHA:** `31e6814cbdf00d9e2fdb86baf43bf02cfd9c9b89`
- **Clone Fingerprint:** `3cb5e4ded40bc942678b991dca4c178d`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `vendor/bundle/ruby/3.2.0/gems/liquid-4.0.4/lib/liquid/standardfilters.rb`
**Lines:** 134 to 150

```text
def sort(input, property = nil)
      ary = InputIterator.new(input)

      return [] if ary.empty?

      if property.nil?
        ary.sort do |a, b|
          nil_safe_compare(a, b)
        end
      elsif ary.all? { |el| el.respond_to?(:[]) }
        begin
          ary.sort { |a, b| nil_safe_compare(a[property], b[property]) }
        rescue TypeError
          raise_property_error(property)
        end
      end
    end
```

---

## 🧑‍💻 Clone Par 2
**File:** `vendor/bundle/ruby/3.2.0/gems/liquid-4.0.4/lib/liquid/standardfilters.rb`
**Lines:** 154 to 170

```text
def sort_natural(input, property = nil)
      ary = InputIterator.new(input)

      return [] if ary.empty?

      if property.nil?
        ary.sort do |a, b|
          nil_safe_casecmp(a, b)
        end
      elsif ary.all? { |el| el.respond_to?(:[]) }
        begin
          ary.sort { |a, b| nil_safe_casecmp(a[property], b[property]) }
        rescue TypeError
          raise_property_error(property)
        end
      end
    end
```

