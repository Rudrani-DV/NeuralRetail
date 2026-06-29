import os
import pandas as pd

print("=" * 60)
print("CHURN DATA PREPARATION")
print("=" * 60)

# -----------------------
# Load Cleaned Data
# -----------------------

df = pd.read_csv("data/processed/cleaned_data.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Latest purchase date
snapshot_date = df["InvoiceDate"].max()

# -----------------------
# Customer Features
# -----------------------

customer = (
    df.groupby("Customer ID")
    .agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "Invoice": "nunique",
        "TotalPrice": "sum"
    })
)

customer.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]

# -----------------------
# Churn Label
# -----------------------

# Customer inactive for more than 90 days

customer["Churn"] = (
    customer["Recency"] > 90
).astype(int)

print("\nDataset Shape")

print(customer.shape)

print("\nChurn Distribution")

print(customer["Churn"].value_counts())

# -----------------------
# Save Dataset
# -----------------------

os.makedirs(
    "data/processed",
    exist_ok=True
)

customer.to_csv(
    "data/processed/churn_data.csv"
)

print("\n✅ Churn Dataset Saved!")