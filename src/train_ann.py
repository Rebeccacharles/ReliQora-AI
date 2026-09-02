import pandas as pd
import tensorflow as tf

from pathlib import Path
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    average_precision_score
)


# Reproducibility
tf.random.set_seed(42)


# Paths
PROCESSED_DIR = Path("data/processed")
MODELS_DIR = Path("models")

MODELS_DIR.mkdir(parents=True, exist_ok=True)


# Load processed data
X_train = pd.read_csv(PROCESSED_DIR / "X_train.csv")
X_test = pd.read_csv(PROCESSED_DIR / "X_test.csv")

y_train = pd.read_csv(PROCESSED_DIR / "y_train.csv").squeeze()
y_test = pd.read_csv(PROCESSED_DIR / "y_test.csv").squeeze()


# Build ANN
model = tf.keras.Sequential([
    tf.keras.Input(shape=(8,)),

    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dropout(0.30),

    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dropout(0.20),

    tf.keras.layers.Dense(1, activation="sigmoid")
])


# Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# Display architecture
print("\n===== ANN Architecture =====")
model.summary()


# Train model
print("\n===== Training ANN =====")

history = model.fit(
    X_train,
    y_train,
    validation_split=0.20,
    epochs=30,
    batch_size=32,
    verbose=1
)


# Predict probabilities
y_probability = model.predict(
    X_test,
    verbose=0
).ravel()

# Convert probabilities to class predictions
y_pred = (y_probability >= 0.5).astype(int)


# Evaluation
print("\n===== ANN Results =====")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

pr_auc = average_precision_score(y_test, y_probability)

print(f"\nPR-AUC: {pr_auc:.4f}")


# Save model
model_path = MODELS_DIR / "ann_model.keras"

model.save(model_path)

print(f"\nANN model saved to: {model_path}")