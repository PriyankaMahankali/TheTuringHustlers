import os
import openai
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Request model
class CoverLetterRequest(BaseModel):
    name: str
    job_title: str
    company_name: str
    skills: str
    experience: str
    custom_prompt: str  # Added field for user-defined prompt

# Function to generate cover letter using OpenAI GPT
def generate_cover_letter(name, job_title, company_name, skills, experience, custom_prompt):
    # If a custom prompt is provided, use it. Otherwise, use a default prompt.
    prompt = custom_prompt if custom_prompt else f"""
    Write a professional and personalized cover letter for {name}, who is applying for the position of {job_title} at {company_name}. 
    The cover letter should highlight their key skills ({skills}) and their experience ({experience}). Keep it concise and engaging.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI cover letter generator."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# API endpoint for cover letter generation
@app.post("/generate_cover_letter/")
async def generate(request: CoverLetterRequest):
    cover_letter = generate_cover_letter(
        request.name, request.job_title, request.company_name, request.skills, request.experience, request.custom_prompt
    )
    return {"cover_letter": cover_letter}
