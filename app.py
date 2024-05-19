import streamlit as st
from main.logic import input_pdf_text, get_gemini_repsonse

def main():
    st.title("Medical Report Summary Generator")
    st.text("Upload a medical report PDF to generate a summary.")

    uploaded_file = st.file_uploader(
        "Upload Your Resume", type="pdf", help="Please upload the PDF file"
    )

    if uploaded_file is not None:
        submit = st.button("Submit")
        if submit:
            input_prompt = """Study the medical report provided and give me a summary where the summary should consist of what is abnormal in this report means what is below or above healthy range
            and because of that what are the effects to the health of the person and for each give some dietary insights.
            """
            text = input_pdf_text(uploaded_file)
            response = get_gemini_repsonse(input_prompt)
            st.subheader(response)

if __name__ == "__main__":
    main()
