# Linear Algebra Appendix NLP

This project processes and analyzes the appendix of the book [Linear Algebra (Jim Hefferon)](https://hefferon.net/linearalgebra/) using spaCy and Universal Dependencies. 
It was used for comparing PDF and TeX, as well as spaCy Small and Transformer models.

## Features

- Cleans and filters JSON-formatted sentences
- Extracts CoNLL-format files with syntactic annotations
- Generates summary statistics (CSV/JSON)
- Extracts compound expressions via UD and TF-IDF

## Structure

- `text_processing.py` — extract and clean the appendix
- `stats_generator.py` — compute linguistic statistics
- `conll_converter.py` — convert to CoNLL format
- `compound_extractor.py` — extract compound phrases
- `token_checker.py` — find anomalous tokens
- `main.py` — handles the full workflow

## Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage

```bash
python main.py
```

## Notes

- Place your input file `lahefferon-processed.json` in the `data/` directory.
- Outputs are saved in `outputs/`.
