# Project Constitution (gemini.md)

## 1. Data Schemas

### Core Domain Models

**UserRequest**
- `input_text`: string (The raw user requirement for test matching)
- `timestamp`: datetime

**TestGenerationPrompt**
- `system_template`: string (The fixed "proper template" stored in code)
- `user_context`: string (The `input_text` from UserRequest)

**TestCaseOutput**
- `test_cases`: list[TestCase]

**TestCase**
- `id`: string
- `type`: enum(functional, edge_case, security, performance)
- `title`: string
- `pre_conditions`: list[string]
- `steps`: list[string]
- `expected_result`: string

## 2. Behavioral Rules

- **North Star:** Start with the specific template defined in the codebase. Do not hallucinate formats.
- **Reliability:** If Ollama is offline, fail gracefully with a clear UI message.
- **Model:** Strictly use `llama3.2`.
- **UI:** Simple Chat Interface (Streamlit).

## 3. Architectural Invariants (A.N.T. Architecture)

- **Adapter (Frontend):** Streamlit App (`app.py`). Handles user input and displays chat.
- **Nexus (Logic):** `generator_logic.py`. Merges User Input + Template. Parsing logic.
- **Tool (Backend):** `ollama_client.py`. distinct module for calling `http://localhost:11434`.
