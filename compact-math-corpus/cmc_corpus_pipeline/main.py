from scripts.ingestion.concat_json import run as concat_json
from scripts.ingestion.clean_sentences import run as clean_sentences
from scripts.annotation.generate_conll import run as generate_conll
from scripts.annotation.extract_spacy_features import run as extract_features
from scripts.annotation.check_anomalous_tokens import run as check_tokens
from scripts.annotation.extract_compounds import run as extract_compounds
from scripts.stats.generate_summary_stats import run as generate_summary
from scripts.stats.generate_full_stats import run as generate_stats
from scripts.tfidf.extract_tfidf_before_conll import run as tfidf_scores_noconll
from scripts.tfidf.extract_tfidf_after_conll import run as tfidf_scores_conll

def main():
    print("=== Starting Math Corpus Pipeline ===")
    concat_json()
    clean_sentences()
    generate_conll()
    extract_features()
    check_tokens()
    extract_compounds()
    generate_summary()
    generate_stats_json()
    tfidf_scores_noconll()
    tfidf_scores_conll()
    print("=== Pipeline Completed ===")

if __name__ == "__main__":
    main()
