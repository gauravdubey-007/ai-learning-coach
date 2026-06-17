import fitz
import os
from pptx import Presentation

def read_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        page_text = page.get_text()
        if page_text:
            text += page_text
    return text

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_ppt(file_path):
    text = ""
    prs = Presentation(file_path)
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                text += shape.text_frame.text + "\n"
    return text

def extract_text(extension):
    folder = os.getcwd()
    all_text = ""
    for file in os.listdir(folder):
        if file.endswith(f".{extension}"):
            full_path = os.path.join(folder, file)
            if extension == "pdf":
                all_text += read_pdf(full_path)
            elif extension == "txt":
                all_text += read_txt(full_path)
            elif extension == "pptx":
                all_text += read_ppt(full_path)
    return all_text
