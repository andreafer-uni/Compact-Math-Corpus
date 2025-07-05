from conll_converter_tex import process_json_to_conll
from compound_analysis import count_long_tokens
from compound_extractor_tex import extract_compounds_ud
from compound_comparator import compare_lists
from pprint import pprint

def main():
    json_path = "data/texappen-lahefferon-processed.json"
    conll_path = "outputs/texappen-lahefferon.conll"
    compounds_tsv = "outputs/texappen-lahefferon-compoundsud.tsv"
    compounds_txt = "outputs/texappen-lahefferon-compoundsud-list.txt"
    pdf_txt = "data/pdfappen-lahefferon-compoundsud-list.txt"

    print("Converting TEX JSON to CoNLL...")
    process_json_to_conll(json_path, conll_path)

    print("Analyzing long tokens...")
    num_long, examples = count_long_tokens(conll_path)
    print(f"Found {num_long} long tokens. Examples:")
    pprint(examples[:10])

    print("Extracting compounds from CoNLL...")
    extract_compounds_ud(conll_path, compounds_tsv, compounds_txt)

    print("Comparing TEX and PDF compound lists...")
    results = compare_lists(compounds_txt, pdf_txt)
    pprint(results)

if __name__ == "__main__":
    main()
