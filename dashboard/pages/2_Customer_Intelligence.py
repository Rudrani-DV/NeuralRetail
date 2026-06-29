import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("👥 Customer Intelligence")

# ----------------------------
# Load Customer Segments
# ----------------------------

df = pd.read_csv("data/processed/customer_segments.csv")

# ----------------------------
# Rename Clusters
# ----------------------------

segment_names = {
    0: "🛒 Regular Customers",
    1: "⚠ At Risk Customers",
    2: "👑 VIP Customers",
    3: "💎 Loyal Customers"
}

df["Segment"] = df["Cluster"].map(segment_names)

# ----------------------------
# KPI Cards
# ----------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", len(df))

c2.metric(
    "Average Recency",
    round(df["Recency"].mean(),1)
)

c3.metric(
    "Average Frequency",
    round(df["Frequency"].mean(),1)
)

c4.metric(
    "Average Spending",
    f"₹{df['Monetary'].mean():,.0f}"
)

st.divider()

# ----------------------------
# Segment Distribution
# ----------------------------

segment_count = (
    df["Segment"]
    .value_counts()
    .reset_index()
)

segment_count.columns = [
    "Segment",
    "Customers"
]

fig = px.bar(
    segment_count,
    x="Segment",
    y="Customers",
    color="Segment",
    title="Customer Segments"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Segment Revenue
# ----------------------------

segment_revenue = (
    df.groupby("Segment")["Monetary"]
    .sum()
    .reset_index()
)

fig = px.pie(
    segment_revenue,
    values="Monetary",
    names="Segment",
    title="Revenue Contribution"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Segment Summary
# ----------------------------

st.subheader("Segment Summary")

summary = (
    df.groupby("Segment")
    .agg({
        "Recency":"mean",
        "Frequency":"mean",
        "Monetary":"mean"
    })
)

st.dataframe(
    summary,
    use_container_width=True
)

# ----------------------------
# Top Customers
# ----------------------------

st.subheader("Top 20 Customers")

top = (
    df.sort_values(
        "Monetary",
        ascending=False
    )
    .head(20)
)

st.dataframe(
    top,
    use_container_width=True,
    hide_index=True
)