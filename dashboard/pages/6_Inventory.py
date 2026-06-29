import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Inventory Intelligence",
    layout="wide"
)

st.title("📦 Inventory Intelligence")

# -----------------------
# Load Data
# -----------------------

df = pd.read_csv("data/processed/inventory_analysis.csv")

# -----------------------
# Sidebar Filters
# -----------------------

st.sidebar.header("Filters")

status = st.sidebar.selectbox(
    "Inventory Status",
    ["All"] + sorted(df["InventoryStatus"].unique())
)

top_n = st.sidebar.slider(
    "Top Products",
    5,
    30,
    10
)

search = st.sidebar.text_input(
    "Search Product"
)

filtered = df.copy()

if status != "All":
    filtered = filtered[
        filtered["InventoryStatus"] == status
    ]

if search:
    filtered = filtered[
        filtered["Description"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

# -----------------------
# KPIs
# -----------------------

total_products = len(filtered)

fast = (
    filtered["InventoryStatus"]
    == "Fast Moving"
).sum()

slow = (
    filtered["InventoryStatus"]
    == "Slow Moving"
).sum()

revenue = filtered["Revenue"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Products", total_products)
c2.metric("Fast Moving", fast)
c3.metric("Slow Moving", slow)
c4.metric("Revenue", f"₹{revenue:,.0f}")

st.divider()

# -----------------------
# Charts
# -----------------------

left, right = st.columns(2)

with left:

    fig = px.pie(
        filtered,
        names="InventoryStatus",
        title="Inventory Status Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    top_products = (
        filtered
        .sort_values(
            "QuantitySold",
            ascending=False
        )
        .head(top_n)
    )

    fig = px.bar(
        top_products,
        x="QuantitySold",
        y="Description",
        orientation="h",
        title=f"Top {top_n} Selling Products"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -----------------------
# Revenue Chart
# -----------------------

top_revenue = (
    filtered
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(top_n)
)

fig = px.bar(
    top_revenue,
    x="Revenue",
    y="Description",
    orientation="h",
    title=f"Top {top_n} Revenue Generating Products"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -----------------------
# Inventory Table
# -----------------------

st.subheader("Inventory Details")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

# -----------------------
# Download
# -----------------------

csv = filtered.to_csv(index=False)

st.download_button(
    "⬇ Download Inventory Report",
    csv,
    file_name="inventory_analysis.csv",
    mime="text/csv"
)