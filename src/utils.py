import os
from PyPDF2 import PdfReader

def load_text_file(file_path):
    """Load a plain text file as a list of lines."""
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def load_pdf_file(file_path):
    """Extract text from a PDF and return as a list of lines."""
    reader = PdfReader(file_path)
    text = []
    for page in reader.pages:
        content = page.extract_text()
        if content:
            # Split by lines for better retrieval granularity
            text.extend([line.strip() for line in content.split("\n") if line.strip()])
    return text

def load_documents_from_data(data_dir="data"):
    """Load all .txt and .pdf documents from a folder."""
    docs = []
    for fname in os.listdir(data_dir):
        fpath = os.path.join(data_dir, fname)
        if fname.lower().endswith(".txt"):
            docs.extend(load_text_file(fpath))
        elif fname.lower().endswith(".pdf"):
            docs.extend(load_pdf_file(fpath))
    return docs
