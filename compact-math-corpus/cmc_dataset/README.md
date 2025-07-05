# CMC Dataset Construction

This repository builds a CMC (Compound Multiword Classifier) dataset by extracting and comparing bigrams from two sources:
- Universal Dependencies English Web Treebank (EWT)
- A mathematical corpus (LaTeX-based)

## Features

- Extracts ADJ-NOUN and NOUN-NOUN bigrams from `.conll` files
- Calculates TF-IDF per sentence
- Compares bigrams between domains
- Annotates math-related bigrams
- Maps bigrams back to sentences
- Creates balanced classification dataset

## Folder Structure

```
cmc-dataset/
├── data/
│   ├── ewtud-train.conllu
│   ├── cmcorpus.conll
│   └── cmcorpus-tfidf.tsv
├── outputs/
│   ├── ewtud-tfidf.tsv
│   ├── bigrams-*.tsv
│   └── cmc-dataset.tsv
├── tfidf_extractor.py
├── bigrams_comparator.py
├── math_concept_annotator.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Output

Final dataset will be saved to:

```
outputs/cmc-dataset.tsv
```

Each row contains:

- `bigram` — bigram term
- `score` — TF-IDF score
- `is-math-concept` — label (1 or 0)
- `sentence` — sentence containing the bigram
