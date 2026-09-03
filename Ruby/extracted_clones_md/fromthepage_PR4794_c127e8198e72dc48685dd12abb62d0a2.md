# 🔍 Clone Analysis | Project: fromthepage | PR: #4794

- **Commit SHA:** `277356721c601b722a5712024c76957c3bfcb000`
- **Clone Fingerprint:** `c127e8198e72dc48685dd12abb62d0a2`
- **Categoria:** `ini_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `app/controllers/transcription_field_controller.rb`
**Lines:** 261 to 269

```text
def authorized?
    unless user_signed_in?
      ajax_redirect_to dashboard_path
    end

    if @collection &&  !current_user.like_owner?(@collection)
      ajax_redirect_to dashboard_path
    end
  end
```

---

## 🧑‍💻 Clone Par 2
**File:** `app/controllers/collection_controller.rb`
**Lines:** 741 to 750

```text
def authorized?
    unless user_signed_in?
      ajax_redirect_to dashboard_path
      return
    end

    if @collection && !current_user.like_owner?(@collection)
      ajax_redirect_to dashboard_path
    end
  end
```

