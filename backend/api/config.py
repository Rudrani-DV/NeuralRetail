from pathlib import Path

# -----------------------
# Project Paths
# -----------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODELS_DIR = PROJECT_ROOT / "models"
DATA_DIR = PROJECT_ROOT / "data" / "processed"

# -----------------------
# Data Files
# -----------------------

CLEANED_DATA = DATA_DIR / "cleaned_data.csv"

CUSTOMERS_FILE = DATA_DIR / "customer_segments.csv"

FORECAST_FILE = DATA_DIR / "forecast.csv"

INVENTORY_FILE = DATA_DIR / "inventory_analysis.csv"

CHURN_DATA = DATA_DIR / "churn_data.csv"

RFM_DATA = DATA_DIR / "rfm_data.csv"

DAILY_SALES = DATA_DIR / "daily_sales.csv"

# -----------------------
# Models
# -----------------------

CHURN_MODEL = MODELS_DIR / "churn_model.pkl"

SARIMA_MODEL = MODELS_DIR / "sarima_model.pkl"