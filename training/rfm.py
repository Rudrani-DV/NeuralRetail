import pandas as pd

# -----------------------
# Load cleaned data
# -----------------------
df = pd.read_csv("data/processed/cleaned_data.csv")

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# -----------------------
# Reference Date
# -----------------------
snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

print("Snapshot Date:", snapshot_date)

# -----------------------
# Create RFM Table
# -----------------------

rfm = df.groupby("Customer ID").agg({

    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,

    "Invoice": "nunique",

    "TotalPrice": "sum"

})

rfm.columns = ["Recency", "Frequency", "Monetary"]

print("\nRFM Table\n")

print(rfm.head())

print("\nShape:", rfm.shape)

# Save
rfm.to_csv("data/processed/rfm_data.csv")

print("\n✅ RFM dataset saved.")