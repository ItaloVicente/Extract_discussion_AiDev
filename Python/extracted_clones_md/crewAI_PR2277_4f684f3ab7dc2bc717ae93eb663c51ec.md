# 🔍 Clone Analysis | Project: crewAI | PR: #2277

- **Commit SHA:** `ec8e705bbc64211dbd81c60afb27ca70d9c14165`
- **Clone Fingerprint:** `4f684f3ab7dc2bc717ae93eb663c51ec`
- **Categoria:** `unique_ini`

---

## 🧑‍💻 Clone Par 1
**File:** `tests/custom_llm_test.py`
**Lines:** 16 to 31

```text
def call(
        self,
        messages: Union[str, List[Dict[str, str]]],
        tools: Optional[List[dict]] = None,
        callbacks: Optional[List[Any]] = None,
        available_functions: Optional[Dict[str, Any]] = None,
    ) -> Union[str, Any]:
        """Record the call and return the predefined response."""
        self.calls.append({
            "messages": messages, 
            "tools": tools,
            "callbacks": callbacks,
            "available_functions": available_functions
        })
        return self.response
```

---

## 🧑‍💻 Clone Par 2
**File:** `tests/custom_llm_test.py`
**Lines:** 69 to 85

```text
def call(
        self,
        messages: Union[str, List[Dict[str, str]]],
        tools: Optional[List[dict]] = None,
        callbacks: Optional[List[Any]] = None,
        available_functions: Optional[Dict[str, Any]] = None,
    ) -> Union[str, Any]:
        self.calls.append({
            "messages": messages, 
            "tools": tools,
            "callbacks": callbacks,
            "available_functions": available_functions
        })
        # In a real implementation, this would use the JWT token to authenticate
        # with an external service
        return "Response from JWT-authenticated LLM"
```

