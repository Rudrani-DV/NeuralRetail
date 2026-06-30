from fastapi import APIRouter, HTTPException
import pandas as pd

from .config import (
    CLEANED_DATA,
    CUSTOMERS_FILE,
    FORECAST_FILE,
    INVENTORY_FILE
)

from .model_loader import churn_model

from .schemas import (
    ChurnRequest,
    ChurnResponse,
    DashboardResponse,
    HealthResponse,
    HomeResponse
)

router = APIRouter()


# --------------------------------------------------
# General
# --------------------------------------------------

@router.get("/", tags=["General"], response_model=HomeResponse)
def home():
    return {
        "application": "NeuralRetail API",
        "version": "1.0.0"
    }


@router.get("/health", tags=["General"], response_model=HealthResponse)
def health():
    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Dashboard
# --------------------------------------------------

@router.get(
    "/dashboard",
    tags=["Dashboard"],
    response_model=DashboardResponse
)
def dashboard():

    if not CLEANED_DATA.exists():
        raise HTTPException(
            status_code=404,
            detail="cleaned_data.csv not found."
        )

    df = pd.read_csv(CLEANED_DATA)

    revenue = float(df["TotalPrice"].sum())
    orders = int(df["Invoice"].nunique())
    customers = int(df["Customer ID"].nunique())
    average_order = revenue / orders if orders else 0

    return DashboardResponse(
        revenue=revenue,
        orders=orders,
        customers=customers,
        average_order_value=round(average_order, 2)
    )


# --------------------------------------------------
# Forecast
# --------------------------------------------------

@router.get("/forecast", tags=["Forecast"])
def forecast():

    if not FORECAST_FILE.exists():
        raise HTTPException(
            status_code=404,
            detail="forecast.csv not found."
        )

    df = pd.read_csv(FORECAST_FILE)

    return df.to_dict(orient="records")


# --------------------------------------------------
# Inventory
# --------------------------------------------------

@router.get("/inventory", tags=["Inventory"])
def inventory():

    if not INVENTORY_FILE.exists():
        raise HTTPException(
            status_code=404,
            detail="inventory_analysis.csv not found."
        )

    df = pd.read_csv(INVENTORY_FILE)

    return df.to_dict(orient="records")


# --------------------------------------------------
# Customers
# --------------------------------------------------

@router.get("/customers", tags=["Customers"])
def customers():

    if not CUSTOMERS_FILE.exists():
        raise HTTPException(
            status_code=404,
            detail="customer_segments.csv not found."
        )

    df = pd.read_csv(CUSTOMERS_FILE)

    return df.to_dict(orient="records")


# --------------------------------------------------
# Machine Learning
# --------------------------------------------------

@router.post(
    "/predict/churn",
    tags=["Machine Learning"],
    response_model=ChurnResponse
)
def predict_churn(data: ChurnRequest):

    prediction = churn_model.predict([[
        data.recency,
        data.frequency,
        data.monetary
    ]])[0]

    result = (
        "Likely to Churn"
        if prediction == 1
        else "Active Customer"
    )

    return ChurnResponse(
        prediction=result
    )