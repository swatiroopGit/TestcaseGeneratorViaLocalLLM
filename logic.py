from tools.client import client

# The "Proper Template" stored in code as per requirements.
TEST_CASE_TEMPLATE = """
You are an expert QA Automation Engineer. Your task is to generate functional and edge case test cases based on the user's description.

### Input Description:
{user_input}

### Output Format:
Propvide the output in JSON format with the following structure:
{{
    "test_cases": [
        {{
            "id": "TC_001",
            "title": "Title of the test case",
            "type": "Functional/Edge/Security",
            "pre_conditions": ["Condition 1", "Condition 2"],
            "steps": ["Step 1", "Step 2", "Step 3"],
            "expected_result": "Expected outcome"
        }}
    ]
}}

### Rules:
1.  Generate at least 5 test cases.
2.  Include at least 1 negative/edge case.
3.  Ensure the output is strictly valid JSON. Do not include markdown formatting (like ```json).
4.  Be specific and verifiable in your steps.
"""

def generate_test_cases(user_input: str) -> str:
    """
    Combines the user input with the template and calls the LLM.
    """
    if not user_input or not user_input.strip():
        raise ValueError("User input cannot be empty.")
        
    # Merge Input + Template
    prompt = TEST_CASE_TEMPLATE.format(user_input=user_input)
    
    # Call the Tool Layer
    try:
        raw_response = client.generate_response(prompt)
        
        # Basic cleanup if the model still outputs markdown
        clean_response = raw_response.strip()
        if clean_response.startswith("```json"):
            clean_response = clean_response[7:]
        if clean_response.startswith("```"):
            clean_response = clean_response[3:]
        if clean_response.endswith("```"):
            clean_response = clean_response[:-3]
            
        return clean_response.strip()
        
    except Exception as e:
        return f"{{'error': '{str(e)}'}}"
