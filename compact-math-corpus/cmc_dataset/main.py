from tfidf_extractor import extract_compounds_tfidf
from bigrams_comparator import compare_bigrams
from math_concept_annotator import annotate_math_concepts
import pandas as pd
import os

def create_subset(input_file, output_file, n=1620):
    df = pd.read_csv(input_file, sep='\t')
    df["is-math-concept"] = 0
    df.head(n).to_csv(output_file, sep='\t', index=False)
    print(f"Subset saved: {output_file}")

def map_bigrams_to_sentences(bigrams_path, conll_path, output_path):
    df_bigrams = pd.read_csv(bigrams_path, sep="\t")
    with open(conll_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    sentences, current_sentence = [], []
    for line in lines:
        if line.strip() == "":
            if current_sentence:
                sentences.append(" ".join(current_sentence))
                current_sentence = []
        else:
            parts = line.strip().split("\t")
            if len(parts) > 0:
                current_sentence.append(parts[0])
    if current_sentence:
        sentences.append(" ".join(current_sentence))

    df_bigrams["sentence"] = df_bigrams["bigram"].apply(
        lambda b: next((s for s in sentences if b in s), "")
    )
    df_bigrams.to_csv(output_path, sep="\t", index=False)
    print(f"Mapped: {output_path}")

def main():
    os.makedirs("outputs", exist_ok=True)

    # Step 1: Extract TF-IDF bigrams from EWT
    extract_compounds_tfidf("data/ewtud-train.conllu", "outputs/ewtud-tfidf.tsv")

    # Step 2: Compare bigrams with math corpus
    compare_bigrams(
        "data/cmcorpus-tfidf.tsv",
        "outputs/ewtud-tfidf.tsv",
        "outputs/bigrams-common.tsv",
        "outputs/bigrams-math-only.tsv",
        "outputs/bigrams-ewt-only.tsv"
    )

    # Step 3: Annotate math-only bigrams
    annotate_math_concepts(
        "outputs/bigrams-math-only.tsv",
        "outputs/bigrams-math-annotated.tsv",
        "outputs/bigrams-math-concepts.tsv"
    )

    # Step 4: Create non-math sample from EWT
    create_subset("outputs/bigrams-ewt-only.tsv", "outputs/bigrams-ewt-only-1620.tsv")

    # Step 5: Map bigrams to sentences
    map_bigrams_to_sentences("outputs/bigrams-ewt-only-1620.tsv", "data/ewtud-train.conllu", "outputs/ewt-data.tsv")
    map_bigrams_to_sentences("outputs/bigrams-math-concepts.tsv", "data/cmcorpus.conll", "outputs/math-concepts.tsv")

    # Step 6: Concatenate
    df1 = pd.read_csv("outputs/ewt-data.tsv", sep="\t")
    df2 = pd.read_csv("outputs/math-concepts.tsv", sep="\t")
    df_combined = pd.concat([df1, df2])
    df_combined.to_csv("outputs/cmc-dataset.tsv", sep="\t", index=False)
    print("Final dataset: outputs/cmc-dataset.tsv")

if __name__ == "__main__":
    main()
