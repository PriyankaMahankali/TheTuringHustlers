# AI Cover Letter Generator

## Empowering Career Progression with Tailored Cover Letters
The objective of this project is to build a generative AI model that can create personalized and professional cover letters tailored to individual job applicants.

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing.

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python** (>= 3.8 recommended)
- **Streamlit** (Python library for UI)
- **GPT4All** (Required for generating cover letters)

### Installing

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo-name/AI-Cover-Letter-Generator.git
   cd AI-Cover-Letter-Generator
   ```

2. **Set up a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download and Install GPT4All**
   - Visit [GPT4All](https://gpt4all.io/) and download the model.
   - Place the model file in the appropriate directory (e.g., `models/` inside the project folder).
   - Update `backend.py` with the correct path to your model file:
     ```python
     MODEL_PATH = "path/to/your/model.gguf"
     ```

### Running the Application

To start the Streamlit app:
```sh
streamlit run app.py
```

## Running the Tests

To ensure everything is working correctly, run the automated tests:
```sh
pytest
```

### Sample Tests
Provide sample test cases for checking the functionality of the cover letter generator.
```sh
pytest tests/test_cover_letter.py
```

### Style Test
Ensure adherence to coding standards using `flake8`.
```sh
flake8 .
```

## Deployment

To deploy this on a live system (e.g., Streamlit Cloud or a web server):
- Ensure all dependencies are installed.
- Follow Streamlit deployment guidelines.
- Update environment variables if required.

## Built With

- [Streamlit](https://streamlit.io/) - Web UI framework
- [GPT4All](https://gpt4all.io/) - AI-powered text generation

## Authors

- **Priyanka**  
- **Harika**  
- **Thanmayi**  
- **Afreen**  


## Acknowledgments

- Thanks to open-source contributors
- Inspiration from AI-powered career tools
- Support from the developer community

