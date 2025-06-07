import random

import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define sample values for categorical fields
genders = ["Male", "Female"]
regions = ["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape",
           "Free State", "Limpopo", "Mpumalanga", "North West", "Nothern Cape"]
employment_statuses = ["Employed", "Self-employed",
                       "Unemployed", "Student", "Retired"]
education_levels = ["High School", "Diploma", "Degree", "Postgraduate"]
car_makes_models = {
    'Toyota': ['Corolla', 'Hilux', 'Fortuner'],
    'Volkswagen': ['Polo', 'Golf', 'Tiguan'],
    'Ford': ['Fiesta', 'Ranger', 'EcoSport'],
    'BMW': ['320i', 'X5', '118i'],
    'Mercedes': ['C200', 'GLA', 'A200'],
    'Hyundai': ['i20', 'Creta', 'Tucson']
}

marital_statuses = ['Single', 'Married', 'Divorced', 'Widowed']
vehicle_usages = ['Private', 'Business', 'Commercial']

# Generate the dataset
n = 15000
data = {
    'Customer_ID': np.arange(1, n+1),
    'Age': np.random.randint(18, 75, size=n),
    'Gender': np.random.choice(genders, size=n),
    'Region': np.random.choice(regions, size=n),
    'Employment_Status': np.random.choice(employment_statuses, size=n),
    'Education_Level': np.random.choice(education_levels, size=n),
    'Years_Driving': np.random.randint(1, 57, size=n),
    'Car_Make': [],
    'Car_Model': [],
    'Manufacture_Year': np.random.randint(2000, 2024, size=n),
    'Annual Mileage': np.random.randint(5000, 60000, size=n),
    'Number_of_Accidents': np.random.poisson(0.5, size=n),
    'Number_of_Claims': np.random.poisson(0.3, size=n),
    'Car_Value': np.random.randint(50000, 1500000, size=n),
    'Premium_Amount': [],
    'Marital_Status': np.random.choice(marital_statuses, size=n),
    'Has_AntiTheft_Device': np.random.choice([0, 1], size=n),
    'Policy_Term': np.random.choice([6, 12, 24], size=n),
    'Credit_Score': np.random.randint(300, 850, size=n),
    'Vehicle_Usage': np.random.choice(vehicle_usages, size=n)
}

# Populate Car_Make and Car_Model
for _ in range(n):
    make = random.choice(list(car_makes_models.keys()))
    model = random.choice(car_makes_models[make])
    data['Car_Make'].append(make)
    data['Car_Model'].append(model)

# Generate Premium_Amount(in ZAR per month) using a basic formula
base_premium = 300  # base premium in ZAR
premium_factors = (
    base_premium +
    0.02 * data['Car_Value'] +
    5 * data['Number_of_Accidents'] +
    3 * data['Number_of_Claims'] -
    0.1 * data['Credit_Score'] -
    2 * data['Years_Driving'] +
    50 * (np.array(data['Vehicle_Usage']) == 'Commercial').astype(int) +
    25 * (np.array(data['Vehicle_Usage']) == 'Business').astype(int) -
    20 * np.array(data['Has_AntiTheft_Device'])
)

# Ensure that the premium amount will always be greater than or equal to R200
data['Premium_Amount'] = np.maximum(200, premium_factors.astype(int))

# Create DataFrame
df = pd.DataFrame

# Save to CSV
file_path = ("/data/raw/car_insurance_premiums_dataset.csv")
df.to_csv(file_path, index=False)
file_path
