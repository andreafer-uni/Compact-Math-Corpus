# Math Corpus Pipeline

This corpus is Concatenation of three books:
* [Linear Algebra (Jim Hefferon)](https://hefferon.net/linearalgebra/). 
* [Abstract Algebra: Theory and Applications (Thomas W. Judson)](https://github.com/twjudson/aata).
* [Discrete Mathematics (Oscar Levin)](https://discrete.openmathbooks.org/pdfs/dmoi4.pdf).

All these files are sourced in PDF format and converted to JSON
without any cleaning process, only conversion with fitz#PyMuPDF and spaCy sentencing.

This project builds a linguistically annotated corpus by processing open-access mathematics textbooks. It includes PDF/TEX ingestion, sentence cleaning, dependency parsing, compound extraction, and TF-IDF scoring.

## Components

- **Ingestion**: Converts PDF/TEX to cleaned sentence JSON.
- **Annotation**: Uses spaCy + UD to generate CoNLL and spaCy features.
- **Stats**: Produces corpus statistics in CSV and JSON.
- **TF-IDF**: Computes bigram scores before and after UD parsing.

## Directory Structure

```
math-corpus-pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── data/
│   ├── raw/  
│   │   ├── lahefferon.pdf
│   │   ├── aajudson.pdf
│   │   └── dmlevin.pdf            
│   ├── intermediate/
│   │   ├── lahefferon-processed.json
│   │   ├── aajudson-processed.json
│   │   ├── dmlevin-processed.json
│   │   ├── cmcorpus-concat.json
│   │   └── cmcorpus.json        
│   ├── processed/
│   │   ├── cmcorpus.conll
│   │ 	└── cmcorpus-spacyfeatures.tsv  
│   └── output/ 
│       ├── cmcorpus-stats.json
│  	├── cmcorpus-stats-summmary.csv
│  	├── cmcorpus-compounds.tsv
│  	├── cmcorpus-tfidf.tsv
│       └── cmcorpus-tfidf-before-conll.tsv
├── scripts/
│   ├── ingestion/
│   │   ├── concat_json.py
│   │   └── clean_sentences.py
│   ├── annotation/
│   │   ├── generate_conll.py
│   │   ├── extract_spacy_features.py
│   │   ├── check_anomalous_tokens.py
│   │   └── extract_compounds.py
│   ├── stats/
│   │   ├── generate_summary_csv.py
│   │   └── generate_full_stats_json.py
│   └── tfidf/
│       └── tfidf_extraction.py
```
## Run the pipeline

```bash
python main.py
```

