# 🔍 Clone Analysis | Project: activestorage-validator | PR: #39

- **Commit SHA:** `82486474fffa1ad8b168c005c0233376785f033e`
- **Clone Fingerprint:** `3e10f0d0e8485b8d6304459bd36cac2f`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `vendor/bundle/ruby/3.2.0/gems/rdoc-6.14.0/lib/rdoc/markdown.rb`
**Lines:** 2873 to 2926

```text
def _HtmlOpenAnchor

    _save = self.pos
    while true # sequence
      _tmp = match_string("<")
      unless _tmp
        self.pos = _save
        break
      end
      _tmp = apply(:_Spnl)
      unless _tmp
        self.pos = _save
        break
      end

      _save1 = self.pos
      while true # choice
        _tmp = match_string("a")
        break if _tmp
        self.pos = _save1
        _tmp = match_string("A")
        break if _tmp
        self.pos = _save1
        break
      end # end choice

      unless _tmp
        self.pos = _save
        break
      end
      _tmp = apply(:_Spnl)
      unless _tmp
        self.pos = _save
        break
      end
      while true
        _tmp = apply(:_HtmlAttribute)
        break unless _tmp
      end
      _tmp = true
      unless _tmp
        self.pos = _save
        break
      end
      _tmp = match_string(">")
      unless _tmp
        self.pos = _save
      end
      break
    end # end sequence

    set_failed_rule :_HtmlOpenAnchor unless _tmp
    return _tmp
  end
```

---

## 🧑‍💻 Clone Par 2
**File:** `vendor/bundle/ruby/3.2.0/gems/rdoc-6.14.0/lib/rdoc/markdown.rb`
**Lines:** 6249 to 6298

```text
def _HtmlBlockClosePre

    _save = self.pos
    while true # sequence
      _tmp = match_string("<")
      unless _tmp
        self.pos = _save
        break
      end
      _tmp = apply(:_Spnl)
      unless _tmp
        self.pos = _save
        break
      end
      _tmp = match_string("/")
      unless _tmp
        self.pos = _save
        break
      end

      _save1 = self.pos
      while true # choice
        _tmp = match_string("pre")
        break if _tmp
        self.pos = _save1
        _tmp = match_string("PRE")
        break if _tmp
        self.pos = _save1
        break
      end # end choice

      unless _tmp
        self.pos = _save
        break
      end
      _tmp = apply(:_Spnl)
      unless _tmp
        self.pos = _save
        break
      end
      _tmp = match_string(">")
      unless _tmp
        self.pos = _save
      end
      break
    end # end sequence

    set_failed_rule :_HtmlBlockClosePre unless _tmp
    return _tmp
  end
```

