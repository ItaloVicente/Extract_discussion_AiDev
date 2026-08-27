# 🔍 Clone Analysis | Project: MoviePilot | PR: #4566

- **Commit SHA:** `bbffb1420bfaa023e6c4b1badd08861ffa51a15c`
- **Clone Fingerprint:** `5fd9a3fcb9ddf9d8494d05e74eb941dc`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `app/api/endpoints/workflow.py`
**Lines:** 225 to 242

```text
def pause_workflow(workflow_id: int,
                   db: Session = Depends(get_db),
                   _: schemas.TokenPayload = Depends(get_current_active_user)) -> Any:
    """
    停用工作流
    """
    workflow = Workflow.get(db, workflow_id)
    if not workflow:
        return schemas.Response(success=False, message="工作流不存在")
    # 删除定时任务
    Scheduler().remove_workflow_job(workflow)
    # 停止工作流
    global_vars.stop_workflow(workflow_id)
    # 更新状态
    workflow.update_state(db, workflow_id, "P")
    return schemas.Response(success=True)
```

---

## 🧑‍💻 Clone Par 2
**File:** `app/api/endpoints/workflow.py`
**Lines:** 244 to 259

```text
def reset_workflow(workflow_id: int,
                   db: Session = Depends(get_db),
                   _: schemas.TokenPayload = Depends(get_current_active_user)) -> Any:
    """
    重置工作流
    """
    workflow = Workflow.get(db, workflow_id)
    if not workflow:
        return schemas.Response(success=False, message="工作流不存在")
    # 停止工作流
    global_vars.stop_workflow(workflow_id)
    # 重置工作流
    workflow.reset(db, workflow_id, reset_count=True)
    # 删除缓存
    SystemConfigOper().delete(f"WorkflowCache-{workflow_id}")
    return schemas.Response(success=True)
```

