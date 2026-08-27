# 🔍 Clone Analysis | Project: pylabrobot | PR: #551

- **Commit SHA:** `5e07ef82ba43e8f38afa61a3b1777207c95470dd`
- **Clone Fingerprint:** `bfdd060abf652811758f1e30f9ac9d15`
- **Categoria:** `ini_mei`

---

## 🧑‍💻 Clone Par 1
**File:** `pylabrobot/resources/hamilton/tip_racks.py`
**Lines:** 75 to 99

```text
def HTF(name: str, with_tips: bool = True) -> TipRack:
  """Tip Rack with 96 1000ul High Volume Tip with filter"""
  return TipRack(
    name=name,
    size_x=122.4,
    size_y=82.6,
    size_z=20.0,
    model="HTF",
    ordered_items=create_ordered_items_2d(
      TipSpot,
      num_items_x=12,
      num_items_y=8,
      dx=7.2,
      dy=5.3,
      dz=-83.5,
      item_dx=9.0,
      item_dy=9.0,
      size_x=9.0,
      size_y=9.0,
      make_tip=high_volume_tip_with_filter,
    ),
    with_tips=with_tips,
  )
```

---

## 🧑‍💻 Clone Par 2
**File:** `pylabrobot/resources/hamilton/tip_racks.py`
**Lines:** 125 to 148

```text
def HTF_ULTRAWIDE(name: str, with_tips: bool = True) -> TipRack:
  """Tip Rack with 96 1000ul High Volume Tip with filter"""
  return TipRack(
    name=name,
    size_x=122.4,
    size_y=82.6,
    size_z=20.0,
    model=HTF_ULTRAWIDE.__name__,
    ordered_items=create_ordered_items_2d(
      TipSpot,
      num_items_x=12,
      num_items_y=8,
      dx=7.2,
      dy=5.3,
      dz=-68.4,
      item_dx=9.0,
      item_dy=9.0,
      size_x=9.0,
      size_y=9.0,
      make_tip=ultrawide_high_volume_tip_with_filter,
    ),
    with_tips=with_tips,
  )
```

