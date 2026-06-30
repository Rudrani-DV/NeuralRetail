# 🛍️ NeuralRetail

> AI-Powered Retail Analytics Platform built with Machine Learning, FastAPI, Streamlit and Docker.

---

## 📌 Overview

NeuralRetail is an end-to-end Retail Analytics platform that helps businesses analyze customer behavior, predict customer churn, forecast sales demand, and optimize inventory using Machine Learning.

The project combines:

- Machine Learning
- Data Analytics
- Interactive Dashboard
- REST API
- Docker Deployment

---

## 🚀 Features

### 📊 Executive Dashboard

- Revenue Analysis
- Customer Overview
- Orders Overview
- KPI Cards

---

### 👥 Customer Intelligence

- RFM Analysis
- Customer Segmentation
- High Value Customers
- Customer Lifetime Insights

---

### 📈 Sales Analytics

- Monthly Revenue
- Top Products
- Country Wise Sales
- Interactive Charts

---

### 📦 Inventory Intelligence

- Inventory Analysis
- Product Performance
- Revenue by Product
- Stock Recommendations

---

### 📉 Demand Forecasting

- SARIMA Forecasting
- 30-Day Sales Forecast
- Trend Visualization

---

### 🤖 Customer Churn Prediction

Predicts whether a customer is likely to churn using a trained XGBoost model.

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- FastAPI
- Uvicorn

### Machine Learning

- Scikit-learn
- XGBoost
- SARIMA (Statsmodels)

### Data Analysis

- Pandas
- NumPy
- Plotly
- Matplotlib

### Deployment

- Docker
- Docker Compose

---

## 📂 Project Structure

```text
NeuralRetail/

backend/
dashboard/
training/
models/
data/
assets/

Dockerfile
docker-compose.yml
requirements.txt
README.md
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd NeuralRetail

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run dashboard/Home.py
```

---

## 🐳 Docker

```bash
docker compose build

docker compose up
```

---

## 🌐 API Documentation

FastAPI Swagger:

```
http://localhost:8000/docs
```

---

## 📸 Dashboard Preview

(Add screenshots here)

---

## 🔮 Future Improvements

- Authentication
- Database Integration
- Live Sales Dashboard
- Cloud Deployment
- Recommendation System
- Automated Model Retraining

---

## 👨‍💻 Author

**Rudrani Dayal Verma**