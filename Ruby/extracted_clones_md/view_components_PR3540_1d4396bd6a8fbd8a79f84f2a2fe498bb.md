# 🔍 Clone Analysis | Project: view_components | PR: #3540

- **Commit SHA:** `3e911e1d65a05d99aaceadc3a38c21d4ce1ecd04`
- **Clone Fingerprint:** `1d4396bd6a8fbd8a79f84f2a2fe498bb`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `test/components/breadcrumbs_test.rb`
**Lines:** 62 to 69

```text
def test_automatically_selects_last_item
    render_inline(Primer::Beta::Breadcrumbs.new) do |component|
      component.with_item(href: "/") { "Home" }
      component.with_item(href: "/about") { "About" }
    end

    assert_selector("li.breadcrumb-item-selected a[aria-current='page']", text: "About")
  end
```

---

## 🧑‍💻 Clone Par 2
**File:** `test/components/breadcrumbs_test.rb`
**Lines:** 85 to 92

```text
def test_breadcrumb_items_have_correct_css_class
    render_inline(Primer::Beta::Breadcrumbs.new) do |component|
      component.with_item(href: "/") { "Home" }
      component.with_item(href: "/about") { "About" }
    end

    assert_selector(".breadcrumb-item", count: 2)
  end
```

