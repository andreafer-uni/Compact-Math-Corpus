import spacy
import json
import pandas as pd
from collections import Counter, defaultdict
from datetime import datetime

def generate_statistics(json_path, csv_out, json_out):
    nlp = spacy.load("en_core_web_sm")
    with open(json_path, "r", encoding="utf-8") as f:
        sentences = json.load(f).get("sentences", [])

    doc = nlp(" ".join(sentences))

    stats = {
        "Total Tokens": len(doc),
        "Total Sentences": len(list(doc.sents)),
        "Unique Words": len(set(t.text.lower() for t in doc if t.is_alpha)),
        "Average Sentence Length": len(doc) / max(len(list(doc.sents)), 1),
        "Average Word Length": sum(len(t.text) for t in doc if t.is_alpha) / max(len([t for t in doc if t.is_alpha]), 1),
        "POS Frequencies": dict(Counter(t.pos_ for t in doc)),
        "Dependency Frequencies": dict(Counter(t.dep_ for t in doc)),
        "Top Informative Terms": Counter([
            t.text.lower() for t in doc if t.is_alpha and not t.is_stop and t.pos_ in {"NOUN", "VERB", "ADJ", "ADV"}
        ]).most_common(20)
    }

    pd.DataFrame(stats.items(), columns=["Metric", "Value"]).to_csv(csv_out, index=False)

    full_stats = {
        **stats,
        "date": datetime.now().isoformat(),
        "pos_stats": {
            pos: dict(Counter(t.text.lower() for t in doc if t.pos_ == pos).most_common(50))
            for pos in set(t.pos_ for t in doc)
        },
        "tag_stats": {
            tag: dict(Counter(t.text.lower() for t in doc if t.tag_ == tag).most_common(50))
            for tag in set(t.tag_ for t in doc)
        },
        "dep_stats": {
            dep: dict(Counter(f"{t.head.text.lower()} {t.text.lower()}" for t in doc if t.dep_ == dep).most_common(50))
            for dep in set(t.dep_ for t in doc)
        },
        "compounds": sum(1 for t in doc if t.dep_ == "compound"),
        "spacy_version": spacy.__version__,
        "spacy_model": "en_core_web_sm"
    }

    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(full_stats, f, indent=4, ensure_ascii=False)
