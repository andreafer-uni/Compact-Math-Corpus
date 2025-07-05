import json
import spacy
from tqdm import tqdm
from spacy_conll import ConllFormatter

def convert_to_conll(json_path, conll_out):
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("conll_formatter", last=True)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f).get("sentences", [])

    with open(conll_out, "w", encoding="utf-8") as out:
        for doc_id, text in enumerate(tqdm(data, desc="Generating CoNLL"), 1):
            doc = nlp(text)
            out.write(f"# doc_id = {doc_id}\n")
            for i, sent in enumerate(doc.sents, 1):
                out.write(f"# sent_id = {i}\n# text = {sent.text}\n{sent._.conll_str.strip()}\n\n")
