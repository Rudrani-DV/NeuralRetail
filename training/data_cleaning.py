import pandas as pd

# Load dataset
df = pd.read_excel("data/raw/online_retail.xlsx")

print("=" * 50)
print("ORIGINAL DATA")
print("=" * 50)

print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nMissing Values")
print(df.isnull().sum())

# Remove missing Customer ID
df = df.dropna(subset=["Customer ID"])

# Remove missing descriptions
df = df.dropna(subset=["Description"])

# Remove cancelled invoices
df = df[~df["Invoice"].astype(str).str.startswith("C")]

# Remove negative or zero quantity
df = df[df["Quantity"] > 0]

# Remove negative or zero price
df = df[df["Price"] > 0]

# Create TotalPrice column
df["TotalPrice"] = df["Quantity"] * df["Price"]

print("\n")
print("=" * 50)
print("CLEANED DATA")
print("=" * 50)

print("Rows:", len(df))

print("\nMissing Values")
print(df.isnull().sum())

print("\nFirst 5 rows")
print(df.head())

# Save cleaned data
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("\n✅ Cleaned dataset saved to data/processed/cleaned_data.csv")