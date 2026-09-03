# 🔍 Clone Analysis | Project: AutoGPT | PR: #10340

- **Commit SHA:** `106177cf6a82edc0396bf7ce28938733ea9e4772`
- **Clone Fingerprint:** `621fbb0ec486c1b401a28f9cbcaaca96`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `autogpt_platform/backend/backend/util/gcs_cleanup.py`
**Lines:** 63 to 118

```text
def cleanup_expired_files(self, prefix: str = "autogpt-temp/") -> Dict[str, Any]:
        """
        Clean up expired files with the given prefix.
        
        Args:
            prefix: GCS path prefix to search for expired files
            
        Returns:
            Dictionary with cleanup statistics
        """
        try:
            logger.info(f"Starting cleanup of expired files with prefix: {prefix}")
            
            deleted_files = []
            errors = []
            total_checked = 0
            
            # List all blobs with the prefix
            blobs = self.bucket.list_blobs(prefix=prefix)
            
            for blob in blobs:
                total_checked += 1
                
                try:
                    # Check if blob is expired
                    if self._is_blob_expired(blob):
                        # Delete the expired blob
                        blob.delete()
                        deleted_files.append({
                            "path": blob.name,
                            "size": blob.size,
                            "deleted_at": datetime.utcnow().isoformat()
                        })
                        logger.info(f"Deleted expired file: {blob.name}")
                
                except Exception as e:
                    error_msg = f"Failed to process blob {blob.name}: {e}"
                    logger.error(error_msg)
                    errors.append(error_msg)
            
            result = {
                "total_checked": total_checked,
                "deleted_count": len(deleted_files),
                "deleted_files": deleted_files,
                "errors": errors,
                "cleanup_time": datetime.utcnow().isoformat()
            }
            
            logger.info(f"Cleanup completed. Checked: {total_checked}, Deleted: {len(deleted_files)}, Errors: {len(errors)}")
            
            return result
        
        except Exception as e:
            logger.error(f"Cleanup failed: {e}")
            raise
```

---

## 🧑‍💻 Clone Par 2
**File:** `autogpt_platform/backend/backend/util/gcs_cleanup.py`
**Lines:** 151 to 212

```text
def cleanup_old_files_by_age(self, prefix: str = "autogpt-temp/", max_age_hours: int = 168) -> Dict[str, Any]:
        """
        Clean up files older than the specified age, regardless of metadata.
        
        Args:
            prefix: GCS path prefix to search for old files
            max_age_hours: Maximum age in hours (default 168 = 7 days)
            
        Returns:
            Dictionary with cleanup statistics
        """
        try:
            logger.info(f"Starting cleanup of files older than {max_age_hours} hours with prefix: {prefix}")
            
            deleted_files = []
            errors = []
            total_checked = 0
            
            cutoff_time = datetime.now(timezone.utc) - timezone.timedelta(hours=max_age_hours)
            
            # List all blobs with the prefix
            blobs = self.bucket.list_blobs(prefix=prefix)
            
            for blob in blobs:
                total_checked += 1
                
                try:
                    # Check if blob is older than cutoff time
                    if blob.time_created and blob.time_created < cutoff_time:
                        # Delete the old blob
                        blob.delete()
                        deleted_files.append({
                            "path": blob.name,
                            "size": blob.size,
                            "created_at": blob.time_created.isoformat(),
                            "deleted_at": datetime.utcnow().isoformat()
                        })
                        logger.info(f"Deleted old file: {blob.name}")
                
                except Exception as e:
                    error_msg = f"Failed to process blob {blob.name}: {e}"
                    logger.error(error_msg)
                    errors.append(error_msg)
            
            result = {
                "total_checked": total_checked,
                "deleted_count": len(deleted_files),
                "deleted_files": deleted_files,
                "errors": errors,
                "cleanup_time": datetime.utcnow().isoformat(),
                "max_age_hours": max_age_hours
            }
            
            logger.info(f"Age-based cleanup completed. Checked: {total_checked}, Deleted: {len(deleted_files)}, Errors: {len(errors)}")
            
            return result
        
        except Exception as e:
            logger.error(f"Age-based cleanup failed: {e}")
            raise
```

