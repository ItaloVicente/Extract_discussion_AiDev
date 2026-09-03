# 🔍 Clone Analysis | Project: weave | PR: #4555

- **Commit SHA:** `1b3a1c1334ccd8cf2783160bd0434c2828a24c4a`
- **Clone Fingerprint:** `8afd84e00c4e47ff0a69c9ad5bf1bcdf`
- **Categoria:** `mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `tests/trace_server/test_calls_query_builder.py`
**Lines:** 763 to 823

```text
def test_calls_query_with_predicate_filters() -> None:
    cq = CallsQuery(project_id="project")
    cq.add_field("id")
    cq.add_field("inputs")
    cq.add_condition(
        tsi_query.AndOperation.model_validate(
            {
                "$and": [
                    {
                        "$eq": [
                            {"$getField": "inputs.param.val"},
                            {"$literal": "hello"},
                        ]
                    },  # <-- heavy condition
                    {
                        "$eq": [{"$getField": "wb_user_id"}, {"$literal": "my_user_id"}]
                    },  # <-- light condition
                ]
            }
        )
    )
    assert_sql(
        cq,
        """
        WITH filtered_calls AS (
            SELECT
                calls_merged.id AS id
            FROM calls_merged
            WHERE calls_merged.project_id = {pb_1:String}
            GROUP BY (calls_merged.project_id, calls_merged.id)
            HAVING (
                ((any(calls_merged.wb_user_id) = {pb_0:String}))
                AND ((any(calls_merged.deleted_at) IS NULL))
                AND ((NOT ((any(calls_merged.started_at) IS NULL))))
            )
        )
        SELECT
            calls_merged.id AS id,
            any(calls_merged.inputs_dump) AS inputs_dump
        FROM calls_merged
        WHERE
            calls_merged.project_id = {pb_1:String}
        AND
            (calls_merged.id IN filtered_calls)
        AND
            ((calls_merged.inputs_dump LIKE {pb_4:String} OR calls_merged.inputs_dump IS NULL))
        GROUP BY (calls_merged.project_id, calls_merged.id)
        HAVING (
            JSON_VALUE(any(calls_merged.inputs_dump), {pb_2:String}) = {pb_3:String}
        )
        """,
        {
            "pb_0": "my_user_id",
            "pb_1": "project",
            "pb_2": '$."param"."val"',
            "pb_3": "hello",
            "pb_4": '%"hello"%',
        },
    )
```

---

## 🧑‍💻 Clone Par 2
**File:** `tests/trace_server/test_calls_query_builder.py`
**Lines:** 931 to 1003

```text
def test_calls_query_with_predicate_filters_multiple_heavy_conditions() -> None:
    cq = CallsQuery(project_id="project")
    cq.add_field("id")
    cq.add_field("inputs")
    cq.add_field("output")
    cq.add_condition(
        tsi_query.AndOperation.model_validate(
            {
                "$and": [
                    {
                        "$eq": [
                            {"$getField": "inputs.param.val"},
                            {"$literal": "hello"},
                        ]
                    },  # <-- heavy condition on start-only field
                    {
                        "$eq": [
                            {"$getField": "output.result"},
                            {"$literal": "success"},
                        ]
                    },  # <-- heavy condition on end-only field
                    {
                        "$eq": [{"$getField": "wb_user_id"}, {"$literal": "my_user_id"}]
                    },  # <-- light condition
                ]
            }
        )
    )
    assert_sql(
        cq,
        """
        WITH filtered_calls AS (
            SELECT
                calls_merged.id AS id
            FROM calls_merged
            WHERE calls_merged.project_id = {pb_1:String}
            GROUP BY (calls_merged.project_id, calls_merged.id)
            HAVING (
                ((any(calls_merged.wb_user_id) = {pb_0:String}))
                AND ((any(calls_merged.deleted_at) IS NULL))
                AND ((NOT ((any(calls_merged.started_at) IS NULL))))
            )
        )
        SELECT
            calls_merged.id AS id,
            any(calls_merged.inputs_dump) AS inputs_dump,
            any(calls_merged.output_dump) AS output_dump
        FROM calls_merged
        WHERE
            calls_merged.project_id = {pb_1:String}
        AND (calls_merged.id IN filtered_calls)
        AND ((calls_merged.inputs_dump LIKE {pb_6:String} OR calls_merged.inputs_dump IS NULL)
            AND (calls_merged.output_dump LIKE {pb_7:String} OR calls_merged.output_dump IS NULL))
        GROUP BY (calls_merged.project_id, calls_merged.id)
        HAVING (
            ((JSON_VALUE(any(calls_merged.inputs_dump), {pb_2:String}) = {pb_3:String}))
            AND
            ((JSON_VALUE(any(calls_merged.output_dump), {pb_4:String}) = {pb_5:String}))
        )
        """,
        {
            "pb_0": "my_user_id",
            "pb_1": "project",
            "pb_2": '$."param"."val"',
            "pb_3": "hello",
            "pb_4": '$."result"',
            "pb_5": "success",
            "pb_6": '%"hello"%',
            "pb_7": '%"success"%',
        },
    )
```

