# Task Plan: Local LLM Test Case Generator

## Phase 1: Initialization & Blueprint (Active)
- [x] Create project memory files
- [x] Discovery Questions answered
- [x] Define Data Schema in `gemini.md`
- [x] Define Architecture (A.N.T.)

## Phase 2: Implementation (A.N.T. Architecture)
- [x] **Infrastructure Setup**
    - [x] Install dependencies (`streamlit`, `ollama`).
    - [x] Pull `llama3.2` model locally.
- [x] **Protocol A: Adapter (UI)**
    - [x] Create `app.py` with Streamlit chat layout.
- [x] **Protocol N: Nexus (Logic)**
    - [x] Create `logic.py` containing the **Master Template**.
    - [x] Implement function to combine Input + Template.
- [x] **Protocol T: Tool (Ollama)**
    - [x] Create `client.py` to interface with Ollama API.

## Phase 3: Testing & Polish
- [ ] Verify connection to local Ollama.
- [ ] Test generation with sample inputs.
- [ ] Refine the "Proper Template" for better results.
