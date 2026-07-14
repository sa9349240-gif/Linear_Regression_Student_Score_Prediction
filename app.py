
import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("linear_regression_model.pkl", "rb"))

st.title("Student Score Prediction App")
st.write("Enter the student details to predict the exam score.")

hours = st.number_input("Hours Studied", min_value=0.0, value=5.0)
sleep = st.number_input("Sleep Hours", min_value=0.0, value=7.0)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=80)

if st.button("Predict Score"):
    prediction = model.predict([[hours, sleep, attendance]])

    st.success(f"Predicted Exam Score: {prediction[0]:.2f}")
