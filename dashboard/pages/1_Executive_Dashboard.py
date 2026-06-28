import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📊 Executive Dashboard")

# Load data
df = pd.read_csv("data/processed/cleaned_data.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# ==========================
# KPIs
# ==========================

revenue = df["TotalPrice"].sum()
customers = df["Customer ID"].nunique()
products = df["StockCode"].nunique()
orders = df["Invoice"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Revenue", f"₹{revenue:,.0f}")
c2.metric("👥 Customers", customers)
c3.metric("📦 Products", products)
c4.metric("🧾 Orders", orders)

st.divider()

# ==========================
# Revenue Trend
# ==========================

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
    markers=True,
    title="Monthly Revenue"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# Two Charts
# ==========================

left, right = st.columns(2)

with left:

    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Quantity",
        y="Description",
        orientation="h",
        title="Top Selling Products"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    top_country = (
        df.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_country,
        x="Country",
        y="TotalPrice",
        title="Revenue by Country"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================
# Recent Orders
# ==========================

st.subheader("Recent Transactions")

st.dataframe(
    df.tail(20),
    use_container_width=True,
    hide_index=True
)