
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_and_save_model(df, model_path="logistic_model.pkl", vectorizer_path="tfidf_vectorizer.pkl"):
    X = df["input"]
    y = df["is_math_concept"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)

    return model, vectorizer, X_train, X_test, y_train, y_test
