import streamlit as st
from backend1 import generate_cover_letter

# Streamlit UI
st.set_page_config(page_title="AI Cover Letter Generator", layout="wide")

st.title("📄 AI Cover Letter Generator")
st.write("Enter your details to generate a personalized cover letter.")

# User inputs
name = st.text_input("Your Name")
job_title = st.text_input("Job Title")
skills = st.text_area("Your Skills", help="List your key skills separated by commas.")
writing_style = st.selectbox("Writing Style", ["Formal", "Casual", "Concise", "Detailed"], index=0)

# Generate button
if st.button("Generate Cover Letter"):
    if name and job_title and skills:
        user_prompt = (
            f"Generate a well-structured {writing_style.lower()} cover letter for {name}, who is applying for the position "
            f"of {job_title}. The letter should include a proper introduction, highlight relevant skills ({skills}), and "
            f"end with a strong closing statement. Ensure proper grammar, spelling, and formatting."
        )
        cover_letter = generate_cover_letter(name, job_title, skills, writing_style)
        st.subheader("📄 Your Cover Letter")
        st.text_area("", cover_letter, height=300)
    else:
        st.error("Please fill in all required fields before generating the cover letter.")
