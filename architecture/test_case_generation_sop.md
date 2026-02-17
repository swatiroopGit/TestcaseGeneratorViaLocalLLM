# SOP: Test Case Generation Logic

**Objective:**
To reliably generate structured JSON test cases (Functional, Edge, Security) from unstructured user input using a local LLM.

## 1. Interface Definition

**Input:**
- `user_input` (string): The raw description of the functionality to test.

**Output:**
- `json_string` (string): A valid JSON string containing a list of test cases, or an error message structure.

## 2. Logic Flow (The "Nexus")

The `generate_test_cases` function in `logic.py` orchestrates this flow:

1.  **Validation:**
    -   Check if `user_input` is empty or whitespace only.
    -   *Action:* If empty, raise `ValueError("User input cannot be empty.")`.

2.  **Prompt Engineering:**
    -   Load `TEST_CASE_TEMPLATE`.
    -   Inject `user_input` into the `{user_input}` placeholder of the template.
    -   *Constraint:* The template must enforce strictly valid JSON output without markdown formatting.

3.  **Tool Execution (The "Tool"):**
    -   Call `client.client.generate_response(prompt)` to send the prompt to Ollama.
    -   *Dependency:* Requires `client.py` to be configured with a valid model (default: `llama3.2`).

4.  **Response Processing:**
    -   Receive `raw_response` from the LLM.
    -   *Sanitization:*
        -   Trim whitespace.
        -   Remove ````json` prefix if present.
        -   Remove ```` ` suffix if present.
    -   *Validation:* (Implicit) The consumer of this output expects JSON. If parsing fails later, it indicates a generation failure.

5.  **Error Handling:**
    -   Capture any `Exception` during the API call (e.g., ConnectionRefusedError / Ollama not running).
    -   *Action:* Return a JSON-like error string: `{'error': '<error_message>'}`.

## 3. Architecture Constraints (Golden Rules)

-   **Deterministic Wrapper:** The `client.py` must handle the network call and retry logic (if any), presenting a simple synchronous interface to the logic layer.
-   **No Business Logic in Client:** The `client.py` should *only* send strings and receive strings. It should not know about "test cases" or JSON schema.
-   **No Network Calls in Logic:** The `logic.py` should allow dependency injection or mocking of the client for testing, though currently it imports the singleton `client` directly (tight coupling accepted for this scale).
-   **Template Versioning:** Changes to the prompt template (`TEST_CASE_TEMPLATE`) must be tested to ensure they don't break JSON structure compliance.

## 4. Edge Cases

| Scenario | System Behavior |
| :--- | :--- |
| **Empty Input** | Returns `ValueError` immediately. |
| **Ollama Offline** | Returns `{'error': '...IS Ollama running?...'}` string. |
| **LLM Returns Markdown** | Sanitization logic strips ````json` and ```` tags. |
| **LLM Returns Text** | Returns the raw text string (which will likely fail JSON parsing in the UI adapter). |
| **Long Latency** | The synchronous call blocks until generation completes or times out (default timeout depends on `ollama` lib). |
