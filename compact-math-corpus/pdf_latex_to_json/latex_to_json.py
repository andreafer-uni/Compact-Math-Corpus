import re
import json
from pylatexenc.latex2text import LatexNodes2Text

def latex_to_json(latex_file_path, output_path):
    with open(latex_file_path, "r", encoding="utf-8") as f:
        latex_content = f.read()

    latex_content = re.sub(r'\\index\{.*?\}', '', latex_content)
    plain_text = LatexNodes2Text().latex_to_text(latex_content)

    plain_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', plain_text)
    plain_text = re.sub(r'(\$.*?\$)', r'\1 ', plain_text)
    plain_text = re.sub(r'(\\\[.*?\\\])', r'\1 ', plain_text)

    sentences = re.split(r'(?<=[.!?])\s+', plain_text)
    sentences = [s.strip() for s in sentences if s.strip()]

    data = {"sentences": sentences}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"LaTeX content converted and saved to: {output_path}")
