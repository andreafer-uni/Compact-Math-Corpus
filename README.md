# Compact Math Corpus

The **Compact Math Corpus (CMC)** is a modular and extensible pipeline designed to extract, clean, annotate, and analyze mathematical textbook content in PDF format. It aims to produce a linguistically annotated corpora for downstream NLP applications such as syntactic analysis, compound extraction, and language modeling.

This repository is based on the work presented in the paper _"Building a Compact Math Corpus."_ by Andréa Ferreira 
→ *[Link to paper IN PROGRESS]*

It supports multiple math textbooks and integrates multiple pipelines with output in formats such as CoNLL, CSV, JSON, TSV, and trained model artifacts.

---

## Components

Each major component is organized as a self-contained pipeline with its own `main.py`, allowing independent processing:

- `pdf_latex_to_json/` — converts raw PDFs and LaTeX sources into structured sentence-level JSON format.
- `cmc_corpus_pipeline/` — corpus-wide pipeline tools including TF-IDF scoring.
- `lahefferon_pipeline/`, `aajudson_pipeline/`, `dmlevin_pipeline/` — specific corpus pipelines for each book.
- `appen_lahefferon/` — spaCy TRF vs. small model evaluation and PDF vs. TeX comparison pipeline.
- `cmc_dataset/` — combined corpora ready for model training (cleaned + annotated).
- `cmc_model/` — trained model using the CMC dataset.

---

## Directory Structure

```bash
compact-math-corpus/
├── README.md                  
├── pdf_latex_to_json        
├── cmc_corpus_pipeline       
├── lahefferon_pipeline      
├── aajudson_pipeline         
├── dmlevin_pipeline         
├── appen_lahefferon         
├── cmc_dataset               
└── cmc_model                
```

---

## Usage

Each pipeline folder contains its own `main.py`, which orchestrates modular scripts in subfolders like `cleaning/`, `stats/`, `annotation/`, and `extract/`.

Example:
```bash
cd lahefferon_pipeline
python main.py
```
---

## Corpora Used

- [Linear Algebra (Jim Hefferon)](https://hefferon.net/linearalgebra/).
- [Abstract Algebra: Theory and Applications (Thomas W. Judson)](https://github.com/twjudson/aata).
- [Discrete Mathematics (Oscar Levin)](https://discrete.openmathbooks.org/pdfs/dmoi4.pdf).
- All processed from freely available PDFs, sentence-split, cleaned, and parsed with `spaCy`.

---

## Outputs

Each pipeline generates outputs such as:
- `*-cleaned.json` — sentence-level corpus
- `*-stats-summary.csv`, `*-stats.json` — corpus-level statistics
- `*-spacyfeatures.tsv`, `*.conll` — UD-based annotations
- `*-compounds.tsv`, `*-compoundsud-list.txt` — compound lists
- `*-tfidf.tsv` — ranked bigrams by TF-IDF
- `*-model.pkl` — trained classifier built from the processed corpus.

---

## Model Training

Final models are trained using the unified CMC dataset and include:
- Logistic Regression
- TF-IDF Vectorizer
- Performance Evaluation 
- Error Analysis and Interpretability

---

## Citation

If you use this corpus or pipeline, please cite:

> Building a Compact Math Corpus for Compound and Syntax Analysis  
> [Andrea Ferreira], 2025.  ##### BIBTEX IN PROGRESS

---

## Dependencies

- Python 3.10+
- `spaCy`, `spacy-conll`, `tqdm`, `pandas`
- `PyMuPDF` or `pdfminer` (for PDF extraction)
- `LaTeX2e` tools (for .tex parsing, optional)

See `requirements.txt` in each pipeline folder.

---

## Status

✅ Modular  
✅ Fully reproducible  
✅ Aligned with Universal Dependencies  
✅ Tested on multiple math textbooks  
✅ Model ready for downstream applications
