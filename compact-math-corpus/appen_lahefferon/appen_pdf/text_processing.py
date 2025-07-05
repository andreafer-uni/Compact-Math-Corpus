import json
import re

def extract_and_clean_json(input_file, output_file, start_idx, end_idx):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    sentences = data["sentences"][start_idx:end_idx + 1]

    cleaned = [
        ''.join(c for c in s if ord(c) < 128)
        for s in sentences
        if s.strip() and len(s.split()) >= 3 and not re.fullmatch(r"[^\w\s]{3,}", s.strip())
    ]

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"sentences": cleaned}, f, indent=2, ensure_ascii=False)
