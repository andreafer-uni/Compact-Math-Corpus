import json
import csv
import spacy
import time
from tqdm import tqdm
import os

def run(json_path="cmcorpus.json", output_file="cmcorpus-spacyfeatures.tsv", model="en_core_web_sm"):
    """Extracts linguistic features from a JSON file and writes them to a TSV file."""

    if not os.path.exists(json_path):
        print(f"[ERROR] Input file not found: {json_path}")
        return

    start_time = time.time()
    print(f"[INFO] Loading spaCy model: {model}")
    nlp = spacy.load(model)

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to read JSON: {e}")
        return

    with open(output_file, "w", encoding="utf-8", newline="") as tsvfile:
        writer = csv.writer(tsvfile, delimiter="\t", quoting=csv.QUOTE_MINIMAL, escapechar="\\")
        writer.writerow([
            "Token ID", "Token", "Lemma", "POS", "Morph Tag",
            "Morph Features", "Head ID", "Dependency", "Head Token"
        ])

        for sentence in tqdm(data.get("sentences", []), desc="Processing sentences", unit="sentence"):
            doc = nlp(sentence)
            for token in doc:
                writer.writerow([
                    token.i + 1,
                    token.text,
                    token.lemma_,
                    token.pos_,
                    token.tag_,
                    str(token.morph.to_dict()),
                    token.head.i + 1,
                    token.dep_,
                    token.head.text
                ])

    elapsed = time.time() - start_time
    print(f"[INFO] TSV file saved to: {output_file}")
    print(f"[INFO] Time taken: {elapsed:.2f} seconds")

if __name__ == "__main__":
    run()
