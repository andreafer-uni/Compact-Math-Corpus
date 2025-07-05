# compound_extractor.py
import re
import math
from collections import defaultdict, Counter
from tqdm import tqdm

def extract_bigrams(conll_path, out_path, mode="ud", list_out_path=None):
    bigram_data = defaultdict(int)
    sentence_bigrams = []
    with open(conll_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    sentences = []
    current = []

    for line in tqdm(lines, desc="Grouping sentences"):
        if line.startswith("#") or not line.strip():
            if current:
                sentences.append(current)
                current = []
            continue
        parts = line.strip().split("\t")
        if len(parts) >= 8:
            current.append((parts[2].lower(), parts[3], parts[7], int(parts[6])))

    if mode == "ud":
        for sent in sentences:
            tokens = {i+1: t for i, t in enumerate(sent)}
            for i, (tok, pos, dep, head) in enumerate(sent):
                if dep == "compound" and head in tokens:
                    phrase = f"{tok} {tokens[head][0]}"
                    bigram_data[phrase] += 1
    else:
        for sent in sentences:
            bigrams = []
            for i in range(len(sent) - 1):
                if ((sent[i][1], sent[i+1][1]) in [("ADJ", "NOUN"), ("NOUN", "NOUN")]):
                    bg = f"{sent[i][0]} {sent[i+1][0]}"
                    bigrams.append(bg)
            for bg in set(bigrams):
                bigram_data[bg] += 1
            sentence_bigrams.append(bigrams)

        total_docs = len(sentence_bigrams)
        tfidf_scores = defaultdict(float)
        for s_bgs in sentence_bigrams:
            tf = Counter(s_bgs)
            for bg, tf_val in tf.items():
                idf = math.log(total_docs / (1 + bigram_data[bg]))
                tfidf_scores[bg] += tf_val * idf
        bigram_data = tfidf_scores

    with open(out_path, "w", encoding="utf-8") as f:
        for bg, val in sorted(bigram_data.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{bg}\t{val:.2f}\n")

    # Optional: Save list of compounds (no frequency)
    if list_out_path and mode == "ud":
        with open(list_out_path, "w", encoding="utf-8") as f:
            for phrase in sorted(bigram_data):
                f.write(f"{phrase}\n")
