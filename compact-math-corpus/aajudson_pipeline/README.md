# Abstract Algebra PDF Pipeline

This repository processes the **[Abstract Algebra: Theory and Applications (Thomas W. Judson)](https://github.com/twjudson/aata)** textbook from a raw PDF converted with fitz#PyMuPDF into a cleaned, annotated corpus using spaCy and Universal Dependencies.

## Components

- **Cleaning**: Removes noisy or invalid sentences and non-ASCII characters.
- **Annotation**: Annotates with spaCy, extracting features and saving in CoNLL and TSV.
- **Stats**: Generates summary CSV and full linguistic JSON statistics.
- **Compounds**: Extracts compound dependencies from CoNLL output.

## Directory Structure

```
aajudson_pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── data/
│   ├── raw/                  # Original JSON (PDF converted)
│   ├── intermediate/         # Cleaned JSON
│   ├── processed/            # CoNLL, TSV, etc.
│   └── output/               # Statistics and compound lists
├── scripts/
│   ├── cleaning/
│   │   └── clean_sentences.py
│   ├── annotation/
│   │   ├── generate_conll.py
│   │   ├── extract_spacy_features.py
│   │   ├── check_anomalous_tokens.py
│   │   └── extract_compounds.py
│   └── stats/
│       ├── generate_summary_csv.py
│       └── generate_full_stats_json.py
```

## Run the Pipeline

```bash
python main.py
```
