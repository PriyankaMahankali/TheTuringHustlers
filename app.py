import streamlit as st
from backend import generate_cover_letter

# Streamlit UI
st.set_page_config(page_title="AI Cover Letter Generator", layout="wide")

st.title("📄 AI Cover Letter Generator")
st.write("Enter your custom prompt to generate a personalized cover letter.")

# User input for the prompt
user_prompt = st.text_area("Custom Prompt", help="Write your own detailed prompt for the AI.")

# Generate button
if st.button("Generate Cover Letter"):
    if user_prompt:
        cover_letter = generate_cover_letter(user_prompt)
        st.subheader("📄 Your Cover Letter")
        st.text_area("", cover_letter, height=300)
    else:
        st.error("Please enter a prompt before generating the cover letter.")
