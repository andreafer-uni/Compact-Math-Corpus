import math
import time
from collections import defaultdict, Counter
from tqdm import tqdm

def extract_compounds_tfidf(conll_file, output_file):
    start_time = time.time()
    sentence_bigrams = []
    bigram_df = defaultdict(int)

    with open(conll_file, "r", encoding="utf-8") as f:
        total_lines = sum(1 for _ in f)

    with open(conll_file, "r", encoding="utf-8") as infile:
        current_sentence = []
        for line in tqdm(infile, desc="Reading and grouping sentences", total=total_lines):
            line = line.strip()
            if not line or line.startswith("#"):
                if current_sentence:
                    bigrams = []
                    for i in range(len(current_sentence) - 1):
                        token1, pos1, _ = current_sentence[i]
                        token2, pos2, _ = current_sentence[i + 1]
                        if (pos1 == "NOUN" and pos2 == "NOUN") or (pos1 == "ADJ" and pos2 == "NOUN"):
                            bigram = f"{token1} {token2}"
                            bigrams.append(bigram)
                    sentence_bigrams.append(bigrams)
                    for bigram in set(bigrams):
                        bigram_df[bigram] += 1
                    current_sentence = []
                continue
            parts = line.split("\t")
            if len(parts) < 8:
                continue
            token = parts[2].lower()
            pos = parts[3]
            dep_rel = parts[7]
            current_sentence.append((token, pos, dep_rel))

    total_sentences = len(sentence_bigrams)
    bigram_tfidf = defaultdict(float)
    for bigrams in sentence_bigrams:
        tf_counter = Counter(bigrams)
        for bigram, tf in tf_counter.items():
            df = bigram_df[bigram]
            idf = math.log(total_sentences / (1 + df))
            tfidf = tf * idf
            bigram_tfidf[bigram] += tfidf

    sorted_bigrams = sorted(bigram_tfidf.items(), key=lambda x: x[1], reverse=True)
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("Bigram\tTF-IDF Weight\n")
        for bigram, tfidf in sorted_bigrams:
            outfile.write(f"{bigram}\t{tfidf:.2f}\n")

    print("\nTop 10 bigrams by TF-IDF:")
    for bigram, tfidf in sorted_bigrams[:10]:
        print(f"{bigram}\t{tfidf:.2f}")
    print(f"\nTotal unique bigrams found: {len(bigram_tfidf)}")
    print(f"Generated file: {output_file}")
    print(f"Total time: {time.time() - start_time:.2f} seconds")
