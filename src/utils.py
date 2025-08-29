import os

def load_text_file(filepath):
    """Load a text file and return a list of lines."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().splitlines()

def pdf_to_text(pdf_path, txt_path=None):
    """
    Convert a PDF to a text file.
    Requires: pip install pypdf
    """
    from pypdf import PdfReader
    
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    if txt_path:
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(text)
    return text
