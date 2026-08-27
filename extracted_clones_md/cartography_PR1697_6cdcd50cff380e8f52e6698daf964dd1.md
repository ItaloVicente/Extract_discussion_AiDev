# 🔍 Clone Analysis | Project: cartography | PR: #1697

- **Commit SHA:** `09f7d5cc7e2eadf8de56645961fb91782b5d52a0`
- **Clone Fingerprint:** `6cdcd50cff380e8f52e6698daf964dd1`
- **Categoria:** `mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `cartography/intel/aws/efs.py`
**Lines:** 136 to 155

```text
def load_efs_mount_targets(
    neo4j_session: neo4j.Session,
    data: List[Dict[str, Any]],
    region: str,
    current_aws_account_id: str,
    aws_update_tag: int,
) -> None:
    logger.info(
        f"Loading Efs {len(data)} mount targets for region '{region}' into graph.",
    )
    load(
        neo4j_session,
        EfsMountTargetSchema(),
        data,
        lastupdated=aws_update_tag,
        Region=region,
        AWS_ID=current_aws_account_id,
    )
```

---

## 🧑‍💻 Clone Par 2
**File:** `cartography/intel/aws/identitycenter.py`
**Lines:** 45 to 67

```text
def load_identity_center_instances(
    neo4j_session: neo4j.Session,
    instance_data: List[Dict],
    region: str,
    current_aws_account_id: str,
    aws_update_tag: int,
) -> None:
    """
    Load Identity Center instances into the graph
    """
    logger.info(
        f"Loading {len(instance_data)} Identity Center instances for region {region}",
    )
    load(
        neo4j_session,
        AWSIdentityCenterInstanceSchema(),
        instance_data,
        lastupdated=aws_update_tag,
        Region=region,
        AWS_ID=current_aws_account_id,
    )
```

