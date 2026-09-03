# 🔍 Clone Analysis | Project: operaton | PR: #912

- **Commit SHA:** `a66410b72e994d5555fd89ef4e9045a77f31139b`
- **Clone Fingerprint:** `5cf4e103f2ea6304de4b4fba6b7f0489`
- **Categoria:** `ini_mei_final`

---

## 🧑‍💻 Clone Par 1
**File:** `engine/src/test/java/org/operaton/bpm/engine/test/jobexecutor/JobDefinitionCreationWithParseListenerTest.java`
**Lines:** 70 to 86

```text
void testCreateJobDefinitionWithParseListener() {
    //given
    String modelFileName = "jobCreationWithinParseListener.bpmn20.xml";
    InputStream in = JobDefinitionCreationWithParseListenerTest.class.getResourceAsStream(modelFileName);
    DeploymentBuilder builder = engineRule.getRepositoryService().createDeployment().addInputStream(modelFileName, in);

    //when the asyncBefore is set in the parse listener
    Deployment deployment = builder.deploy();
    engineRule.manageDeployment(deployment);

    //then there exists a new job definition
    JobDefinitionQuery query = engineRule.getManagementService().createJobDefinitionQuery();
    JobDefinition jobDef = query.singleResult();
    assertNotNull(jobDef);
    assertEquals(jobDef.getProcessDefinitionKey(), "oneTaskProcess");
    assertEquals(jobDef.getActivityId(), "servicetask1");
  }
```

---

## 🧑‍💻 Clone Par 2
**File:** `engine/src/test/java/org/operaton/bpm/engine/test/jobexecutor/JobDefinitionCreationWithParseListenerTest.java`
**Lines:** 90 to 106

```text
void testCreateJobDefinitionWithParseListenerAndAsyncInXml() {
    //given the asyncBefore is set in the xml
    String modelFileName = "jobAsyncBeforeCreationWithinParseListener.bpmn20.xml";
    InputStream in = JobDefinitionCreationWithParseListenerTest.class.getResourceAsStream(modelFileName);
    DeploymentBuilder builder = engineRule.getRepositoryService().createDeployment().addInputStream(modelFileName, in);

    //when the asyncBefore is set in the parse listener
    Deployment deployment = builder.deploy();
    engineRule.manageDeployment(deployment);

    //then there exists only one job definition
    JobDefinitionQuery query = engineRule.getManagementService().createJobDefinitionQuery();
    JobDefinition jobDef = query.singleResult();
    assertNotNull(jobDef);
    assertEquals(jobDef.getProcessDefinitionKey(), "oneTaskProcess");
    assertEquals(jobDef.getActivityId(), "servicetask1");
  }
```

