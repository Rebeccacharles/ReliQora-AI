import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Paths
DATA_PATH = Path("data/raw/telemetry_data.csv")
PROCESSED_DIR = Path("data/processed")
MODELS_DIR = Path("models")

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)


# Load dataset
df = pd.read_csv(DATA_PATH)

print(f"Dataset loaded: {df.shape}")


# Separate features and target
X = df.drop("failure", axis=1)
y = df["failure"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Feature scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Save processed datasets
pd.DataFrame(
    X_train_scaled,
    columns=X.columns
).to_csv(
    PROCESSED_DIR / "X_train.csv",
    index=False
)

pd.DataFrame(
    X_test_scaled,
    columns=X.columns
).to_csv(
    PROCESSED_DIR / "X_test.csv",
    index=False
)

y_train.to_csv(
    PROCESSED_DIR / "y_train.csv",
    index=False
)

y_test.to_csv(
    PROCESSED_DIR / "y_test.csv",
    index=False
)


# Save scaler
joblib.dump(
    scaler,
    MODELS_DIR / "scaler.pkl"
)


# Display summary
print("\nPreprocessing completed successfully!")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print(f"Features: {X.shape[1]}")
print(f"Scaler saved to: {MODELS_DIR / 'scaler.pkl'}")