import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("uber_xgb_model.pkl")

# Load hourly data
hourly_df = pd.read_csv("hourly_counts.csv", parse_dates=["Date"], index_col="Date")

st.title("Uber Trip Demand Prediction")
st.write("This app predicts the next hour's Uber trip demand using the last 24 hours of data.")

# Show chart
st.subheader("Last 7 Days of Hourly Trips")
st.line_chart(hourly_df["Count"].tail(24 * 7))

# Prepare last 24 hours
last_24 = hourly_df["Count"].tail(24).values

st.subheader("Last 24 Hours Used for Prediction")
st.write(last_24)

# Predict
if st.button("Predict Next Hour"):
    X = last_24.reshape(1, -1)
    pred = model.predict(X)[0]
    st.success(f"Predicted trips next hour: {pred:.0f}")
