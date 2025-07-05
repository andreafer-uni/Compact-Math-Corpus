
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold

def run_cross_validation(df):
    X = df["input"].values
    y = df["is_math_concept"].values

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
    X_vec = vectorizer.fit_transform(X)

    kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
    results = []
    reports = []

    for fold, (train_idx, test_idx) in enumerate(kf.split(X_vec, y), start=1):
        X_train, X_test = X_vec[train_idx], X_vec[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        report_dict = classification_report(y_test, y_pred, output_dict=True, digits=3)
        report_df = pd.DataFrame(report_dict).transpose()
        report_df["fold"] = fold
        reports.append(report_df)

        results.append({
            "fold": fold,
            "accuracy": report_dict["accuracy"],
            "precision_0": report_dict["0"]["precision"],
            "recall_0": report_dict["0"]["recall"],
            "f1_0": report_dict["0"]["f1-score"],
            "precision_1": report_dict["1"]["precision"],
            "recall_1": report_dict["1"]["recall"],
            "f1_1": report_dict["1"]["f1-score"],
            "macro_f1": report_dict["macro avg"]["f1-score"]
        })

    results_df = pd.DataFrame(results)
    full_report_df = pd.concat(reports, axis=0).reset_index().rename(columns={"index": "metric"})

    results_df.to_csv("fold_summary_metrics.csv", index=False)
    full_report_df.to_csv("full_classification_report.csv", index=False)

    # Plot F1 scores
    plt.figure(figsize=(12, 6))
    plt.plot(results_df["fold"], results_df["f1_1"], marker="o", label="F1 (math concept)")
    plt.plot(results_df["fold"], results_df["f1_0"], marker="s", label="F1 (non-concept)")
    plt.plot(results_df["fold"], results_df["macro_f1"], marker="^", label="F1 Macro")
    plt.title("F1-Score per Fold")
    plt.xlabel("Fold")
    plt.ylabel("F1-Score")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("f1_scores_per_fold.pdf")
    plt.show()

    return results_df
