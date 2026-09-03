# 🔍 Clone Analysis | Project: OpenDeepWiki | PR: #197

- **Commit SHA:** `2175de711b59b6f51aab9fe2182f36a3d46c80b5`
- **Clone Fingerprint:** `3b56c88066d5a1836aea7d3c64971e5d`
- **Categoria:** `unique_final`

---

## 🧑‍💻 Clone Par 1
**File:** `Provider/KoalaWiki.Provider.SqlServer/Migrations/20250513064801_Initial.cs`
**Lines:** 348 to 376

```text
protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "ChatShareMessageItems");

            migrationBuilder.DropTable(
                name: "ChatShareMessages");

            migrationBuilder.DropTable(
                name: "DocumentCatalogs");

            migrationBuilder.DropTable(
                name: "DocumentCommitRecords");

            migrationBuilder.DropTable(
                name: "DocumentFileItemSources");

            migrationBuilder.DropTable(
                name: "DocumentOverviews");

            migrationBuilder.DropTable(
                name: "Documents");

            migrationBuilder.DropTable(
                name: "Warehouses");

            migrationBuilder.DropTable(
                name: "DocumentFileItems");
        }
```

---

## 🧑‍💻 Clone Par 2
**File:** `Provider/KoalaWiki.Provider.Sqlite/Migrations/20250429184747_Initial.cs`
**Lines:** 247 to 266

```text
protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "DocumentCatalogs");

            migrationBuilder.DropTable(
                name: "DocumentFileItemSources");

            migrationBuilder.DropTable(
                name: "DocumentOverviews");

            migrationBuilder.DropTable(
                name: "Documents");

            migrationBuilder.DropTable(
                name: "Warehouses");

            migrationBuilder.DropTable(
                name: "DocumentFileItems");
        }
```

