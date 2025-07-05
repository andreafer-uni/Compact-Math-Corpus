
import json
import re

def clean_sentences(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sentences = data.get("sentences", [])

    def analyze_sentences(sentences):
        results = []
        for idx, sentence in enumerate(sentences):
            length = len(sentence)
            num_lines = sentence.count('\n')
            num_words = len(sentence.split())
            is_empty = sentence.strip() == ""
            is_too_short = num_words < 3
            is_mostly_symbols = bool(re.fullmatch(r"[^\w\s]{3,}", sentence.strip()))
            results.append({
                "index": idx,
                "length": length,
                "num_lines": num_lines,
                "num_words": num_words,
                "is_empty": is_empty,
                "is_too_short": is_too_short,
                "is_mostly_symbols": is_mostly_symbols,
                "content": sentence[:200]
            })
        return results

    analysis = analyze_sentences(sentences)
    suspect_indices = [
        result["index"] for result in analysis
        if result["is_empty"] or result["is_too_short"] or result["is_mostly_symbols"]
    ]

    cleaned_sentences = [
        s for idx, s in enumerate(sentences) if idx not in suspect_indices
    ]

    def clean_non_basic_unicode(sentences):
        return [''.join(char for char in sentence if ord(char) < 128) for sentence in sentences]

    sentences_cleaned_unicode = clean_non_basic_unicode(cleaned_sentences)

    cleaned_data = {"sentences": sentences_cleaned_unicode}
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
