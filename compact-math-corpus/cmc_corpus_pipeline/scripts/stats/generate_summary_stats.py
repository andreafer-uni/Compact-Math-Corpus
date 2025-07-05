import json
import spacy
import pandas as pd
from collections import Counter

def generate_summary_stats(json_path, csv_output):
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    nlp.add_pipe("sentencizer")

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    text = " ".join(data.get("sentences", []))
    doc = nlp(text)

    stats = {
        "Total Tokens": len(doc),
        "Total Sentences": len(list(doc.sents)),
        "Unique Words": len(set(t.text.lower() for t in doc if t.is_alpha)),
        "Average Sentence Length": len(doc) / len(list(doc.sents)) if doc else 0,
        "Average Word Length": sum(len(t.text) for t in doc if t.is_alpha) / max(len([t for t in doc if t.is_alpha]), 1),
        "POS Frequencies": dict(Counter(t.pos_ for t in doc)),
        "Top Informative Terms": Counter([
            t.text.lower() for t in doc if t.is_alpha and not t.is_stop and t.pos_ in {"NOUN", "VERB", "ADJ", "ADV"}
        ]).most_common(20)
    }

    df = pd.DataFrame(stats.items(), columns=["Metric", "Value"])
    df.to_csv(csv_output, index=False)
