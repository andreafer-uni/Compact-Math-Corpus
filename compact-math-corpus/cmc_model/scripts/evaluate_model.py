
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model(model, vectorizer, X_test, y_test, df):
    y_pred = model.predict(vectorizer.transform(X_test))

    print(classification_report(y_test, y_pred))

    test_df = df.loc[X_test.index].copy()
    test_df["true"] = y_test
    test_df["pred"] = y_pred

    errors = test_df[test_df["true"] != test_df["pred"]]
    print("Total number of errors:", len(errors))
    print(errors[["bigram", "sentence", "true", "pred"]])

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(4, 3))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=["Non-Math", "Math"],
                yticklabels=["Non-Math", "Math"],
                annot_kws={"size": 14})
    plt.title("Confusion Matrix", fontsize=14)
    plt.xlabel("Predicted Label", fontsize=12)
    plt.ylabel("True Label", fontsize=12)
    plt.tight_layout()
    plt.savefig("confusion_matrix.pdf", format="pdf")
    plt.show()
