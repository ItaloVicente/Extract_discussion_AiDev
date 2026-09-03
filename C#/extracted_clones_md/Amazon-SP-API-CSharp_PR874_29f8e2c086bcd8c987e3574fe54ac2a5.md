# 🔍 Clone Analysis | Project: Amazon-SP-API-CSharp | PR: #874

- **Commit SHA:** `ececefada63fc1043c9a430cf9a642dd6f27dc44`
- **Clone Fingerprint:** `29f8e2c086bcd8c987e3574fe54ac2a5`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `Source/FikaAmazonAPI/Services/ReportService.cs`
**Lines:** 475 to 508

```text
public async Task<IList<string>> DownloadExistingReportAndDownloadFileAsync(ReportTypes reportTypes, DateTime? createdSince = null, DateTime? createdUntil = null, CancellationToken cancellationToken = default)
        {
            var parameters = new ParameterReportList();
            parameters.reportTypes = new List<ReportTypes>();
            parameters.reportTypes.Add(reportTypes);

            parameters.marketplaceIds = new MarketplaceIds();
            parameters.marketplaceIds.Add(AmazonCredential.MarketPlace.ID);


            if (createdSince.HasValue)
                parameters.createdSince = createdSince;
            if (createdUntil.HasValue)
                parameters.createdUntil = createdUntil;

            var reports = await GetReportsAsync(parameters, cancellationToken);

            var reportsPath = new List<string>();

            if (reports != null)
            {
                foreach (var reportData in reports)
                {
                    if (!string.IsNullOrEmpty(reportData.ReportDocumentId))
                    {
                        var filePath = await GetReportFileAsync(reportData.ReportDocumentId, cancellationToken: cancellationToken);
                        reportsPath.Add(filePath);

                    }
                }
            }

            return reportsPath;
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `Source/FikaAmazonAPI/Services/ReportService.cs`
**Lines:** 513 to 545

```text
public async Task<IList<MemoryStream>> DownloadExistingReportAndDownloadFileStreamAsync(ReportTypes reportTypes, DateTime? createdSince = null, DateTime? createdUntil = null, CancellationToken cancellationToken = default)
        {
            var parameters = new ParameterReportList();
            parameters.reportTypes = new List<ReportTypes>();
            parameters.reportTypes.Add(reportTypes);

            parameters.marketplaceIds = new MarketplaceIds();
            parameters.marketplaceIds.Add(AmazonCredential.MarketPlace.ID);

            if (createdSince.HasValue)
                parameters.createdSince = createdSince;
            if (createdUntil.HasValue)
                parameters.createdUntil = createdUntil;

            var reports = await GetReportsAsync(parameters, cancellationToken);

            var reportsStreams = new List<MemoryStream>();

            if (reports != null)
            {
                foreach (var reportData in reports)
                {
                    if (!string.IsNullOrEmpty(reportData.ReportDocumentId))
                    {
                        var stream = await GetReportFileStreamAsync(reportData.ReportDocumentId, cancellationToken: cancellationToken);
                        reportsStreams.Add(stream);

                    }
                }
            }

            return reportsStreams;
        }
```

