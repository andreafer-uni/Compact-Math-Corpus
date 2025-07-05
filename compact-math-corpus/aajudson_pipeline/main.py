from scripts.cleaning.clean_sentences import run as clean
from scripts.stats.generate_stats_summary import run as stats_summary 
from scripts.stats.generate_full_stats import run as stats_json 
from scripts.annotation.extract_spacy_features import run as extract_features 
from scripts.annotation.generate_conll import run as generate_conll
from scripts.annotation.check_anomalous_tokens import run as check_tokens
from scripts.extract.extract_compounds import run as extract_compounds


def main():
    print("Starting pipeline...")
    clean()
    stats_summary()
    stats_json()
    extract_features()
    generate_conll()
    check_tokens()
    extract_compounds()
    print("Pipeline complete.")

if __name__ == '__main__':
    main()
