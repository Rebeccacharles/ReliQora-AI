import pandas as pd
import joblib

from pathlib import Path
from sklearn.linear_model import LogisticRegression
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


# Create Logistic Regression model
model = LogisticRegression(
    random_state=42,
    max_iter=1000
)


# Train model
model.fit(X_train, y_train)


# Predictions
y_pred = model.predict(X_test)
y_probability = model.predict_proba(X_test)[:, 1]


# Evaluation
print("\n===== Logistic Regression Results =====")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

pr_auc = average_precision_score(y_test, y_probability)

print(f"\nPR-AUC: {pr_auc:.4f}")


# Save model
model_path = MODELS_DIR / "logistic_regression.pkl"

joblib.dump(model, model_path)

print(f"\nModel saved to: {model_path}")