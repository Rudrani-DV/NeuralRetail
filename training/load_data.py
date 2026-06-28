import pandas as pd

# Load dataset
df = pd.read_excel("data/raw/online_retail.xlsx")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())