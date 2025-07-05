# CMC Model 

This repository contains a complete pipeline for identifying mathematical concepts in bigrams using a labeled dataset.

## Components

- **load_and_clean.py**: Loads the TSV dataset, handles missing values, and prepares input features.
- **evaluate_model.py**: Trains a logistic regression model and evaluates it on test data, showing errors and confusion matrix.
- **cross_validation.py**: Performs 10-fold stratified cross-validation and exports detailed reports and plots.
- **feature_analysis.py**: Visualizes the most influential features using logistic regression weights.


## Outputs

- `logistic_model.pkl`, `tfidf_vectorizer.pkl`
- `confusion_matrix.pdf`, `important_features_weights.pdf`
- `fold_summary_metrics.csv`, `full_classification_report.csv`, `summary_metrics.csv`

## Directory Structure

```
cmc-model-pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── data/
│   └── cmc-dataset.tsv           
├── outputs/ 
│   ├── logistic_model.pkl 
│   ├── tfidf_vectorizer.pkl
│   ├── confusion_matrix.pdf
│   ├── important_features_weights.pdf
│   ├── full_classification_report.csv 
│   ├── fold_summary_metrics.csv
│   └── summary_metrics.csv
├── scripts/
│   ├── __init__.py
│   ├── load_and_clean.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── cross_validation.py
│   └── feature_analysis.py
```


## How to run

```bash
python main.py
```

