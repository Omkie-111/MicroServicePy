import google.generativeai as genai
import pypdf as pdf
from dotenv import load_dotenv

load_dotenv()  ## load all our environment variables
API_KEY = "AIzaSyAiaBGYjqySBaXjtOs1g7bY6nF8UD3z1Oo"
genai.configure(api_key=API_KEY)


def get_gemini_repsonse(input_prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input_prompt)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text
