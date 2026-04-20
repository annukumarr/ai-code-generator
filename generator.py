import google.generativeai as genai
import os
from dotenv import load_dotenv
from config import MODEL, SYSTEM_PROMPT

load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel(MODEL)

def generate_code(language: str, prompt: str) -> str:
    try:
        response = model.generate_content(
            f"{SYSTEM_PROMPT}\n\nLanguage: {language}\nTask: {prompt}"
        )

        return response.text if response.text else "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"