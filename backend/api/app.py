from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="NeuralRetail API",
    description="""
## NeuralRetail AI Retail Analytics Platform

Production-ready REST API for retail analytics.

### Features

- 📊 Executive Dashboard KPIs
- 👥 Customer Segmentation
- 📦 Inventory Intelligence
- 📈 Sales Forecasting
- 🤖 Customer Churn Prediction

Built using:
- FastAPI
- Scikit-learn
- SARIMA
- Pandas
- Streamlit
""",
    version="1.0.0",
    contact={
        "name": "Anurag Mahanta"
    },
    license_info={
        "name": "MIT License"
    }
)

app.include_router(
    router,
    prefix="/api/v1"
)