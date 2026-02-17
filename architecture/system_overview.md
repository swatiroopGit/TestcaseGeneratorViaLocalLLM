# System Overview: A.N.T. Architecture

**Objective:**
Provide a high-level map of the system components and their interactions, following the A.N.T. (Adapter, Nexus, Tools) architectural pattern.

## 1. Component Map

### Layer 1: Adapter (Protocol A)
-   **Component:** `app.py` (Streamlit Application)
-   **Role:** The frontend interface.
-   **Responsibility:**
    -   Capture user input (`st.text_area`).
    -   Trigger the generation process (`st.button`).
    -   Display the results (`st.json` / `st.markdown`).
    -   Handle high-level errors (e.g., show "Service Down" message).
-   **Dependencies:** Imports `logic.py` (specifically `generate_test_cases`).

### Layer 2: Nexus (Protocol N)
-   **Component:** `logic.py`
-   **Role:** The business logic core.
-   **Responsibility:**
    -   **Validation:** Ensure inputs are valid.
    -   **Orchestration:** Combine inputs with templates (`TEST_CASE_TEMPLATE`).
    -   **Parsing:** Convert raw LLM output into structured data (JSON).
    -   *Constraint:* Does NOT communicate directly with externals (uses Tool layer).
-   **Dependencies:** Imports `client.py` (specifically `client` instance).

### Layer 3: Tools (Protocol T)
-   **Component:** `client.py` (Ollama Client)
-   **Role:** The execution tool.
-   **Responsibility:**
    -   **Communication:** Send prompts to the local Ollama instance.
    -   **Configuration:** Manage model selection (`llama3.2`).
    -   *Constraint:* Purely functional input/output. No business logic.
-   **Dependencies:** `ollama` library.

## 2. Execution Flow

1.  **User Input:** User enters a requirement string in the Streamlit UI.
2.  **Trigger:** User clicks "Generate".
3.  **App Call:** `app.py` calls `generate_test_cases(user_input)`.
4.  **Logic Processing:**
    -   `logic.py` validates input.
    -   `logic.py` formats the prompt using strict JSON-enforcing template.
    -   `logic.py` calls `client.generate_response(prompt)`.
5.  **Tool Execution:**
    -   `client.py` sends request to Ollama.
    -   Ollama generates response (JSON string).
    -   `client.py` returns raw string.
6.  **Parsing & Return:**
    -   `logic.py` cleans the raw string (removes markdown).
    -   `logic.py` returns the clean JSON string (or error object).
7.  **Display:** `app.py` renders the JSON in the UI.

## 3. Deployment & Environment

-   **Environment Variables:** None currently (using defaults).
-   **Local Service:** Requires `ollama serve` running on `localhost:11434`.
-   **Python Stack:** `streamlit`, `ollama`.

## 4. Future Considerations

-   **Retry Logic:** Add retry mechanism in `client.py` for transient failures.
-   **Model Selection:** allow user to select model in UI (pass through logic).
-   **Templating:** Move template to separate file or database for easier editing.
