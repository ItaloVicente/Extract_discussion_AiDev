# 🔍 Clone Analysis | Project: crewAI | PR: #2865

- **Commit SHA:** `2c26ab27c01cea0db400b2d4f5782f79afe8a49f`
- **Clone Fingerprint:** `49b22c1a3bf03bba5040d537deecc14e`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `tests/test_markdown_task.py`
**Lines:** 9 to 32

```text
def test_markdown_option_in_task_prompt():
    """Test that when markdown=True, the task prompt includes markdown formatting instructions."""
    
    researcher = Agent(
        role="Researcher",
        goal="Research a topic",
        backstory="You're a researcher specialized in providing well-formatted content.",
        allow_delegation=False,
    )

    task = Task(
        description="Research advances in AI in 2023",
        expected_output="A summary of key AI advances in 2023",
        markdown=True,
        agent=researcher,
    )

    prompt = task.prompt()
    
    assert "Research advances in AI in 2023" in prompt
    assert "A summary of key AI advances in 2023" in prompt
    assert "Your final answer MUST be formatted in Markdown syntax." in prompt
```

---

## 🧑‍💻 Clone Par 2
**File:** `tests/test_markdown_task.py`
**Lines:** 33 to 53

```text
def test_markdown_option_not_in_task_prompt_by_default():
    """Test that by default (markdown=False), the task prompt does not include markdown formatting instructions."""
    
    researcher = Agent(
        role="Researcher",
        goal="Research a topic",
        backstory="You're a researcher specialized in providing well-formatted content.",
        allow_delegation=False,
    )

    task = Task(
        description="Research advances in AI in 2023",
        expected_output="A summary of key AI advances in 2023",
        agent=researcher,
    )

    prompt = task.prompt()
    
    assert "Research advances in AI in 2023" in prompt
    assert "A summary of key AI advances in 2023" in prompt
    assert "Your final answer MUST be formatted in Markdown syntax." not in prompt
```

