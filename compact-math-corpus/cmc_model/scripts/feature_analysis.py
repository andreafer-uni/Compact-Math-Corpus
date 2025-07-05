
import pandas as pd
import matplotlib.pyplot as plt

def plot_feature_weights(model, vectorizer, top_n=10):
    feature_names = vectorizer.get_feature_names_out()
    weights = model.coef_[0]

    weights_df = pd.DataFrame({
        "feature": feature_names,
        "weight": weights
    }).sort_values(by="weight", ascending=False)

    top_math = weights_df.head(top_n)
    top_non_math = weights_df.tail(top_n).sort_values(by="weight")

    plt.figure(figsize=(10, 6))
    plt.barh(top_non_math["feature"], top_non_math["weight"], color="orange", label="Non-Math")
    plt.barh(top_math["feature"], top_math["weight"], color="blue", label="Math")
    plt.axvline(0, color="black", linewidth=0.8)
    plt.title("Most Influential Features")
    plt.xlabel("Weight")
    plt.ylabel("Feature")
    plt.legend()
    plt.tight_layout()
    plt.savefig("important_features_weights.pdf", format="pdf")
    plt.show()
