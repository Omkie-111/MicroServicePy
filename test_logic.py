from unittest.mock import MagicMock, patch

# Assuming `get_gemini_response` and `input_pdf_text` are defined in a module named `main.logic`
import main
import main.logic

# Mocking genai.GenerativeModel
@patch('main.logic.genai.GenerativeModel')
def test_get_gemini_response(mock_generative_model):
    mock_model_instance = MagicMock()
    mock_model_instance.generate_content.return_value.text = "Generated text"
    mock_generative_model.return_value = mock_model_instance

    input_prompt = "Input prompt"
    response = main.logic.get_gemini_repsonse(input_prompt)
    
    assert response == "Generated text"

# Mocking pdf.PdfReader
@patch('main.logic.pdf.PdfReader')
def test_input_pdf_text(mock_pdf_reader):
    mock_reader_instance = MagicMock()
    mock_reader_instance.pages = [MagicMock(extract_text=lambda: "Page 1 text"),
                                   MagicMock(extract_text=lambda: "Page 2 text")]
    mock_pdf_reader.return_value = mock_reader_instance

    uploaded_file = "dummy_file.pdf"
    text = main.logic.input_pdf_text(uploaded_file)
    
    assert text == "Page 1 textPage 2 text"

