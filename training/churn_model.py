import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("=" * 60)
print("CHURN PREDICTION MODEL")
print("=" * 60)

# -----------------------
# Load Data
# -----------------------

df = pd.read_csv("data/processed/churn_data.csv")

X = df[[
    "Recency",
    "Frequency",
    "Monetary"
]]

y = df["Churn"]

# -----------------------
# Train Test Split
# -----------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------
# Train Model
# -----------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------
# Predictions
# -----------------------

pred = model.predict(X_test)

acc = accuracy_score(
    y_test,
    pred
)

print(f"\nAccuracy : {acc:.4f}")

print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        pred
    )
)

print("\nConfusion Matrix\n")

print(
    confusion_matrix(
        y_test,
        pred
    )
)

# -----------------------
# Save Model
# -----------------------

os.makedirs(
    "models",
    exist_ok=True
)

joblib.dump(
    model,
    "models/churn_model.pkl"
)

print("\n✅ Churn Model Saved!")