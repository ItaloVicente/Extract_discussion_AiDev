# 🔍 Clone Analysis | Project: Chronicle-Values | PR: #159

- **Commit SHA:** `1fcee9eceeaee1694d746a01f21cda11d0d434ee`
- **Clone Fingerprint:** `bd269f1aebc4602ee9a7eae284163916`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `src/main/java/net/openhft/chronicle/values/CharSequenceFieldModel.java`
**Lines:** 526 to 545

```text
void generateEquals(ValueBuilder valueBuilder, MethodSpec.Builder methodBuilder) {
            if (get != null) {
                boolean hasGetUsing = getUsing != null;
                if (hasGetUsing) {
                    ClassName heapClassName = valueBuilder.className();
                    methodBuilder.beginControlFlow("if (other instanceof $T)", heapClassName);
                }
                methodBuilder.addCode("if (!$T.equals($N, other.$N())) return false;\n",
                        CharSequences.class, field, get.getName());
                if (hasGetUsing) {
                    methodBuilder.nextControlFlow("else");
                    {
                        equalsWithGetUsing(methodBuilder);
                    }
                    methodBuilder.endControlFlow();
                }
            } else {
                equalsWithGetUsing(methodBuilder);
            }
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `src/main/java/net/openhft/chronicle/values/CharSequenceFieldModel.java`
**Lines:** 560 to 581

```text
void generateArrayElementEquals(
                ArrayFieldModel arrayFieldModel, ValueBuilder valueBuilder,
                MethodSpec.Builder methodBuilder) {
            if (get != null) {
                boolean hasGetUsing = getUsing != null;
                if (hasGetUsing) {
                    ClassName heapClassName = valueBuilder.className();
                    methodBuilder.beginControlFlow("if (other instanceof $T)", heapClassName);
                }
                methodBuilder.addCode("if (!$T.equals($N[index], other.$N(index))) return false;\n",
                        CharSequences.class, field, get.getName());
                if (hasGetUsing) {
                    methodBuilder.nextControlFlow("else");
                    {
                        equalsArrayElementWithGetUsing(methodBuilder);
                    }
                    methodBuilder.endControlFlow();
                }
            } else {
                equalsArrayElementWithGetUsing(methodBuilder);
            }
        }
```

