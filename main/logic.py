import google.generativeai as genai
import pypdf as pdf
from dotenv import load_dotenv

load_dotenv()  ## load all our environment variables
API_KEY = "AIzaSyAiaBGYjqySBaXjtOs1g7bY6nF8UD3z1Oo"
genai.configure(api_key=API_KEY)


def get_gemini_repsonse(input_prompt):
    """
    Generate a response using the Gemini-Pro model from GenAI based on the input prompt.

    Args:
    - input_prompt (str): The prompt to generate a response for.

    Returns:
    - str: The generated response text.
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input_prompt)
    return response.text


def input_pdf_text(uploaded_file):
    """
    Extract text content from a PDF file.

    Args:
    - uploaded_file (file): The PDF file to extract text from.

    Returns:
    - str: The extracted text content.
    """
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text
