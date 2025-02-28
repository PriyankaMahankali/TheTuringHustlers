from gpt4all import GPT4All

# Load the GPT4All model
MODEL_PATH = "C:/Users/priya/OneDrive/Documents/GenAIHackathon/Meta-Llama-3-8B-Instruct.Q4_0.gguf"
model = GPT4All(MODEL_PATH, allow_download=False)

def generate_cover_letter(name, job_title, skills, writing_style):
    """
    Uses GPT4All to generate a cover letter based on structured user inputs.
    """
    user_prompt = (
        f"Write a {writing_style.lower()} cover letter for {name} applying for the position of {job_title}. "
        f"Highlight the following skills: {skills}."
    )
    
    response = model.generate(user_prompt)
    return response if response else "Error generating cover letter."

