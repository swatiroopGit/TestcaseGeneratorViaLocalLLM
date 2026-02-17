# 🚀 GLAS.T. Auto-Test Generator

> **G**enerative **L**ocal **A**utomated **S**ystem for **T**esting
> *Built with the B.L.A.S.T. Protocol & A.N.T. Architecture*

GLAS.T. is a local AI tool that generates structured software test cases from simple feature descriptions. It leverages **Ollama** and **Llama 3.2** to run entirely offline, ensuring data privacy and zero cloud costs.

## ✨ Features

- **100% Local AI:** Powered by Ollama + Llama 3.2. No API keys required.
- **Privacy First:** Your feature requirements never leave your machine.
- **Structured Output:** Generates Functional, Edge, Security, and Performance test cases in JSON format.
- **Premium UI:** A modern Streamlit interface with dark mode and glassmorphism styling.
- **Downloadable:** Export your test suite as a JSON file for integration with other tools.

## 🏗️ Architecture (A.N.T.)

This project follows the **A.N.T.** (Adapter, Nexus, Tools) architecture for reliability:

- **Adapter (Layer 1):** `app.py` - The Streamlit frontend. Handles user interaction and display.
- **Nexus (Layer 2):** `logic.py` - The reasoning engine. Validates input and structures the prompts.
- **Tool (Layer 3):** `tools/client.py` - The execution layer. Deterministically communicates with the local Ollama instance.

## 🚀 Getting Started

### Prerequisites

1.  **Python 3.10+** installed.
2.  **Ollama** installed and running. [Download Ollama](https://ollama.com/)
3.  **Llama 3.2 Model** pulled:
    ```bash
    ollama pull llama3.2
    ```

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/swatiroopGit/TestcaseGeneratorViaLocalLLM.git
    cd TestcaseGeneratorViaLocalLLM
    ```

2.  Install Python dependencies:
    ```bash
    pip install streamlit ollama
    ```

### Running the App

1.  Ensure Ollama is running in the background (`ollama serve`).
2.  Start the Streamlit application:
    ```bash
    streamlit run app.py
    ```
3.  Open your browser to `http://localhost:8501`.

## 📖 Usage Guide

1.  **Input:** In the text area, describe the feature you want to test (e.g., *"A login page with email validation and a 'Forgot Password' link"*).
2.  **Generate:** Click the **Generate Test Cases** button.
3.  **Review:** The AI will generate a set of test cases, categorized by type (Functional, Edge, Security, etc.).
4.  **Export:** Click **Download JSON Suite** to save the results.

## 📂 Project Structure

```
├── app.py                  # Frontend (Streamlit)
├── logic.py                # Business Logic (Nexus)
├── tools/
│   └── client.py           # Ollama Interface (Tool)
├── architecture/           # Technical SOPs & Documentation
│   ├── system_overview.md
│   └── ...
├── tests/                  # Integration tests
└── README.md               # Project Documentation
```

## 📄 License

This project is open-source and available under the MIT License.
