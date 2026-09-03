# 🔍 Clone Analysis | Project: maybe | PR: #2389

- **Commit SHA:** `4ba560c177917c7536bbf9771cdd590170b7fbf7`
- **Clone Fingerprint:** `dda2536ed7ef4c90f68cdbf2d143f7ca`
- **Categoria:** `mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `app/models/user.rb`
**Lines:** 123 to 129

```text
def setup_mfa!
    update!(
      otp_secret: ROTP::Base32.random(32),
      otp_required: false,
      otp_backup_codes: []
    )
  end
```

---

## 🧑‍💻 Clone Par 2
**File:** `app/models/user.rb`
**Lines:** 138 to 144

```text
def disable_mfa!
    update!(
      otp_secret: nil,
      otp_required: false,
      otp_backup_codes: []
    )
  end
```

