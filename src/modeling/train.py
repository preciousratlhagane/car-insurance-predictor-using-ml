import os
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from features import preprocess_features

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load the data
df = pd.read_csv("../data/processed/cleaned_data.csv")

# Preprocess the features
df_processed = preprocess_features(df)

# Define target variable and the features
X = df_processed.drop(columns=['Premium_Amount'])
y = df_processed['Premium_Amount']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predict using the test_set and evaluate
y_pred = model.predict(X_test_scaled)


print("Mean Absoute Error:", mean_absolute_error(y_test, y_pred))
print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R-squared:", r2_score(y_test, y_pred))
