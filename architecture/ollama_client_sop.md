# SOP: Ollama Client Interface

**Objective:**
To provide a deterministic, atomic interface for communicating with the local Ollama LLM service.

## 1. Interface Definition

**Input:**
- `prompt` (string): The text prompt to send to the model.
- `model_name` (string, optional): The name of the model to query (default: `llama3.2`).

**Output:**
- `content` (string): The generated text response from the model.

## 2. Logic Flow (The "Tool")

The `OllamaClient` class in `client.py` manages this interaction:

1.  **Preparation:**
    -   Initialize with `model_name`.
    -   *Constraint:* Assume Ollama is running locally on default port (11434).

2.  **Request Construction:**
    -   Format the request using `ollama.chat`:
        -   `model`: `self.model_name`
        -   `messages`: `[{'role': 'user', 'content': prompt}]`

3.  **Execution:**
    -   Send the request to the `ollama` library.
    -   *Logging:* Log the request sending (INFO level).

4.  **Response Extraction:**
    -   Extract `response['message']['content']`.
    -   *Logging:* Log the response receipt (INFO level).

5.  **Error Handling:**
    -   Catch `Exception` during the call.
    -   *Action:* Log the error (ERROR level) and raise a new `Exception` with a user-friendly message: "Failed to generate test cases. Is Ollama running? Error: ..."

## 3. Architecture Constraints

-   **Atomic Operation:** This tool does one thing: Send prompt -> Get response. It does not parse JSON, validate input, or format templates.
-   **Environment Independence:** The client assumes standard Ollama configuration.
-   **No Retries:** Currently, the client does not implement automatic retries (fail-fast).

## 4. Edge Cases

| Scenario | System Behavior |
| :--- | :--- |
| **Ollama Service Down** | Raises `Exception: Failed to generate...` immediately. |
| **Model Not Found** | Likely raises `ollama.ResponseError` inside the library call. |
| **Empty Response** | Returns empty string (if model generates nothing). |
| **Timeout** | Dependent on underlying `ollama` library timeout settings (default: infinite/long). |
