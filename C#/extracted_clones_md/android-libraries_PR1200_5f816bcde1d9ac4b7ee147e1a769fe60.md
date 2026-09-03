# 🔍 Clone Analysis | Project: android-libraries | PR: #1200

- **Commit SHA:** `ec002703a53bc6a8c48ceb4f0a9148f66d59da83`
- **Clone Fingerprint:** `5f816bcde1d9ac4b7ee147e1a769fe60`
- **Categoria:** `mei`

---

## 🧑‍💻 Clone Par 1
**File:** `source/com.android.billingclient/billing/Additions/Additions.cs`
**Lines:** 86 to 104

```text
public Task<QueryPurchaseHistoryResult> QueryPurchaseHistoryAsync(string skuType)
        {
            var tcs = new TaskCompletionSource<QueryPurchaseHistoryResult>();

            var listener = new InternalPurchaseHistoryResponseListener
            {
                PurchaseHistoryResponseHandler = (r, h) => tcs.TrySetResult(new QueryPurchaseHistoryResult
                {
                    Result = r,
                    PurchaseHistoryRecords = h
                })
            };

            // QueryPurchaseHistory method may not exist in v8.x, commenting out for now
            // QueryPurchaseHistory(skuType, listener);
            tcs.TrySetResult(new QueryPurchaseHistoryResult { Result = null, PurchaseHistoryRecords = null });

            return tcs.Task;
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `source/com.android.billingclient/billing/Additions/Additions.cs`
**Lines:** 106 to 124

```text
public Task<QueryPurchaseHistoryResult> QueryPurchaseHistoryAsync(QueryPurchaseHistoryParams queryPurchaseHistoryParams)
        {
            var tcs = new TaskCompletionSource<QueryPurchaseHistoryResult>();

            var listener = new InternalPurchaseHistoryResponseListener
            {
                PurchaseHistoryResponseHandler = (r, h) => tcs.TrySetResult(new QueryPurchaseHistoryResult
                {
                    Result = r,
                    PurchaseHistoryRecords = h
                })
            };

            // QueryPurchaseHistory method may not exist in v8.x, commenting out for now
            // QueryPurchaseHistory(queryPurchaseHistoryParams, listener);
            tcs.TrySetResult(new QueryPurchaseHistoryResult { Result = null, PurchaseHistoryRecords = null });

            return tcs.Task;
        }
```

