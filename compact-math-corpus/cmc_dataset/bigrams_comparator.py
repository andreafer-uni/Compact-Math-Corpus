import pandas as pd

def compare_bigrams(math_path, ewt_path, out_common, out_math_only, out_ewt_only):
    ewt_df = pd.read_csv(ewt_path, sep="\t", header=None, names=["bigram", "score"])
    math_df = pd.read_csv(math_path, sep="\t", header=None, names=["bigram", "score"])

    common_df = pd.merge(math_df, ewt_df, on="bigram", suffixes=("-math", "-ewt"))
    math_only_df = math_df[~math_df["bigram"].isin(ewt_df["bigram"])]
    ewt_only_df = ewt_df[~ewt_df["bigram"].isin(math_df["bigram"])]

    common_df.to_csv(out_common, sep="\t", index=False)
    math_only_df.to_csv(out_math_only, sep="\t", index=False)
    ewt_only_df.to_csv(out_ewt_only, sep="\t", index=False)

    print(f"Total bigrams in common: {len(common_df)}")
    print(f"Math only: {len(math_only_df)}")
    print(f"EWT only: {len(ewt_only_df)}")
