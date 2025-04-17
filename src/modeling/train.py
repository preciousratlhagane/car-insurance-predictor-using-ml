from features import preprocess_features
import os
import sys

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split

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

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict using the test_set and evaluate
y_pred = model.predict(X_test)


print("Mean Absoute Error:", mean_absolute_error(y_test, y_pred))
print("Root Mean Squared Error:", root_mean_squared_error(y_test, y_pred))
print("R-squared:", r2_score(y_test, y_pred))
