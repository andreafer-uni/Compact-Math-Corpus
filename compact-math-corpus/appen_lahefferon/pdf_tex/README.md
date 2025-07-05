# TEX vs. PDF Comparison

This project analyzes and compares compound terms extracted from PDF and LaTeX versions of a textbook appendix (e.g., Jim Hefferon's Linear Algebra).

## Modules

- `conll_converter_tex.py` — Converts LaTeX JSON into CoNLL format
- `compound_analysis.py` — Identifies anomalously long tokens in CoNLL files
- `compound_extractor_tex.py` — Extracts compound terms based on dependency relations
- `compound_comparator.py` — Compares compound lists from TEX and PDF
- `main.py` — Executes the full pipeline

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

- Ensure the following input files are in the `data/` folder:
  - `texappen-lahefferon-processed.json`
  - `pdfappen-lahefferon-compoundsud-list.txt`
- Output files will be saved in the `outputs/` folder.


## Output Files

The following output files will be generated in the `outputs/` folder:

- `texappen-lahefferon.conll` — CoNLL representation of the LaTeX appendix
- `texappen-lahefferon-compoundsud.tsv` — Compound terms extracted with frequencies
- `texappen-lahefferon-compoundsud-list.txt` — List of unique compound terms (no frequency)
- `overlap-compounds.pdf` — Venn diagram showing overlap between TEX and PDF compound terms
