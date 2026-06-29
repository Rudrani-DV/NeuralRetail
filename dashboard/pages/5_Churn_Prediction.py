import joblib
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Churn Prediction",
    layout="wide"
)

st.title("⚠️ Customer Churn Prediction")

# -----------------------
# Load Data
# -----------------------

df = pd.read_csv("data/processed/churn_data.csv")

model = joblib.load("models/churn_model.pkl")

# -----------------------
# Predictions
# -----------------------

X = df[["Recency", "Frequency", "Monetary"]]

df["Prediction"] = model.predict(X)

# -----------------------
# KPIs
# -----------------------

total = len(df)
churn = (df["Prediction"] == 1).sum()
active = total - churn
rate = churn / total * 100

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", total)
c2.metric("High Risk", churn)
c3.metric("Active", active)
c4.metric("Churn Rate", f"{rate:.1f}%")

st.divider()

# -----------------------
# Churn Distribution
# -----------------------

left, right = st.columns(2)

with left:

    fig = px.pie(
        df,
        names="Prediction",
        title="Customer Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    })

    fig = px.bar(
        importance.sort_values(
            "Importance",
            ascending=False
        ),
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# -----------------------
# Interactive Prediction
# -----------------------

st.subheader("Predict Customer Churn")

col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input(
        "Recency",
        min_value=0,
        value=30
    )

with col2:
    frequency = st.number_input(
        "Frequency",
        min_value=1,
        value=5
    )

with col3:
    monetary = st.number_input(
        "Monetary",
        min_value=0.0,
        value=1000.0
    )

if st.button("Predict"):

    pred = model.predict(
        [[recency, frequency, monetary]]
    )[0]

    if pred == 1:
        st.error("🔴 Customer is likely to churn.")
    else:
        st.success("🟢 Customer is likely to stay.")

st.divider()

# -----------------------
# High Risk Customers
# -----------------------

st.subheader("High Risk Customers")

risk = df[df["Prediction"] == 1]

st.dataframe(
    risk,
    use_container_width=True,
    hide_index=True
)

# -----------------------
# Download
# -----------------------

csv = df.to_csv(index=False)

st.download_button(
    "⬇ Download Predictions",
    csv,
    file_name="customer_churn_predictions.csv",
    mime="text/csv"
)