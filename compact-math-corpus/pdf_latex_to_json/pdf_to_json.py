import fitz  # PyMuPDF
import spacy
import json

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text

def pdf_to_json(pdf_path, output_path):
    nlp = spacy.load("en_core_web_sm")
    text = extract_text_from_pdf(pdf_path)
    doc = nlp(text)
    data = {"sentences": [sent.text for sent in doc.sents]}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Tokenized PDF text saved to: {output_path}")
