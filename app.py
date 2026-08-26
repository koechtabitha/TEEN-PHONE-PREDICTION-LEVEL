import streamlit as st
import pandas as pd
import joblib

# Load saved model and preprocessor
model = joblib.load("logistic_addiction_classifier (1).pkl")
preprocessor = joblib.load("addiction_preprocessor (1).pkl")

st.title("📱 Smartphone Addiction Risk Prediction")
st.write("Predict smartphone addiction risk among teenagers.")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])

academic = st.number_input(
    "Academic Performance",
    min_value=0,
    max_value=10,
    value=5
)

social = st.number_input(
    "Social Interactions",
    min_value=0,
    max_value=10,
    value=5
)

depression = st.number_input(
    "Depression Level",
    min_value=0,
    max_value=10,
    value=5
)

sleep = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=8.0
)

exercise = st.number_input(
    "Exercise Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

daily_usage = st.number_input(
    "Daily Smartphone Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

education = st.number_input(
    "Time on Education Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

# Feature engineering
sleep_deficit = max(0, 9 - sleep)

if daily_usage > 0:
    exercise_to_usage_ratio = exercise / daily_usage
    edu_to_total_ratio = education / daily_usage
else:
    exercise_to_usage_ratio = 0
    edu_to_total_ratio = 0

# Create input dataframe
new_data = pd.DataFrame({
    "Gender": [gender],
    "Academic_Performance": [academic],
    "Social_Interactions": [social],
    "Depression_Level": [depression],
    "Sleep_Hours": [sleep],
    "Exercise_Hours": [exercise],
    "Daily_Usage_Hours": [daily_usage],
    "Time_on_Education": [education],
    "sleep_deficit": [sleep_deficit],
    "exercise_to_usage_ratio": [exercise_to_usage_ratio],
    "edu_to_total_ratio": [edu_to_total_ratio]
})

# Prediction
if st.button("Predict Addiction Risk"):

    processed_data = preprocessor.transform(new_data)

    prediction = model.predict(processed_data)[0]

    st.subheader("Prediction")

    if prediction == "High":
        st.error("🔴 High Smartphone Addiction Risk")
    elif prediction == "Moderate":
        st.warning("🟠 Moderate Smartphone Addiction Risk")
    else:
        st.success("🟢 Low Smartphone Addiction Risk")

    # Prediction probabilities
    probabilities = model.predict_proba(processed_data)[0]

    st.subheader("Prediction Probabilities")

    probability_df = pd.DataFrame({
        "Risk Level": model.classes_,
        "Probability": probabilities
    })

    probability_df["Probability"] = (
        probability_df["Probability"] * 100
    ).round(2)

    st.dataframe(probability_df)