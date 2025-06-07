import numpy as np
import pandas as pd


def preprocess_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses the input DataFrame by engineering new features, dropping non-informative columns, and encoding categorical variables. 

    The preprocessing steps include:
        1. Creating a new feature 'Accident_Claim_Rate'
        2. Creating a new feature 'Claims_per_Year'
        3. Dropping the 'Customer ID' column, if it exists, as it is non-informative for modelling.
        4. One-hot encoding all categorical features, dropping the first category in each to avoid multicollinearity.

    Args:
        df (pd.DataFrame): A pandas DataFrame containing the raw feature data, including 'Number_of_Claims', 'Number_of_Accidents', 'Years_Driving', and possibly categorical columns

    Returns:
        pd.DataFrame: A processed DataFrame with additional numerical features and encoded categorical features, ready for use in a machine learning model. 
    """
    # Create a copy of the dataframe
    df = df.copy()

    # Calculate the proportion of the claims to the number of accidents
    df['Accident_Claim_Rate'] = df['Number_of_Claims'] / \
        df['Number_of_Accidents'].replace(0, np.nan)
    df['Accident_Claim_Rate'] = df['Accident_Claim_Rate'].fillna(0)

    # Calculate the claims made per year by each driver
    df['Claims_per_Year'] = df['Number_of_Claims'] / \
        df['Years_Driving'].replace(0, np.nan)
    df['Claims_per_Year'] = df['Claims_per_Year'].fillna(0)

    # Drop only non-useful columns
    df.drop(columns=["Customer_ID"], inplace=True, errors="ignore")

    # One hot-encode categorical features
    categorical_cols = df.select_dtypes(include=object).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df
