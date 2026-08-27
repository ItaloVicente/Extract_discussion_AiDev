# 🔍 Clone Analysis | Project: triton-viz | PR: #86

- **Commit SHA:** `b436d64310684bfa4cb70125bf34a82421a5fff0`
- **Clone Fingerprint:** `c5cecdb2a95ef6ba9987d6ddde2b797a`
- **Categoria:** `unique_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `examples/load_store_simple.py`
**Lines:** 18 to 31

```text
def simple_kernel(
    x_ptr,
    output_ptr,
    n_elements,
    BLOCK_SIZE: tl.constexpr,
):
    pid = tl.program_id(axis=0)
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)
    mask = offsets < n_elements
    x = tl.load(x_ptr + offsets, mask=mask)
    tl.store(output_ptr + offsets, x, mask=mask)
```

---

## 🧑‍💻 Clone Par 2
**File:** `examples/load_store.py`
**Lines:** 12 to 25

```text
def simple_kernel(
    x_ptr,
    output_ptr,
    n_elements,
    BLOCK_SIZE: tl.constexpr,
):
    pid = tl.program_id(axis=0)
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)
    mask = offsets < n_elements
    x = tl.load(x_ptr + offsets, mask=mask)
    tl.store(output_ptr + offsets, x, mask=mask)
```

