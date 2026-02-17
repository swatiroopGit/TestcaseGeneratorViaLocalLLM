import sys
import os

# Add parent directory to path to allow importing from root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic import generate_test_cases
# Mock client to avoid actual LLM calls during this basic test if possible,
# or just run it to test full integration.
# For this architect phase verification, let's test full integration (Integration Test).

def test_integration():
    print("Testing generate_test_cases integration...")
    try:
        user_input = "A simple login form with email and password."
        result = generate_test_cases(user_input)
        print(f"Result received (len={len(result)}):")
        print(result[:200] + "..." if len(result) > 200 else result)
        
        if "test_cases" in result:
             print("SUCCESS: JSON structure detected.")
        elif "error" in result:
             print("FAILURE: Error returned from logic.")
        else:
             print("WARNING: unexpected format.")
             
    except Exception as e:
        print(f"CRITICAL FAILURE: {e}")

if __name__ == "__main__":
    test_integration()
