import json
import spacy
from tqdm import tqdm
from spacy_conll import ConllFormatter
import time
import os

def run(input_path: str = "cmcorpus.json", output_path: str = "cmcorpus.conll"):
    """Processes a JSON file of sentences and outputs a CoNLL-formatted file."""
    start_time = time.time()

    if not os.path.exists(input_path):
        print(f"[ERROR] Input file not found: {input_path}")
        return

    try:
        with open(input_path, "r", encoding="utf-8") as infile:
            data = json.load(infile)
    except Exception as e:
        print(f"[ERROR] Failed to load JSON: {e}")
        return

    if isinstance(data, dict) and "sentences" in data:
        data = [{"content": sentence} for sentence in data["sentences"]]

    if not data:
        print("[WARNING] No valid content found.")
        return

    nlp = spacy.load("en_core_web_sm")
    if "senter" not in nlp.pipe_names and "parser" not in nlp.pipe_names:
        print("[WARNING] Sentence segmentation model is not enabled.")

    nlp.add_pipe("conll_formatter", last=True)

    doc_id = 0
    sent_id = 0

    with open(output_path, "w", encoding="utf-8") as outfile:
        for article in tqdm(data, desc="Processing articles"):
            content = article.get("content", "").strip()
            if not content:
                continue

            doc = nlp(content)
            doc_id += 1
            outfile.write(f"# doc_id = {doc_id}\n")

            for sent in doc.sents:
                sent_id += 1
                outfile.write(f"# sent_id = {sent_id}\n")
                outfile.write(f"# text = {sent.text}\n")

                conll_output = sent._.conll_str.strip()
                if not conll_output:
                    print(f"[WARNING] Empty CoNLL output for sentence {sent_id}")
                outfile.write(conll_output + "\n\n")

    elapsed = time.time() - start_time
    print(f"[INFO] CoNLL file saved at: {output_path}")
    print(f"[INFO] Time taken: {elapsed:.2f} seconds")

if __name__ == "__main__":
    run()
    
