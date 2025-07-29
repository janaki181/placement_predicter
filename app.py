import streamlit as st
import pickle
import joblib
import numpy as np

# Load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

sc = joblib.load('sc.pkl')  # This must be the FITTED scaler

# Streamlit app
st.title("Placement Prediction")

cgpa = st.number_input("Enter CGPA : ")
iq = st.number_input("Enter IQ : ")

if st.button("Predict Placement"):
    input_data = np.array([[cgpa, iq]])
    input_scaled = sc.transform(input_data)  # Use transform ONLY
    prediction = model.predict(input_scaled)
    result = "Placed" if prediction[0] == 1 else "Not Placed"
    st.success(f"Prediction: {result}")
