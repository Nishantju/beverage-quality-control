"""
=========================================
Dataset Exploration Module
=========================================

Purpose:
    Explore any beverage dataset before
    preprocessing and model training.

Author: Nishant Kumar
"""
from config import DATASETS
import pandas as pd


def explore_dataset(file_path):

    print("=" * 70)
    print("DATASET INFORMATION")
    print("=" * 70)

    # -----------------------------
    # Load Dataset
    # -----------------------------
    df = pd.read_csv(file_path)

    # -----------------------------
    # Basic Information
    # -----------------------------
    print(f"\nRows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")
    print("-" * 70)
    print(df.columns.tolist())

    print("\nData Types")
    print("-" * 70)
    print(df.dtypes)

    # -----------------------------
    # Missing Values
    # -----------------------------
    missing = df.isnull().sum()

    print("\nMissing Values")
    print("-" * 70)
    print(missing)

    # -----------------------------
    # Duplicate Rows
    # -----------------------------
    duplicates = df.duplicated().sum()

    print("\nDuplicate Rows")
    print("-" * 70)
    print(duplicates)

    # -----------------------------
    # Numerical / Categorical
    # -----------------------------
    numerical_columns = df.select_dtypes(include=["number"]).columns.tolist()

    categorical_columns = df.select_dtypes(exclude=["number"]).columns.tolist()

    print("\nNumerical Columns")
    print("-" * 70)
    print(numerical_columns)

    print("\nCategorical Columns")
    print("-" * 70)
    print(categorical_columns)

    # -----------------------------
    # Target Classes
    # -----------------------------
    if "Quality" in df.columns:

        print("\nQuality Classes")
        print("-" * 70)
        print(df["Quality"].value_counts(dropna=False))

    # -----------------------------
    # Dataset Quality Report
    # -----------------------------
    print("\n" + "=" * 70)
    print("DATA QUALITY REPORT")
    print("=" * 70)

    print(f"Total Rows          : {len(df)}")
    print(f"Missing Values      : {missing.sum()}")
    print(f"Duplicate Rows      : {duplicates}")
    print(f"Numerical Columns   : {len(numerical_columns)}")
    print(f"Categorical Columns : {len(categorical_columns)}")

    issues = []

    if missing.sum() > 0:
        issues.append("Missing values found.")

    if duplicates > 0:
        issues.append("Duplicate rows found.")

    object_columns = df.select_dtypes(include=["object"]).columns.tolist()

    for column in object_columns:
        if column != "Quality":
            issues.append(f"{column} is stored as text.")

    print("\nDataset Ready?")

    if len(issues) == 0:
        print("YES")
    else:
        print("NO")

        print("\nIssues Found:")

        for issue in issues:
            print(f"- {issue}")

    print("\nExploration Complete!")


if __name__ == "__main__":

    dataset_name = "apple"

    dataset_info = DATASETS[dataset_name]

    explore_dataset(dataset_info["file_path"])