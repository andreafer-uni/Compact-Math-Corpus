import json
import spacy
from tqdm import tqdm
from spacy_conll import ConllFormatter

def process_json_to_conll(json_file, output_file):
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("conll_formatter", last=True)

    try:
        with open(json_file, "r", encoding="utf-8") as infile:
            data = json.load(infile)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading JSON file: {e}")
        return

    if isinstance(data, dict) and "sentences" in data:
        data = [{"content": sentence} for sentence in data["sentences"]]

    if not data:
        print("Warning: No valid articles found in the JSON file.")
        return

    doc_id = 0
    sent_id = 0

    with open(output_file, "w", encoding="utf-8") as outfile:
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
                    print(f"Warning: No CoNLL output for sentence {sent_id}")
                outfile.write(conll_output + "\n\n")

    print(f"CoNLL file saved at: {output_file}")
