import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="Sleep Stress Prediction", layout="wide")

st.title("📱😴 Sleep & Stress Prediction App")
st.write("Predict stress level based on sleep, mobile usage, and lifestyle factors.")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("sleep_mobile_stress_dataset_15000.csv")

df = load_data()

# Show dataset
st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

st.subheader("📊 Basic Information")
st.write("Shape of dataset:", df.shape)
st.write("Columns:", list(df.columns))

# Sidebar inputs
st.sidebar.header("Enter User Details")

age = st.sidebar.slider("Age", 18, 60, 25)
gender = st.sidebar.selectbox("Gender", df["gender"].unique())
occupation = st.sidebar.selectbox("Occupation", df["occupation"].unique())
daily_screen_time_hours = st.sidebar.slider("Daily Screen Time (hours)", 1.0, 12.0, 5.0)
phone_usage_before_sleep_minutes = st.sidebar.slider("Phone Usage Before Sleep (minutes)", 0, 180, 60)
sleep_duration_hours = st.sidebar.slider("Sleep Duration (hours)", 3.0, 12.0, 7.0)
sleep_quality_score = st.sidebar.slider("Sleep Quality Score", 1, 10, 5)
caffeine_intake_cups = st.sidebar.slider("Caffeine Intake (cups)", 0, 10, 2)
physical_activity_minutes = st.sidebar.slider("Physical Activity (minutes)", 0, 180, 30)
notifications_received_per_day = st.sidebar.slider("Notifications per Day", 0, 300, 80)
mental_fatigue_score = st.sidebar.slider("Mental Fatigue Score", 1, 10, 5)

# Show entered data
input_data = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "occupation": [occupation],
    "daily_screen_time_hours": [daily_screen_time_hours],
    "phone_usage_before_sleep_minutes": [phone_usage_before_sleep_minutes],
    "sleep_duration_hours": [sleep_duration_hours],
    "sleep_quality_score": [sleep_quality_score],
    "caffeine_intake_cups": [caffeine_intake_cups],
    "physical_activity_minutes": [physical_activity_minutes],
    "notifications_received_per_day": [notifications_received_per_day],
    "mental_fatigue_score": [mental_fatigue_score]
})

st.subheader("📝 User Input")
st.dataframe(input_data)

# Simple demo prediction logic (replace later with trained model)
if st.button("Predict Stress Level"):
    predicted_stress = (
        daily_screen_time_hours * 0.5
        + phone_usage_before_sleep_minutes * 0.01
        - sleep_duration_hours * 0.3
        + caffeine_intake_cups * 0.4
        - physical_activity_minutes * 0.01
        + mental_fatigue_score * 0.5
    )

    predicted_stress = max(1, min(10, round(predicted_stress, 2)))

    st.success(f"Predicted Stress Level: **{predicted_stress} / 10**")

    if predicted_stress < 4:
        st.info("Stress Category: Low")
    elif predicted_stress < 7:
        st.warning("Stress Category: Medium")
    else:
        st.error("Stress Category: High")