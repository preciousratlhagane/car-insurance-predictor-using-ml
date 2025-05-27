import pandas as pd
from collections import Counter


def fix_invalid_education_rows(data: pd.DataFrame) -> pd.DataFrame:
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
    max_driving_years = data["Age"] - 18
    invalid_driving_years = data["Years_Driving"] > max_driving_years

    data.loc[invalid_driving_years,
             'Years_Driving'] = max_driving_years[invalid_driving_years]
    return data


def clean_dataset(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna(how="all")
    data = data.drop_duplicates().reset_index(drop=True)
    data = fix_invalid_education_rows(data)
    data = fix_employment_status(data)
    data = fix_invalid_driving_years(data)
    return data
