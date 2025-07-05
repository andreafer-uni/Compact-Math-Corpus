
import json
import spacy
import pandas as pd
from collections import Counter
import time

def generate_stats_summary(input_json_path, output_csv_path):
    start_time = time.time()
    nlp = spacy.load("en_core_web_sm")

    with open(input_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    sentences = data.get("sentences", [])
    if not sentences:
        print("No sentences found.")
        return

    full_text = " ".join(sentences)
    doc = nlp(full_text)

    num_tokens = len(doc)
    num_sentences = len(list(doc.sents))
    num_unique_words = len(set(token.text.lower() for token in doc if token.is_alpha))
    pos_counts = Counter(token.pos_ for token in doc)
    dep_counts = Counter(token.dep_ for token in doc)
    avg_sentence_length = num_tokens / num_sentences if num_sentences > 0 else 0
    word_lengths = [len(token.text) for token in doc if token.is_alpha]
    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    informative_terms = [
        token.text.lower()
        for token in doc
        if token.is_alpha and not token.is_stop and token.pos_ in {"NOUN", "VERB", "ADJ", "ADV"}
    ]
    informative_counts = Counter(informative_terms).most_common(20)

    stats = {
        "Total Tokens": num_tokens,
        "Total Sentences": num_sentences,
        "Unique Words": num_unique_words,
        "Average Sentence Length": avg_sentence_length,
        "Average Word Length": avg_word_length,
        "POS Frequencies": dict(pos_counts),
        "Dependency Frequencies": dict(dep_counts),
        "Top Informative Terms": informative_counts,
    }

    df_stats = pd.DataFrame(stats.items(), columns=["Metric", "Value"])
    df_stats.to_csv(output_csv_path, index=False, encoding="utf-8")

    print(f"Statistics saved in: {output_csv_path}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
