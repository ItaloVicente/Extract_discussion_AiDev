# 🔍 Clone Analysis | Project: posthog | PR: #35081

- **Commit SHA:** `42470e5ec004259a14494cfb903561f0c9bf829a`
- **Clone Fingerprint:** `60185943f6dea19c55fb8f3fea5fcb0b`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `posthog/queries/funnels/test/test_funnel_trends.py`
**Lines:** 508 to 559

```text
def test_period_not_final(self):
        # Use timezone-aware datetime to ensure consistent behavior across environments
        now = datetime.now(tz=ZoneInfo("UTC"))

        journeys_for(
            {
                "user_eight": [
                    {"event": "step one", "timestamp": now.strftime("%Y-%m-%d %H:%M:%S.%f")},
                    {"event": "step two", "timestamp": (now + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S.%f")},
                    {"event": "step three", "timestamp": (now + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S.%f")},
                ]
            },
            self.team,
        )

        filter = Filter(
            data={
                "insight": INSIGHT_FUNNELS,
                "display": TRENDS_LINEAR,
                "interval": "day",
                "date_from": (now - timedelta(1)).strftime(FORMAT_TIME),
                "date_to": now.strftime(FORMAT_TIME_DAY_END),
                "funnel_window_days": 1,
                "events": [
                    {"id": "step one", "order": 0},
                    {"id": "step two", "order": 1},
                    {"id": "step three", "order": 2},
                ],
            }
        )
        results = ClickhouseFunnelTrends(filter, self.team)._exec_query()

        self.assertEqual(len(results), 2)

        day = results[0]  # yesterday
        self.assertEqual(day["reached_from_step_count"], 0)
        self.assertEqual(day["reached_to_step_count"], 0)
        self.assertEqual(day["conversion_rate"], 0)
        self.assertEqual(
            day["timestamp"].replace(tzinfo=ZoneInfo("UTC")),
            (datetime(now.year, now.month, now.day) - timedelta(1)).replace(tzinfo=ZoneInfo("UTC")),
        )

        day = results[1]  # today
        self.assertEqual(day["reached_from_step_count"], 1)
        self.assertEqual(day["reached_to_step_count"], 1)
        self.assertEqual(day["conversion_rate"], 100)
        self.assertEqual(
            day["timestamp"].replace(tzinfo=ZoneInfo("UTC")),
            datetime(now.year, now.month, now.day).replace(tzinfo=ZoneInfo("UTC")),
        )
```

---

## 🧑‍💻 Clone Par 2
**File:** `posthog/hogql_queries/insights/funnels/test/test_funnel_trends.py`
**Lines:** 547 to 598

```text
def test_period_not_final(self):
        now = datetime.now()

        journeys_for(
            {
                "user_eight": [
                    {"event": "step one", "timestamp": now},
                    {"event": "step two", "timestamp": now + timedelta(minutes=1)},
                    {"event": "step three", "timestamp": now + timedelta(minutes=2)},
                ]
            },
            self.team,
        )

        filters = {
            "insight": INSIGHT_FUNNELS,
            "funnel_viz_type": "trends",
            "display": TRENDS_LINEAR,
            "interval": "day",
            "date_from": (now - timedelta(1)).strftime(FORMAT_TIME),
            "date_to": now.strftime(FORMAT_TIME_DAY_END),
            "funnel_window_days": 1,
            "events": [
                {"id": "step one", "order": 0},
                {"id": "step two", "order": 1},
                {"id": "step three", "order": 2},
            ],
        }

        query = cast(FunnelsQuery, filter_to_query(filters))
        results = FunnelsQueryRunner(query=query, team=self.team, just_summarize=True).calculate().results

        self.assertEqual(len(results), 2)

        day = results[0]  # yesterday
        self.assertEqual(day["reached_from_step_count"], 0)
        self.assertEqual(day["reached_to_step_count"], 0)
        self.assertEqual(day["conversion_rate"], 0)
        self.assertEqual(
            day["timestamp"].replace(tzinfo=ZoneInfo("UTC")),
            (datetime(now.year, now.month, now.day) - timedelta(1)).replace(tzinfo=ZoneInfo("UTC")),
        )

        day = results[1]  # today
        self.assertEqual(day["reached_from_step_count"], 1)
        self.assertEqual(day["reached_to_step_count"], 1)
        self.assertEqual(day["conversion_rate"], 100)
        self.assertEqual(
            day["timestamp"].replace(tzinfo=ZoneInfo("UTC")),
            datetime(now.year, now.month, now.day).replace(tzinfo=ZoneInfo("UTC")),
        )
```

