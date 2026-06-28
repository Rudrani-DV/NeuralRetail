import pandas as pd
import plotly.express as px
import os

# -----------------------
# Load Data
# -----------------------

df = pd.read_csv("data/processed/cleaned_data.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create reports folder
os.makedirs("reports", exist_ok=True)

# -----------------------
# KPI Summary
# -----------------------

print("=" * 50)
print("DATASET SUMMARY")
print("=" * 50)

print("Total Transactions :", len(df))
print("Total Customers    :", df["Customer ID"].nunique())
print("Total Products     :", df["StockCode"].nunique())
print("Countries          :", df["Country"].nunique())

print("\nTotal Revenue : ₹{:,.2f}".format(df["TotalPrice"].sum()))

# -----------------------
# Monthly Revenue
# -----------------------

df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

monthly = (
    df.groupby("Month")["TotalPrice"]
      .sum()
      .reset_index()
)

fig = px.line(
    monthly,
    x="Month",
    y="TotalPrice",
    title="Monthly Revenue"
)

fig.write_html("reports/monthly_revenue.html")

# -----------------------
# Top 10 Countries
# -----------------------

country = (
    df.groupby("Country")["TotalPrice"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

fig = px.bar(
    country,
    x="Country",
    y="TotalPrice",
    title="Top 10 Countries by Revenue"
)

fig.write_html("reports/top_countries.html")

# -----------------------
# Top 10 Products
# -----------------------

products = (
    df.groupby("Description")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .reset_index()
)

fig = px.bar(
    products,
    x="Quantity",
    y="Description",
    orientation="h",
    title="Top Selling Products"
)

fig.write_html("reports/top_products.html")

print("\nEDA Reports Generated Successfully!")
print("Check the reports folder.")