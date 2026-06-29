import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.data_loader import load_data

st.set_page_config(
    page_title="Demand Forecasting",
    layout="wide"
)

st.title("📈 Demand Forecasting")

# -----------------------
# Load Data
# -----------------------

history = load_data()

forecast = pd.read_csv("data/processed/forecast.csv")

history["InvoiceDate"] = pd.to_datetime(history["InvoiceDate"])

history = (
    history.groupby(history["InvoiceDate"].dt.date)["TotalPrice"]
    .sum()
    .reset_index()
)

history.columns = ["Date", "Revenue"]

history["Date"] = pd.to_datetime(history["Date"])
forecast["Date"] = pd.to_datetime(forecast["Date"])

# -----------------------
# KPIs
# -----------------------

forecast_days = len(forecast)
forecast_total = forecast["Forecast"].sum()
forecast_avg = forecast["Forecast"].mean()

best_day = forecast.loc[
    forecast["Forecast"].idxmax()
]

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Forecast Days",
    forecast_days
)

c2.metric(
    "Forecast Revenue",
    f"₹{forecast_total:,.0f}"
)

c3.metric(
    "Average / Day",
    f"₹{forecast_avg:,.0f}"
)

c4.metric(
    "Highest Forecast",
    f"₹{best_day['Forecast']:,.0f}"
)

st.divider()

# -----------------------
# Combined Chart
# -----------------------

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=history["Date"],
        y=history["Revenue"],
        mode="lines",
        name="Historical Sales"
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast["Date"],
        y=forecast["Forecast"],
        mode="lines+markers",
        name="Forecast"
    )
)

fig.update_layout(
    title="Historical vs Forecast Sales",
    xaxis_title="Date",
    yaxis_title="Revenue",
    height=550
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------
# Two Charts
# -----------------------

left, right = st.columns(2)

with left:

    fig = px.line(
        history.tail(60),
        x="Date",
        y="Revenue",
        title="Last 60 Days Sales"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.bar(
        forecast,
        x="Date",
        y="Forecast",
        title="Next 30 Days Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -----------------------
# Forecast Table
# -----------------------

st.subheader("Next 30 Days Forecast")

st.dataframe(
    forecast,
    use_container_width=True,
    hide_index=True
)

# -----------------------
# Download
# -----------------------

csv = forecast.to_csv(index=False)

st.download_button(
    "⬇ Download Forecast CSV",
    csv,
    file_name="forecast.csv",
    mime="text/csv"
)