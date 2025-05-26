import os
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

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


# Isolate the numeric features to scale them only
numeric_columns = X_train.select_dtypes(include=['float64', 'int64']).columns
ohe_col = [col for col in numeric_columns if col != 'Premium_Amount']

X_train_numeric = X_train[numeric_columns]
X_train_ohe = X_train[ohe_col]

X_test_numeric = X_test[numeric_columns]
X_test_ohe = X_test[ohe_col]


# Scale only the numeric columns based on the training data
scaler = StandardScaler()
X_train_numeric_scaled = scaler.fit_transform(X_train_numeric)
X_test_numeric_scaled = scaler.transform(X_test_numeric)

# Combine the numeric columns with the non-numeric columns
X_train_scaled = np.hstack([X_train_numeric_scaled, X_train_ohe.values])
X_test_scaled = np.hstack([X_test_numeric_scaled, X_test_ohe.values])

# Define the models and their respective parameters
models = {
    "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42),
    "Ridge": Ridge(alpha=1.0),
    "XGBoost": XGBRegressor(n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42)
}

# Store the results of the evaluation metrics of the different models
model_results = {}

# Evaluate each model
for model_name, model in models.items():
    model.fit(X_train_scaled, y_train)

    # Predict on train and test sets
    y_train_pred = model.predict(X_train_scaled)
    y_test_pred = model.predict(X_test_scaled)

    # Training performance
    mae_train = mean_absolute_error(y_train, y_train_pred)
    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
    r2_train = r2_score(y_train, y_train_pred)

    # Test performance
    mae_test = mean_absolute_error(y_test, y_test_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    r2_test = r2_score(y_test, y_test_pred)

    # Save to dictionary
    model_results[model_name] = {
        "model": model,
        "MAE_Train": mae_train,
        "RMSE_Train": rmse_train,
        "R2_Train": r2_train,
        "MAE_Test": mae_test,
        "RMSE_Test": rmse_test,
        "R2_Test": r2_test
    }

    # Print results
    print(f"--- {model_name} ---")
    print(
        f"Train -> MAE: {mae_train:.2f}, RMSE: {rmse_train:.2f}, R²: {r2_train:.6f}")
    print(
        f"Test  -> MAE: {mae_test:.2f}, RMSE: {rmse_test:.2f}, R²: {r2_test:.6f}\n")
