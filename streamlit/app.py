import streamlit as st

# Enter your age
age = st.number_input(
    "Enter your age", value=None, placeholder="Type a number..."
)

st.write("The current age is", age)

# Enter your gender
gender = st.selectbox("Gender", ["Male", "Female"])
st.write("You selected:", gender)

# Province
province = st.selectbox("Province", ["Free State", "Limpopp", "Gauteng", "Mpumalanga",
                        "Nothern Cape", "KwaZulu-Natal", "Western Cape", "North West", "Eastern Cape"])
st.write("You selected:", province)

# Employment status
employment_status = st.selectbox("Employment_status", [
                                 "Self-employed", "Employed", "Retired", "Unemployed", "Student"])

# Years_driving
years_driving = st.slider(
    "How many years of driving experience do you have?", 0, 130, 25)
st.write("You chose:", years_driving)

# Car Make
car_make = st.selectbox("Car_Make", ["Ford", "BMW", "Hyundai",
                        "Toyota", "Mercedes", "Volkswagen"])
st.write("You chose:", car_make)

# Car_Model
car_model = st.selectbox("Car_Model", ["Fiesta", "X5", "Tucson", "118i", "Creta", "EcoSport", "i20", "Hilux",
                         "Corolla", "Ranger", "320i", "Fortuner", "Golf", "A200", "GLA", "Tiguan", "C200", "Polo"])

# Marital_Status
marital_status = st.selectbox(
    "Marital_status", ["Widowed", "Single", "Married", "Divorced"])
st.write("You chose:", marital_status)

# Vehicle_usage
vehicle_usage = st.selectbox(
    "Vehicle_usage", ["Commercial", "Business", "Private"])
st.write("You chose:", vehicle_usage)

# Manufacture_year
manufacture_year = st.number_input(
    "Car Manufacture Year:", value=None, placeholder="Type a number...")
st.write("You chose:", manufacture_year)

# Annual_car_mileage
annual_car_mileage = st.number_input(
    "Annual Car Mileage:", st.write("You chose:", car_make))
st.write("You chose:", annual_car_mileage)

# Number of accidents
number_of_accidents = st.number_input(
    "Number of Accidents:", value=None, placeholder="Type a number...")
st.write("You chose:", number_of_accidents)

# Number of claims
number_of_claims = st.number_input(
    "Number of Claims:", value=None, placeholder="Type a number...")
st.write("You chose:", number_of_claims)

# Car_value
car_value = st.number_input("Car Value in Rands:",
                            value=None, placeholder="Type a number...")
st.write("You chose:", car_value)

# Tracking_device
tracking_device = st.radio(
    "Do you have a tracking device installed?",
    ["Yes", "No"]
)
st.write("You chose:", tracking_device)

# Policy_term
policy_term = st.selectbox("Policy_Term", ["6", "12"])
st.write("You chose:", policy_term)

# Credit Score
credit_score = st.number_input(
    "Credit Score", value=None, placeholder="Enter your credit score...")
st.write("You chose:", credit_score)
