from scripts import load_and_clean, train_model, evaluate_model, cross_validation, feature_analysis

if __name__ == "__main__":
    # 1. Load and clean data
    df, X, y, vectorizer = load_and_clean.run()

    # 2. Train model (save model + vectorizer)
    model = train_model.run(X, y, vectorizer)

    # 3. Evaluate model
    evaluate_model.run(X, y, vectorizer, model)

    # 4. Cross-validation
    cross_validation.run(df)

    # 5. Feature importance plot
    feature_analysis.run(vectorizer, model)
