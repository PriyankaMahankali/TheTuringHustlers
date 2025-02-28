import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key from environment
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def generate_cover_letter(user_prompt):
    """
    Calls Gemini API to generate a cover letter based on the user's custom prompt.
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_prompt)
    
    return response.text if response else "Error generating cover letter."
