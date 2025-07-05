
import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path, sep="\t")
    df = df.dropna(subset=["bigram", "sentence", "is_math_concept"])
    df["input"] = df["bigram"] + " | " + df["sentence"]
    return df
