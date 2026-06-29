import os
import joblib
import warnings
import pandas as pd

from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")

print("=" * 60)
print("DEMAND FORECASTING (SARIMA)")
print("=" * 60)

# -----------------------
# Load Data
# -----------------------

df = pd.read_csv("data/processed/daily_sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

df.set_index("Date", inplace=True)

sales = df["Revenue"]

print("\nTraining Data")
print(sales.head())

# -----------------------
# Train SARIMA
# -----------------------

print("\nTraining Model...")

model = SARIMAX(
    sales,
    order=(1,1,1),
    seasonal_order=(1,1,1,7),
    enforce_stationarity=False,
    enforce_invertibility=False
)

model_fit = model.fit()

print("✅ Model Trained!")

# -----------------------
# Forecast
# -----------------------

forecast = model_fit.forecast(30)

forecast_df = pd.DataFrame({
    "Date": pd.date_range(
        sales.index[-1] + pd.Timedelta(days=1),
        periods=30
    ),
    "Forecast": forecast.values
})

# -----------------------
# Save Files
# -----------------------

os.makedirs("models", exist_ok=True)

joblib.dump(
    model_fit,
    "models/sarima_model.pkl"
)

forecast_df.to_csv(
    "data/processed/forecast.csv",
    index=False
)

print("\nForecast Saved!")

print("\nNext 30 Days\n")

print(forecast_df)