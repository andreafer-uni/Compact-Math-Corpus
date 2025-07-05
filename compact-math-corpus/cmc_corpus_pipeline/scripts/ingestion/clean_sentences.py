import json
import re

def clean_sentences(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sentences = data.get("sentences", [])

    def is_valid(s):
        if not s.strip():
            return False
        if len(s.split()) < 3:
            return False
        if re.fullmatch(r"[^\w\s]{3,}", s.strip()):
            return False
        return True

    def remove_non_ascii(s):
        return ''.join(c for c in s if ord(c) < 128)

    cleaned = [remove_non_ascii(s) for s in sentences if is_valid(s)]

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"sentences": cleaned}, f, ensure_ascii=False, indent=2)
