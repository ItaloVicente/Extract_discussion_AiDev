# 🔍 Clone Analysis | Project: DDNS | PR: #499

- **Commit SHA:** `f9346188893f290dbb57d0946bd7f3752b8f9958`
- **Clone Fingerprint:** `7fcb9fbd99302def8272db7f613de81a`
- **Categoria:** `unique_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `tests/test_config_ssl.py`
**Lines:** 67 to 75

```text
def test_env_ssl_false(self):
        """Test SSL configuration via environment variable DDNS_SSL=false"""
        env_vars = {'DDNS_SSL': 'false', 'DDNS_TOKEN': 'test'}
        with patch.dict(os.environ, env_vars):
            with patch.object(sys, 'argv', ['test']):
                init_config(__description__, __doc__, __version__, build_date)
                ssl_config = get_config('ssl')
                self.assertEqual(ssl_config, 'false')
```

---

## 🧑‍💻 Clone Par 2
**File:** `tests/test_config_ssl.py`
**Lines:** 122 to 131

```text
def test_case_insensitive_env_vars(self):
        """Test that environment variables are case insensitive"""
        env_vars = {'ddns_ssl': 'false', 'ddns_token': 'test'}
        with patch.dict(os.environ, env_vars):
            with patch.object(sys, 'argv', ['test']):
                init_config(__description__, __doc__, __version__, build_date)
                ssl_config = get_config('ssl')
                self.assertEqual(ssl_config, 'false')
```

