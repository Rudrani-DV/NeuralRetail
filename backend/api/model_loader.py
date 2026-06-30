import joblib

from .config import CHURN_MODEL, SARIMA_MODEL

# Load models only once when the API starts

churn_model = joblib.load(CHURN_MODEL)

sarima_model = joblib.load(SARIMA_MODEL)