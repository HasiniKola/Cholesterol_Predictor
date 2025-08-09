import streamlit as st
import joblib
from recommendation import recommend

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# UI
st.set_page_config(page_title="Cholesterol Predictor", page_icon="🩺")
st.title("🩺 Cholesterol Level Predictor")
st.markdown("Predict your cholesterol level and get personalized health advice.")

# Inputs
age = st.slider("Age", 18, 100, 30)
bmi = st.slider("BMI", 10.0, 40.0, 22.0)
bp = st.slider("Blood Pressure", 80, 200, 120)
activity = st.selectbox("Activity Level", [1, 2, 3, 4, 5], format_func=lambda x: f"{x} - {'Sedentary' if x==1 else 'Active' if x==5 else 'Moderate'}")

# Predict
if st.button("Predict Cholesterol"):
    input_data = scaler.transform([[age, bmi, bp, activity]])
    result = model.predict(input_data)[0]
    st.success(f"Predicted Cholesterol Level: **{round(result, 2)} mg/dL**")
    st.info(recommend(result))