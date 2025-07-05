from pdf_to_json import pdf_to_json
from latex_to_json import latex_to_json

def main():
    pdf_input = "data/your-book.pdf"  # Replace with your PDF file
    pdf_output = "outputs/lahefferon-processed.json"

    latex_input = "data/texappen-lahefferon-tex.tex"
    latex_output = "outputs/texappen-lahefferon-processed.json"

    print(f"Processing PDF: {pdf_input}")
    pdf_to_json(pdf_input, pdf_output)

    print("Processing LaTeX...")
    latex_to_json(latex_input, latex_output)

if __name__ == "__main__":
    main()
