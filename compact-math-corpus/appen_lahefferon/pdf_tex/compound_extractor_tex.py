import time
import re
from collections import defaultdict
from tqdm import tqdm

def extract_compounds_ud(conll_file, compounds_file, compounds_list_file):
    start_time = time.time()
    compounds = defaultdict(int)

    with open(conll_file, "r", encoding="utf-8") as f:
        total_lines = sum(1 for _ in f)

    with open(conll_file, "r", encoding="utf-8") as infile:
        sentences = []
        current_sentence = []

        for line in tqdm(infile, desc="Reading and grouping sentences", total=total_lines):
            line = line.strip()
            if not line or line.startswith("#"):
                if current_sentence:
                    sentences.append(current_sentence)
                    current_sentence = []
                continue

            parts = line.split("\t")
            if len(parts) < 8:
                continue

            token_id = int(parts[0])
            token = parts[2].lower()
            pos = parts[3]
            head_id = int(parts[6])
            dep_rel = parts[7]

            current_sentence.append({
                "id": token_id,
                "token": token,
                "pos": pos,
                "head_id": head_id,
                "dep_rel": dep_rel
            })

    for sentence in tqdm(sentences, desc="Analyzing compounds by UD 'compound'"):
        id2token = {tok["id"]: tok for tok in sentence}
        for tok in sentence:
            if tok["dep_rel"] == "compound":
                head_token = id2token.get(tok["head_id"])
                if head_token:
                    compound_phrase = f"{tok['token']} {head_token['token']}"
                    compounds[compound_phrase] += 1

    with open(compounds_file, "w", encoding="utf-8") as outfile:
        for compound, count in sorted(compounds.items(), key=lambda item: item[1], reverse=True):
            outfile.write(f"{compound}\t{count}\n")

    with open(compounds_list_file, "w", encoding="utf-8") as outlist:
        for compound in sorted(compounds):
            outlist.write(f"{compound}\n")

    print(f"Saved: {compounds_file}")
    print(f"Saved: {compounds_list_file}")
