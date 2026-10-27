"""
=========================================
Data Preprocessing Module
=========================================

Purpose:
    Clean and prepare datasets for
    machine learning.

Author: Nishant Kumar
"""
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
from config import DATASETS
from sklearn.model_selection import train_test_split

def load_dataset(file_path):
    """
    Load a CSV dataset.

    Parameters:
        file_path (str): Path to the dataset.

    Returns:
        pandas.DataFrame
    """

    print("=" * 60)
    print("Loading Dataset...")
    print("=" * 60)

    df = pd.read_csv(file_path)

    print("Dataset loaded successfully.")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df


def drop_columns(df, columns):
    """
    Remove unwanted columns.

    Parameters:
        df (DataFrame): Dataset.
        columns (list): Columns to remove.

    Returns:
        DataFrame
    """

    print("\nRemoving unwanted columns...")

    df = df.drop(columns=columns)

    print("Removed columns:", columns)

    return df

def inspect_column(df, column_name):
    """
    Display useful information about a column.

    Parameters:
        df (DataFrame): Dataset.
        column_name (str): Column to inspect.
    """

    print("\n" + "=" * 60)
    print(f"Inspecting Column : {column_name}")
    print("=" * 60)

    # Data type
    print(f"\nData Type : {df[column_name].dtype}")

    # Missing values
    print(f"Missing Values : {df[column_name].isnull().sum()}")

    # Number of unique values
    print(f"Unique Values : {df[column_name].nunique()}")

    # First 10 values
    print("\nFirst 10 Values")
    print("-" * 60)
    print(df[column_name].head(10))

def convert_to_numeric(df, column_name):
    """
    Convert a column to numeric values.

    Parameters:
        df (DataFrame): Dataset.
        column_name (str): Column to convert.

    Returns:
        DataFrame
    """

    print("\n" + "=" * 60)
    print(f"Converting '{column_name}' to numeric")
    print("=" * 60)

    # Save original column
    original_column = df[column_name]

    # Convert to numeric
    df[column_name] = pd.to_numeric(
        df[column_name],
        errors="coerce"
    )

    # Find rows that became NaN after conversion
    invalid_rows = df[
        df[column_name].isna() &
        original_column.notna()
    ]

    if len(invalid_rows) == 0:
        print("Conversion successful.")
        print("No invalid values found.")

    else:
        print(f"Invalid values found: {len(invalid_rows)}")

        print("\nInvalid Entries")
        print("-" * 60)

        print(
            invalid_rows[[column_name]]
        )

    print(f"\nNew Data Type : {df[column_name].dtype}")

    return df

def handle_missing_values(df):
    """
    Remove rows containing missing values.

    Parameters:
        df (DataFrame): Dataset

    Returns:
        DataFrame
    """

    print("\n" + "=" * 60)
    print("Handling Missing Values")
    print("=" * 60)

    rows_before = len(df)

    # Remove rows with missing values
    df = df.dropna()

    rows_after = len(df)

    removed_rows = rows_before - rows_after

    print(f"Rows Before : {rows_before}")
    print(f"Rows After  : {rows_after}")
    print(f"Rows Removed: {removed_rows}")

    return df


def split_features_target(df, target_column):
    """
    Split dataset into features (X) and target (y).

    Parameters:
        df (DataFrame)
        target_column (str)

    Returns:
        X, y
    """

    print("\n" + "=" * 60)
    print("Splitting Features and Target")
    print("=" * 60)

    X = df.drop(columns=[target_column])

    y = df[target_column]

    print(f"Features Shape : {X.shape}")
    print(f"Target Shape   : {y.shape}")

    print("\nFeature Columns")
    print("-" * 60)
    print(X.columns.tolist())

    print("\nTarget Column")
    print("-" * 60)
    print(target_column)

    return X, y


def encode_target(y):
    """
    Encode the target labels.

    Parameters:
        y (Series): Target column.

    Returns:
        y_encoded, encoder
    """

    print("\n" + "=" * 60)
    print("Encoding Target")
    print("=" * 60)

    encoder = LabelEncoder()

    y_encoded = encoder.fit_transform(y)

    print("Class Mapping")
    print("-" * 60)

    for label, code in zip(encoder.classes_, encoder.transform(encoder.classes_)):
        print(f"{label} --> {code}")

    return y_encoded, encoder

def train_test_split_data(X, y):
    """
    Split the dataset into training and testing sets.
    """

    print("\n" + "=" * 60)
    print("Splitting Training and Testing Data")
    print("=" * 60)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print(f"Training Samples : {len(X_train)}")
    print(f"Testing Samples  : {len(X_test)}")

    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    """
    Scale the training and testing features.
    """

    print("\n" + "=" * 60)
    print("Scaling Features")
    print("=" * 60)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    print("Training Shape :", X_train_scaled.shape)
    print("Testing Shape  :", X_test_scaled.shape)

    return X_train_scaled, X_test_scaled, scaler



def encode_categorical_features(dataframe, categorical_columns):

    print("\n" + "=" * 60)
    print("Encoding Categorical Features")
    print("=" * 60)

    encoders = {}

    for column in categorical_columns:

        print(f"\nEncoding '{column}'")

        encoder = LabelEncoder()

        dataframe[column] = encoder.fit_transform(
            dataframe[column].astype(str)
        )

        encoders[column] = encoder

        print("Classes:")
        for index, value in enumerate(encoder.classes_):
            print(f"{value} --> {index}")

    return dataframe, encoders






if __name__ == "__main__":

    dataset_name = "apple"

    dataset_info = DATASETS[dataset_name]

    df = load_dataset(dataset_info["file_path"])

    df = drop_columns(
        df,
        dataset_info["drop_columns"]
    )

    print("\nCurrent Columns")
    print(df.columns.tolist())
    for column in dataset_info["numeric_columns"]:

        inspect_column(df, column)

        df = convert_to_numeric(df, column)
    df = handle_missing_values(df)

    X, y = split_features_target(
        df,
        dataset_info["target_column"]
    )


    y, encoder = encode_target(y)
    X_train, X_test, y_train, y_test = train_test_split_data(X, y)
    X_train, X_test, scaler = scale_features(X_train, X_test)
    print("\nFirst 10 Encoded Values")
    print("-" * 60)
    print(y[:10])




    print("\nFinal Dataset Shape")
    print(df.shape)