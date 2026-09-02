import pandas as pd
import joblib

from pathlib import Path
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    average_precision_score
)


# Paths
PROCESSED_DIR = Path("data/processed")
MODELS_DIR = Path("models")

MODELS_DIR.mkdir(parents=True, exist_ok=True)


# Load processed data
X_train = pd.read_csv(PROCESSED_DIR / "X_train.csv")
X_test = pd.read_csv(PROCESSED_DIR / "X_test.csv")

y_train = pd.read_csv(PROCESSED_DIR / "y_train.csv").squeeze()
y_test = pd.read_csv(PROCESSED_DIR / "y_test.csv").squeeze()


# Models
models = {
    "Decision Tree": DecisionTreeClassifier(
        max_depth=8,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
}


# Train and evaluate
for name, model in models.items():

    print(f"\n{'=' * 50}")
    print(f"{name} Results")
    print(f"{'=' * 50}")

    # Train
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    y_probability = model.predict_proba(X_test)[:, 1]

    # Classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion matrix
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # PR-AUC
    pr_auc = average_precision_score(y_test, y_probability)
    print(f"\nPR-AUC: {pr_auc:.4f}")

    # Save model
    filename = name.lower().replace(" ", "_") + ".pkl"
    model_path = MODELS_DIR / filename

    joblib.dump(model, model_path)

    print(f"Model saved to: {model_path}")