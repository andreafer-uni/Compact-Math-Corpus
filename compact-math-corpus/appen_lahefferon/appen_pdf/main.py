# main.py
from text_processing import extract_and_clean_json
from stats_generator import generate_statistics
from conll_converter import convert_to_conll
from compound_extractor import extract_bigrams
from token_checker import check_long_tokens

def main():
    input_file = "lahefferon-processed.json"
    cleaned_json_path = "pdfappen-lahefferon.json"
    stats_csv_path = "pdfappen-lahefferon-stats-summary.csv"
    stats_json_path = "pdfappen-lahefferon-stats.json"
    conll_output_path = "pdfappen-lahefferon.conll"
    compounds_ud_path = "pdfappen-lahefferon-compoundsud.tsv"
    compounds_list_path = "pdfappen-lahefferon-compoundsud-list.txt"
    compounds_tfidf_path = "pdfappen-lahefferon-tfidf.tsv"

    print("Extracting and cleaning sentences...")
    extract_and_clean_json(input_file, cleaned_json_path, 9706, 9956)

    print("Generating statistics...")
    generate_statistics(cleaned_json_path, stats_csv_path, stats_json_path)

    print("Converting to CoNLL format...")
    convert_to_conll(cleaned_json_path, conll_output_path)

    print("Checking for long tokens...")
    long_tokens = check_long_tokens(conll_output_path)
    print("Examples:", long_tokens)

    print("Extracting compounds using UD method...")
    extract_bigrams(conll_output_path, compounds_ud_path, mode="ud", list_out_path=compounds_list_path)

    print("Extracting compounds using TF-IDF method...")
    extract_bigrams(conll_output_path, compounds_tfidf_path, mode="tfidf")

if __name__ == "__main__":
    main()
