import pandas as pd
import numpy as np


def preprocess_features(df: pd.DataFrame) -> pd.DataFrame:
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
