import pandas as pd

def annotate_math_concepts(input_file, output_annotated, output_concepts):
    df = pd.read_csv(input_file, sep='\t')
    df = df[df["bigram"] != "bigram"].reset_index(drop=True)

    math_keywords = [
        "matrix", "function", "formula", "graph", "term", "degree", "algebraic", "index", "logic",
        "map", "ring", "measure", "determinant", "angle", "component", "explicit", "foundation",
        "proof", "analysis", "science", "column", "row", "symmetric", "linear", "factor", "value",
        "vector", "theorem", "equation", "expression", "integral", "derivative", "sum", "series",
        "limit", "zero", "identity", "modulo", "integer", "rational", "real", "complex", "number"
    ]

    def is_math_concept(bigram):
        return int(any(word in bigram.lower() for word in math_keywords))

    df["is-math-concept"] = df["bigram"].apply(is_math_concept)
    df.to_csv(output_annotated, sep='\t', index=False)

    df_math = df[df["is-math-concept"] == 1].reset_index(drop=True)
    df_math.to_csv(output_concepts, sep='\t', index=False)

    print(f"Annotated: {len(df)}, Math Concepts: {len(df_math)}")
