from PyPDF2 import PdfReader
import docx

def parse_resume(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return " ".join(paragraph.text for paragraph in doc.paragraphs)
    return ""