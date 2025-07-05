
import csv
from collections import defaultdict
from tqdm import tqdm
import time 

def extract_compounds(conll_file, compounds_file):
    """Extract compounds from CoNLL file based on UD 'compound' dependencies."""
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
                continue  # Ignore malformed lines

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
                head_id = tok["head_id"]
                head_token = id2token.get(head_id)
                if head_token:
                    compound_phrase = f"{tok['token']} {head_token['token']}"
                    compounds[compound_phrase] += 1

    with open(compounds_file, "w", encoding="utf-8") as outfile:
        sorted_compounds = sorted(compounds.items(), key=lambda item: item[1], reverse=True)
        for compound, count in sorted_compounds:
            outfile.write(f"{compound}\t{count}\n")

    elapsed = time.time() - start_time
    print(f"Arquivo gerado: {compounds_file}")
    print(f"Tempo total: {elapsed:.2f} segundos")

if __name__ == "__main__":
    conll_path = "dmlevin.conll"
    compounds_tsv_path = "dmlevin-compounds.tsv"
    extract_compounds(conll_path, compounds_tsv_path)
