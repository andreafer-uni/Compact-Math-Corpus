import json
import spacy
from collections import Counter, defaultdict
from datetime import datetime
import time
from tqdm import tqdm

def generate_trf_detailed(json_path, output_path, page_count=525):
    nlp = spacy.load("en_core_web_trf")
    start_time = time.time()

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    sentences = data.get("sentences", [])
    doc = nlp(" ".join(sentences))

    num_tokens = len(doc)
    num_sentences = len(list(doc.sents))
    num_unique_lemmas = len(set(token.lemma_.lower() for token in doc if token.is_alpha))
    sentence_lengths = Counter(len(sent) for sent in doc.sents)
    sorted_sentence_lengths = dict(sorted(sentence_lengths.items()))
    pos_counts = Counter(token.pos_ for token in doc)
    dep_counts = Counter(token.dep_ for token in doc)
    tag_counts = Counter(token.tag_ for token in doc)

    pos_stats = {
        pos: Counter(token.text.lower() for token in doc if token.pos_ == pos).most_common(50)
        for pos in tqdm(pos_counts, desc="Processing POS tags")
    }
    tag_stats = {
        tag: Counter(token.text.lower() for token in doc if token.tag_ == tag).most_common(50)
        for tag in tqdm(tag_counts, desc="Processing morphological tags")
    }

    dep_stats = defaultdict(Counter)
    for token in tqdm(doc, desc="Processing dependencies"):
        if token.dep_ in dep_counts:
            phrase = f"{token.head.text.lower()} {token.text.lower()}"
            dep_stats[token.dep_][phrase] += 1
    dep_stats = {dep: dict(dep_stats[dep].most_common(50)) for dep in dep_counts}

    compound_count = sum(1 for token in doc if token.dep_ == "compound")

    stats = {
        "spacy_version": spacy.__version__,
        "spacy_model": "en_core_web_trf",
        "date": datetime.now().isoformat(),
        "corpus": "trflinearalgebra-pdf",
        "documents/pages": page_count,
        "sentences": num_sentences,
        "sentence_lengths": sorted_sentence_lengths,
        "tokens": num_tokens,
        "lemmas": num_unique_lemmas,
        "pos": dict(pos_counts),
        "tag": dict(tag_counts),
        "deps": dict(dep_counts),
        "compounds": compound_count,
        "pos_stats": {pos: dict(words) for pos, words in pos_stats.items()},
        "tag_stats": {tag: dict(words) for tag, words in tag_stats.items()},
        "dep_stats": dep_stats,
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4, ensure_ascii=False)

    print(f"Statistics saved in: {output_path}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
