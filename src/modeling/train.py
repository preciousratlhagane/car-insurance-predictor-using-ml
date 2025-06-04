import os
import sys
import joblib
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
df_processed.columns

# Define target variable and the features
X = df_processed.drop(columns=['Premium_Amount'])
y = df_processed['Premium_Amount']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
X_train.columns

# Isolate the numeric features to scale them only
all_numeric_columns = X_train.select_dtypes(include='number')
columns_to_scale = all_numeric_columns.loc[:,
                                           all_numeric_columns.dtypes != 'uint8'].columns

columns_to_leave_as = [
    col for col in X_train.columns if col not in columns_to_scale]

# Scale only the numeric columns based on the training data
scaler = StandardScaler()
X_train_scaled_part = scaler.fit_transform(X_train[columns_to_scale])
X_test_scaled_part = scaler.transform(X_test[columns_to_scale])

# Combine the numeric columns with the non-numeric columns
X_train_scaled = np.hstack(
    [X_train_scaled_part, X_train[columns_to_leave_as].values])
X_test_scaled = np.hstack(
    [X_test_scaled_part, X_test[columns_to_leave_as].values])

# Define the models and their respective parameters
models = {
    "Random Forest": RandomForestRegressor(n_estimators=80, max_depth=10, random_state=42),
    "Ridge": Ridge(alpha=1.0),
    "XGBoost": XGBRegressor(n_estimators=80, max_depth=6, learning_rate=0.1, random_state=42)
}

# Store the results of the evaluation metrics of the different models
model_results = {}
metrics_list = []

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
    mae_percentage = np.mean(np.abs((y_test - y_test_pred) / y_test)) * 100

    # Save to dictionary
    model_results[model_name] = {
        "model": model,
        "MAE_Train": mae_train,
        "RMSE_Train": rmse_train,
        "R2_Train": r2_train,
        "MAE_Test": mae_test,
        "RMSE_Test": rmse_test,
        "R2_Test": r2_test,
        "MAPE_Test": mae_percentage
    }

    metrics_list.append({
        "model": model,
        "MAE_Train": mae_train,
        "RMSE_Train": rmse_train,
        "R2_Train": r2_train,
        "MAE_Test": mae_test,
        "RMSE_Test": rmse_test,
        "R2_Test": r2_test,
        "MAPE_Test (%)": mae_percentage
    })


# Define the save directory to save the trained models and the metrics list
save_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "models"))
os.makedirs(save_dir, exist_ok=True)


# Save the metrics into a pandas dataframe
metrics_df = pd.DataFrame(metrics_list)
metrics_df.to_csv(os.path.join(save_dir, "model_metrics.csv"), index=False)


# Save trained models using joblib
for model_name, results in model_results.items():
    model_file = os.path.join(
        save_dir, f"{model_name.replace(' ', '_').lower()}_model.joblib")
    joblib.dump(results["model"], model_file)

# Save the fitted scaler
scaler_file = os.path.join(save_dir, "scaler.joblib")
joblib.dump((scaler, columns_to_scale.tolist()), scaler_file)

# Save the model features
model_features = list(X_train.columns)
features_file = os.path.join(save_dir, "model_features.joblib")
joblib.dump(model_features, features_file)
