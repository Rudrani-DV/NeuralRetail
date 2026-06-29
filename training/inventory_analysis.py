import os
import pandas as pd

print("=" * 60)
print("INVENTORY ANALYSIS")
print("=" * 60)

# -----------------------
# Load Cleaned Data
# -----------------------

df = pd.read_csv("data/processed/cleaned_data.csv")

# -----------------------
# Product Summary
# -----------------------

inventory = (
    df.groupby(["StockCode", "Description"])
    .agg(
        QuantitySold=("Quantity", "sum"),
        Revenue=("TotalPrice", "sum"),
        AvgPrice=("Price", "mean"),
        Orders=("Invoice", "nunique")
    )
    .reset_index()
)

# -----------------------
# Inventory Status
# -----------------------

inventory["InventoryStatus"] = "Normal"

inventory.loc[
    inventory["QuantitySold"] >= 1000,
    "InventoryStatus"
] = "Fast Moving"

inventory.loc[
    inventory["QuantitySold"] <= 100,
    "InventoryStatus"
] = "Slow Moving"

# -----------------------
# Recommendation
# -----------------------

inventory["Recommendation"] = inventory["InventoryStatus"].map({
    "Fast Moving": "Restock Immediately",
    "Normal": "Monitor Stock",
    "Slow Moving": "Reduce Inventory"
})

# -----------------------
# Save
# -----------------------

os.makedirs(
    "data/processed",
    exist_ok=True
)

inventory.to_csv(
    "data/processed/inventory_analysis.csv",
    index=False
)

print("\nInventory Summary")

print(inventory.head())

print("\nInventory Status")

print(
    inventory["InventoryStatus"].value_counts()
)

print("\n✅ Inventory analysis saved!")