from collections import Counter

import pandas as pd


def fix_invalid_education_rows(data: pd.DataFrame) -> pd.DataFrame:
    """
    Removes rows from the dataframe where the individual's age is below the minimu required for their reported education level.

    The function assumes the following minimum age thresholds:
    - High School: 18
    - Diploma: 18
    - Degree: 18
    - Postgraduate: 21

    Rows with education levels not listed in the thresholds are removed by default.

    Args:
        data (pd.DataFrame): A pandas DataFrame containing at least the columns 'Age' and 'Education_Level'.

    Returns:
        pd.DataFrame: A filtered DataFrame with only valid education level entries.
    """
    minimum_age_for_education_level = {
        "High School": 18,
        "Diploma": 18,
        "Degree": 18,
        "Postgraduate": 21,
    }

    data = data[data.apply(
        lambda row: row["Age"] >= minimum_age_for_education_level.get(row["Education_Level"], float('inf')), axis=1)]

    return data


def fix_employment_status(data: pd.DataFrame) -> pd.DataFrame:
    """
    Corrects inconsistent employment status entries based on age constraints and rebalances the distribution toward a defined target distribution.

    The function performs two main tasks:
        1. Validates each individual's employment status against their age using the following rules:
            - Unemployed: 18-65 years
            - Student: 18-35 years
            - Employed: 16-65 years
            - Self-Employed: 18-80 years
            - Retired: 65-100 years
        2. If the individual's current employment status does not fit within the valid age range, a new status is assigned from the valid options based on the closest match to a target employment status distribution. 

    Target employment status distribution:
        - Retired: 25.7376%
        - Student: 25.6475%
        - Employed: 25.0567%
        - Unemployed: 24.8917%
        - Self-Employed: 24.2140%

    Args:
        data (pd.DataFrame): A pandas DataFrame containing at least the columns 'Age' and 'Employment_Status'.

    Returns:
        pd.DataFrame: A DataFrame where all the employment status entries are age-appropriate and approximately balanced toward the target distribution.
    """
    employment_age_limits = {
        "Unemployed": (18, 65),
        "Student": (18, 35),
        "Employed": (18, 65),
        "Self-Employed": (18, 80),
        "Retired": (65, 100)
    }

    target_distribution = {
        "Retired": 0.257376,
        "Student": 0.256475,
        "Employed": 0.250567,
        "Unemployed": 0.248917,
        "Self-Employed": 0.243140
    }

    total_rows = len(data)
    current_counts = Counter(data["Employment_Status"])

    def fix_employment_smart(row):
        age = row["Age"]
        current_status = row["Employment_Status"]

        min_age, max_age = employment_age_limits.get(current_status, (0, 150))
        if min_age <= age <= max_age:
            return current_status

        valid_statuses = [
            status for status, (min_a, max_a) in employment_age_limits.items()
            if min_a <= age <= max_a
        ]

        if not valid_statuses:
            return current_status

        best_status = None
        smallest_gap = float("inf")
        for status in valid_statuses:
            current_prop = current_counts[status] / total_rows
            target_prop = target_distribution.get(status, 0)
            gap = abs(target_prop - current_prop)
            if gap < smallest_gap:
                smallest_gap = gap
                best_status = status

        current_counts[best_status] += 1
        return best_status

    data["Employment_Status"] = data.apply(fix_employment_smart, axis=1)
    return data


def fix_invalid_driving_years(data: pd.DataFrame) -> pd.DataFrame:
    """
    Corrects entries in the 'Years_Driving' column that exceed the maximum possible driving years based on the individual's age. 

    Assumes the minimum legal driving age is 18. Therefore, the maximum possible driving years for an individual is (Age - 18).

    For any record where 'Years_Driving' exceeds this maximum, the value is capped to (Age - 18).
    Args:
        data (pd.DataFrame): A pandas DataFrame containing at least the columns 'Age' and 'Years_Driving'.

    Returns:
        pd.DataFrame: A DataFrame with corrected 'Years_Driving' values that do not exceed what is possible based on the individual's age.
    """
    max_driving_years = data["Age"] - 18
    invalid_driving_years = data["Years_Driving"] > max_driving_years

    data.loc[invalid_driving_years,
             'Years_Driving'] = max_driving_years[invalid_driving_years]
    return data


def clean_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input dataset by applying a series of data quality checks and corrections.

    The cleaning process includes:
        1. Dropping rows that are completely empty.
        2. Removing duplicate rows and resetting the index.
        3. Removing the rows with invalid education levels based on age.
        4. Fixing employment statuses that are inconsistent with the individual's age, while balancing the overall distribution.
        5. Capping 'Years_Driving' values that exceed the maximum possible based on age.

    Args:
        data (pd.DataFrame): A pandas DataFrame containing at least the columns 'Age', 'Education_Level', 'Employment_Status', and 'Years_Driving'

    Returns:
        pd.DataFrame: A cleaned and corrected DataFrame with improved data consistency. 
    """
    data = data.dropna(how="all")
    data = data.drop_duplicates().reset_index(drop=True)
    data = fix_invalid_education_rows(data)
    data = fix_employment_status(data)
    data = fix_invalid_driving_years(data)
    return data
