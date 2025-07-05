
import pandas as pd
import csv
import json
import spacy
import time
from tqdm import tqdm

def extract_spacy_features(json_path, output_file, model="en_core_web_sm"):
    nlp = spacy.load(model)
    start_time = time.time()

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(output_file, "w", encoding="utf-8", newline="") as tsvfile:
        writer = csv.writer(tsvfile, delimiter="\t", quoting=csv.QUOTE_MINIMAL, escapechar="\")
        writer.writerow([
            "Token ID", "Token", "Lemma", "POS", "Morph Tag",
            "Morph Features", "Head ID", "Dependency", "Head Token"
        ])

        for sentence in tqdm(data["sentences"], desc="Processing sentences", unit="sentence"):
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

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"TSV file saved successfully in: {output_file}")
    print(f"Execution time: {execution_time:.2f} seconds")
