# 🔍 Clone Analysis | Project: onnxscript | PR: #2406

- **Commit SHA:** `02b5e5d7bfda97536245e62a3de5ad0c73b45199`
- **Clone Fingerprint:** `e329f24f9341551afb98d0182b8cfadb`
- **Categoria:** `mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `onnxscript/rewriter/ort_fusions/group_normalization_merge_silu.py`
**Lines:** 13 to 36

```text
def group_normalization_and_silu_submodule(
    op,
    input,
    weight,
    bias,
    epsilon,
    groups,
):
    group_norm = op.GroupNorm(
        input,
        weight,
        bias,
        activation=0,
        channels_last=1,
        epsilon=epsilon,
        groups=groups,
        _domain="com.microsoft",
    )
    transposed = op.Transpose(group_norm, perm=[0, 3, 1, 2])
    return torch_module_op.submodule("torch_nn_modules_activation_SiLU")(
        transposed
    )  # TODO(rama)
```

---

## 🧑‍💻 Clone Par 2
**File:** `onnxscript/rewriter/ort_fusions/group_normalization_merge_silu.py`
**Lines:** 37 to 57

```text
def group_normalization_with_silu(
    op,
    input,
    weight,
    bias,
    epsilon,
    groups,
):
    group_norm = op.GroupNorm(
        input,
        weight,
        bias,
        activation=1,
        channels_last=1,
        epsilon=epsilon,
        groups=groups,
        _domain="com.microsoft",
    )
    return op.Transpose(group_norm, perm=[0, 3, 1, 2])
```

