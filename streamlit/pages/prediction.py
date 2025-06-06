# Load environment variables first
import os
import sys
import time

import joblib
import pandas as pd
from dotenv import load_dotenv

import streamlit as st

# Load environment variables
load_dotenv()

# Get the absolute path to the project root (two levels up from this file)
project_root = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", ".."))

# Add the project root directory to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.features import preprocess_features  # noqa: E402

# Paths to the model and scaler
model_path = ("../models/ridge_model.joblib")
scaler_path = ("../models/scaler.joblib")
model_features_path = ("../models/model_features.joblib")

# Load model and scaler
model = joblib.load(model_path)
scaler, numeric_columns = joblib.load(scaler_path)
model_features = joblib.load(model_features_path)

# Add design elements to the page
st.set_page_config(page_title="Predict Premium", page_icon="📊")
st.title("Predict Your Car Insurance Premium")

st.header("Demographic information")

# Enter your age
age = int(st.number_input(
    "Enter your age", value=20, placeholder="Type a number...", min_value=18, max_value=100
))

# Enter your gender
gender = st.selectbox("Gender", ["Female", "Male"])

# Marital_Status
marital_status = st.selectbox(
    "What is your current marital status?", ["Divorced", "Married", "Single", "Widowed"])

# Province
province = st.selectbox("Select the province you currently reside in:", ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo" "Mpumalanga",
                                                                         "North West",  "Nothern Cape", "Western Cape"])

# Education Level
education_level = st.selectbox(
    "What is your highest level of education?", ["Degree", "Diploma", "High School", "Postgraduate"])

# Employment status
employment_status = st.selectbox("What is your current employment status?", [
    "Employed", "Retired", "Self-employed", "Student", "Unemployed"])

# Years_driving
max_years_driving = age - 18
if max_years_driving > 0:
    years_driving = int(st.slider(
        "How many years of driving experience do you have?", min_value=0, max_value=max_years_driving, value=min(5, max_years_driving)))
else:
    years_driving = 0
    st.warning(
        "You are not eligible to drive yet. Driving experience is set to 0.")

st.header("Vehicle information")

# Dictionary to map car makes to their models
car_make_models = {
    "BMW": ["118i", "320i", "X5"],
    "Ford": ["EcoSport", "Fiesta", "Ranger"],
    "Hyundai": ["Creta", "i20", "Tucson"],
    "Mercedes": ["A200",  "C200", "GLA"],
    "Toyota": ["Corolla", "Fortuner", "Hilux"],
    "Volkswagen": ["Golf", "Polo", "Tiguan"]
}

# Car Make
car_make = st.selectbox("Select the make of your car:",
                        list(car_make_models.keys()))

# Car_Model
car_model = st.selectbox("Select your car model:", car_make_models[car_make])

# Vehicle_usage
vehicle_usage = st.selectbox(
    "For what purposes do you use your car?", ["Business", "Commercial", "Private"])

# Manufacture_year
manufacture_year = int(st.number_input(
    "What is the manufacture year of your car?", value=2015, placeholder="Type a number...", min_value=1980, max_value=2025, step=1
))

# Annual_car_mileage
annual_car_mileage = int(st.number_input(
    "Enter the annual car mileage:", value=10000, min_value=0, max_value=500000))

# Number of accidents
number_of_accidents = int(st.number_input(
    "How many accidents has your car been involved in?", value=1, placeholder="Type a number...", min_value=0, max_value=10, step=1))

# Number of claims
number_of_claims = int(st.number_input(
    "How many claims have you filed in relation to your car?", value=1, placeholder="Type a number...",  min_value=0, max_value=10, step=1))

# Car_value
car_value = st.number_input("Car Value (ZAR):",
                            value=50000, placeholder="Type a number...", help="Enter the current value of your car in South African Rands (ZAR)")

# Tracking_device
tracking_device = st.radio(
    "Do you have a tracking device installed?",
    ["No", "Yes"]
)
tracking_device_encoded = 1 if tracking_device == "Yes" else 0

# Policy_term
policy_term = st.selectbox(
    "Select your desired policy term in months:", [6, 12, 24])

# Credit Score
credit_score = int(st.number_input(
    "Enter your credit score", value=350, placeholder="Enter your credit score...",  min_value=300, max_value=850, step=1))

# Define the credit category based on the credit score given:


def categorize_credit_score(credit_score):
    if credit_score < 580:
        return "Poor"
    elif 580 <= credit_score < 670:
        return "Fair"
    elif 670 <= credit_score < 740:
        return "Good"
    elif 740 <= credit_score < 800:
        return "Very Good"
    else:
        return "Excellent"


credit_category = categorize_credit_score(credit_score)

input_dictionary = {
    "Age": age,
    "Gender": gender,
    "Region": province,
    "Employment_Status": employment_status,
    "Education_Level": education_level,
    "Years_Driving": years_driving,
    "Car_Make": car_make,
    "Car_Model": car_model,
    "Manufacture_Year": manufacture_year,
    "Annual_Mileage": annual_car_mileage,
    "Number_of_Accidents": number_of_accidents,
    "Number_of_Claims": number_of_claims,
    "Car_Value": car_value,
    "Marital_Status": marital_status,
    "Has_AntiTheft_Device": tracking_device_encoded,
    "Policy_Term": policy_term,
    "Credit_Score": credit_score,
    "Vehicle_Usage": vehicle_usage,
    "Credit_Category": credit_category
}

col1, col2, col3 = st.columns([3.4, 2, 3.4])

with col2:
    pressed = st.button("Get your premium", type="primary")

if pressed:
    with st.spinner("Calculating premium..."):
        time.sleep(1)

        # Process input
        input_df = pd.DataFrame([input_dictionary])
        input_df_processed = preprocess_features(input_df)

        # Ensure all required columns are present
        for col in model_features:
            if col not in input_df_processed.columns:
                input_df_processed[col] = 0

        input_df_processed = input_df_processed[model_features]

        # Make sure numeric columns exist before scaling
        missing_numeric_cols = [
            col for col in numeric_columns if col not in input_df_processed.columns]
        for col in missing_numeric_cols:
            input_df_processed[col] = 0.0

        input_df_processed[numeric_columns] = scaler.transform(
            input_df_processed[numeric_columns]).astype('float64')

        # Predict
        prediction = model.predict(input_df_processed)

    # Display success message **outside** columns block, so it will be left aligned
    st.success(f"Estimated Insurance Premium: R{prediction[0]:,.2f} per month")
