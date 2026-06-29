import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

st.set_page_config(
    page_title="Sales Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Analytics Dashboard")
st.caption("Analyze sales performance across products, countries and time.")

df = load_data()

# ===================================================
# SIDEBAR
# ===================================================

st.sidebar.header("🔍 Filters")

countries = sorted(df["Country"].unique())

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + countries
)

if selected_country != "All":
    df = df[df["Country"] == selected_country]

# Date Filter

min_date = df["InvoiceDate"].min().date()
max_date = df["InvoiceDate"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_dates) == 2:
    start_date, end_date = selected_dates

    df = df[
        (df["InvoiceDate"].dt.date >= start_date) &
        (df["InvoiceDate"].dt.date <= end_date)
    ]

# ===================================================
# KPIs
# ===================================================

revenue = df["TotalPrice"].sum()
orders = df["Invoice"].nunique()
customers = df["Customer ID"].nunique()
products = df["StockCode"].nunique()
avg_order = revenue / orders if orders else 0

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("💰 Revenue", f"₹{revenue:,.0f}")
c2.metric("🧾 Orders", f"{orders:,}")
c3.metric("👥 Customers", f"{customers:,}")
c4.metric("📦 Products", f"{products:,}")
c5.metric("🛒 Avg Order", f"₹{avg_order:,.0f}")

st.divider()

# ===================================================
# MONTH COLUMN
# ===================================================

df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# ===================================================
# MONTHLY REVENUE
# ===================================================

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
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig, use_container_width=True)

# ===================================================
# MONTHLY ORDERS
# ===================================================

orders_month = (
    df.groupby("Month")["Invoice"]
    .nunique()
    .reset_index()
)

fig = px.bar(
    orders_month,
    x="Month",
    y="Invoice",
    title="Monthly Orders"
)

st.plotly_chart(fig, use_container_width=True)

# ===================================================
# TWO CHARTS
# ===================================================

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
        title="Top 10 Selling Products"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

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
        title="Revenue by Country"
    )

    st.plotly_chart(fig, use_container_width=True)

# ===================================================
# RECENT TRANSACTIONS
# ===================================================

st.subheader("📄 Recent Transactions")

st.dataframe(
    df.tail(20),
    use_container_width=True,
    hide_index=True
)

# ===================================================
# DOWNLOAD
# ===================================================

st.download_button(
    "📥 Download Filtered Sales Data",
    data=df.to_csv(index=False),
    file_name="sales_data.csv",
    mime="text/csv"
)