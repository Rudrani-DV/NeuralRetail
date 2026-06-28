import streamlit as st

st.set_page_config(
    page_title="NeuralRetail",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 NeuralRetail")

st.subheader("AI Powered Sales Intelligence Platform")

st.markdown("---")

st.markdown("""
### Welcome 👋

NeuralRetail is an AI-powered retail analytics platform designed to help businesses:

- 📈 Analyze Sales
- 👥 Understand Customers
- 📦 Optimize Inventory
- 📉 Forecast Demand
- ⚠ Predict Customer Churn

Use the sidebar to navigate through the dashboard.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("✔ Data Pipeline")

with col2:
    st.success("✔ Machine Learning")

with col3:
    st.success("✔ Business Intelligence")