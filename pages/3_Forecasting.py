import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

df = pd.read_csv("sales_data.csv")

st.title("Demand Forecasting")

store = st.selectbox(
    "Store",
    sorted(df["Store ID"].unique())
)

product = st.selectbox(
    "Product",
    sorted(df["Product ID"].unique())
)

category = st.selectbox(
    "Category",
    sorted(df["Category"].unique())
)

region = st.selectbox(
    "Region",
    sorted(df["Region"].unique())
)

weather = st.selectbox(
    "Weather",
    sorted(df["Weather Condition"].unique())
)

seasonality = st.selectbox(
    "Seasonality",
    sorted(df["Seasonality"].unique())
)

price = st.number_input("Price")

discount = st.number_input("Discount")

inventory = st.number_input(
    "Inventory Level"
)

units_ordered = st.number_input(
    "Units Ordered"
)

competitor = st.number_input(
    "Competitor Pricing"
)

promotion = st.selectbox(
    "Promotion",
    [0,1]
)

epidemic = st.selectbox(
    "Epidemic",
    [0,1]
)

if st.button("Predict"):

    data = [[
        6,2026,2,24,3,0,
        price,
        discount,
        inventory,
        units_ordered,
        competitor,
        promotion,
        epidemic,
        encoders["Store ID"].transform([store])[0],
        encoders["Product ID"].transform([product])[0],
        encoders["Category"].transform([category])[0],
        encoders["Region"].transform([region])[0],
        encoders["Weather Condition"].transform([weather])[0],
        encoders["Seasonality"].transform([seasonality])[0]
    ]]

    prediction = model.predict(data)

    st.success(
        f"Forecast Demand = {prediction[0]:.0f}"
    )