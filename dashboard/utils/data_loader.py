import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cleaned_data.csv")
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    return df

@st.cache_data
def load_segments():
    return pd.read_csv("data/processed/customer_segments.csv")