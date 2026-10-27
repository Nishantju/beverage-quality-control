from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

import joblib

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


from preprocess import (
    load_dataset,
    drop_columns,
    convert_to_numeric,
    encode_categorical_features,
    handle_missing_values,
    split_features_target,
    encode_target,
    train_test_split_data,
    scale_features,
)

from config import DATASETS


dataset_name = "orange"

dataset_info = DATASETS[dataset_name]

df = load_dataset(dataset_info["file_path"])

df = drop_columns(df, dataset_info["drop_columns"])

if "categorical_columns" in dataset_info:

    df, categorical_encoders = encode_categorical_features(
        df,
        dataset_info["categorical_columns"]
    )

for column in dataset_info["numeric_columns"]:
    df = convert_to_numeric(df, column)

df = handle_missing_values(df)

X, y = split_features_target(df, dataset_info["target_column"])

y, encoder = encode_target(y)

X_train, X_test, y_train, y_test = train_test_split_data(X, y)

X_train, X_test, scaler = scale_features(X_train, X_test)


print("\n" + "=" * 60)
print("Training Logistic Regression")
print("=" * 60)

lr_model = LogisticRegression(random_state=42)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_predictions)

print(f"Accuracy : {lr_accuracy:.4f}")

joblib.dump(
    lr_model,
    f"../models/{dataset_name}_logistic_model.pkl"
)



print("\n" + "=" * 60)
print("Training Support Vector Machine")
print("=" * 60)

svm_model = SVC(
    probability=True,
    random_state=42
)

svm_model.fit(X_train, y_train)

svm_predictions = svm_model.predict(X_test)

svm_accuracy = accuracy_score(y_test, svm_predictions)

print(f"Accuracy : {svm_accuracy:.4f}")

joblib.dump(
    svm_model,
    f"../models/{dataset_name}_svm_model.pkl"
)



print("\n" + "=" * 60)
print("Training Gaussian Naive Bayes")
print("=" * 60)

nb_model = GaussianNB()

nb_model.fit(X_train, y_train)

nb_predictions = nb_model.predict(X_test)

nb_accuracy = accuracy_score(y_test, nb_predictions)

print(f"Accuracy : {nb_accuracy:.4f}")

joblib.dump(
    nb_model,
    f"../models/{dataset_name}_naive_bayes_model.pkl"
)

joblib.dump(
    scaler,
    f"../models/{dataset_name}_scaler.pkl"
)

joblib.dump(
    encoder,
    f"../models/{dataset_name}_encoder.pkl"
)

if "categorical_columns" in dataset_info:

    joblib.dump(
        categorical_encoders,
        f"../models/{dataset_name}_categorical_encoders.pkl"
    )


print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(f"Logistic Regression : {lr_accuracy:.4f}")
print(f"Support Vector Machine : {svm_accuracy:.4f}")
print(f"Gaussian Naive Bayes : {nb_accuracy:.4f}")

print("\nAll models saved successfully!")