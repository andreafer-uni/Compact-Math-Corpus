# spaCy Transformer (TRF) vs Small Model Comparison

This project analyzes and compares linguistic statistics using spaCy's `en_core_web_trf` (Transformer) and `en_core_web_sm` (Small) models on tokenized text from scientific PDFs.

## Features

- Computes summary and detailed linguistic statistics using `en_core_web_trf`
- Outputs data to CSV and JSON for analysis and comparison
- Enables radar plot comparisons between transformer-based and small models

## File Structure

- `trf_stats_summary.py` — Generates CSV summary stats
- `trf_detailed_stats.py` — Generates detailed JSON stats
- `main.py` — Runs the full process

## Setup

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_trf
```

## Usage

```bash
python main.py
```

## Output Files

- Output files are saved in the `outputs/` directory.
