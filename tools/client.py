import ollama
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OllamaClient:
    def __init__(self, model_name="llama3.2"):
        self.model_name = model_name

    def generate_response(self, prompt: str) -> str:
        """
        Generates a response from the local Ollama model.
        
        Args:
            prompt (str): The full prompt to send to the model.
            
        Returns:
            str: The content of the model's response.
            
        Raises:
            Exception: If the connection fails or generation errors.
        """
        try:
            logger.info(f"Sending request to Ollama model: {self.model_name}")
            response = ollama.chat(model=self.model_name, messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            content = response['message']['content']
            logger.info("Received response from Ollama.")
            return content
            
        except Exception as e:
            logger.error(f"Error communicating with Ollama: {e}")
            raise Exception(f"Failed to generate test cases. Is Ollama running? Error: {str(e)}")

# Singleton instance for easy import
client = OllamaClient()
