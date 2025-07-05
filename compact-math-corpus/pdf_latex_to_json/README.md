# PDF and LaTeX to JSON Converter

This project extracts text from any PDF (e.g., textbooks) and a LaTeX file (e.g., Jim Hefferon's appendix) and converts them into sentence-based JSON files using Python and spaCy.

## Features

- Converts any PDF (e.g., textbook) into tokenized sentences
- Converts LaTeX appendix into plain text and tokenized sentences
- Saves both outputs as JSON

## File Structure

- `pdf_to_json.py` — Extracts and tokenizes PDF content using spaCy
- `latex_to_json.py` — Converts LaTeX to plain text and splits into sentences
- `main.py` — Runs both processes

## Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage

```bash
python main.py
```

## Notes

- Place the input files in a `data/` folder:
  - any PDF file (e.g., `lahefferon.pdf`)
  - `texappen-lahefferon-tex.tex`
- Output files will be saved in an `outputs/` folder.
