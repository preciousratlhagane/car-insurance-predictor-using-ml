import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def preprocess_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop only non-useful columns
    df.drop(columns=["Customer_ID"], inplace=True)

    # One hot-encode categorical features
    categorical_cols = [
        'Gender', 'Region', 'Employment_Status', 'Education_Level',
        'Car_Make', 'Car_Model', 'Marital_Status', 'Vehicle_Usage'
    ]

    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df
