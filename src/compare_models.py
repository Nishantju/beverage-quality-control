from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB



from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


from preprocess import (
    load_dataset,
    drop_columns,
    convert_to_numeric,
    handle_missing_values,
    encode_categorical_features,
    split_features_target,
    encode_target,
    train_test_split_data,
    scale_features
)

from config import DATASETS

import joblib

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



dataset_info = DATASETS["orange"]

df = load_dataset(dataset_info["file_path"])

df = drop_columns(
    df,
    dataset_info["drop_columns"]
)

for column in dataset_info["numeric_columns"]:
    df = convert_to_numeric(df, column)

df = handle_missing_values(df)

if "categorical_columns" in dataset_info:

    df, encoders = encode_categorical_features(
        df,
        dataset_info["categorical_columns"]
    )



X, y = split_features_target(
    df,
    dataset_info["target_column"]
)

y, encoder = encode_target(y)

X_train, X_test, y_train, y_test = train_test_split_data(X, y)

X_train, X_test, scaler = scale_features(
    X_train,
    X_test
)



print("\n" + "=" * 60)
print("LOGISTIC REGRESSION")
print("=" * 60)

lr_model = LogisticRegression(random_state=42)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)



lr_precision = precision_score(
    y_test,
    lr_predictions,
    average="weighted"
)

lr_recall = recall_score(
    y_test,
    lr_predictions,
    average="weighted"
)

lr_f1 = f1_score(
    y_test,
    lr_predictions,
    average="weighted"
)





lr_accuracy = accuracy_score(
    y_test,
    lr_predictions
)

print(f"Accuracy  : {lr_accuracy:.4f}")
print(f"Precision : {lr_precision:.4f}")
print(f"Recall    : {lr_recall:.4f}")
print(f"F1 Score  : {lr_f1:.4f}")

print("\n" + "=" * 60)
print("SUPPORT VECTOR MACHINE")
print("=" * 60)

svm_model = SVC(
    probability=True,
    random_state=42
)

svm_model.fit(X_train, y_train)

svm_predictions = svm_model.predict(X_test)



svm_precision = precision_score(
    y_test,
    svm_predictions,
    average="weighted"
)

svm_recall = recall_score(
    y_test,
    svm_predictions,
    average="weighted"
)

svm_f1 = f1_score(
    y_test,
    svm_predictions,
    average="weighted"
)





svm_accuracy = accuracy_score(
    y_test,
    svm_predictions
)


print(f"Accuracy  : {svm_accuracy:.4f}")
print(f"Precision : {svm_precision:.4f}")
print(f"Recall    : {svm_recall:.4f}")
print(f"F1 Score  : {svm_f1:.4f}")


print("\n" + "=" * 60)
print("GAUSSIAN NAIVE BAYES")
print("=" * 60)

nb_model = GaussianNB()

nb_model.fit(X_train, y_train)

nb_predictions = nb_model.predict(X_test)



nb_precision = precision_score(
    y_test,
    nb_predictions,
    average="weighted"
)

nb_recall = recall_score(
    y_test,
    nb_predictions,
    average="weighted"
)

nb_f1 = f1_score(
    y_test,
    nb_predictions,
    average="weighted"
)






nb_accuracy = accuracy_score(
    y_test,
    nb_predictions
)

print(f"Accuracy  : {nb_accuracy:.4f}")
print(f"Precision : {nb_precision:.4f}")
print(f"Recall    : {nb_recall:.4f}")
print(f"F1 Score  : {nb_f1:.4f}")

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(f"Logistic Regression : {lr_accuracy:.4f}")
print(f"SVM                 : {svm_accuracy:.4f}")
print(f"Naive Bayes         : {nb_accuracy:.4f}")


joblib.dump(lr_model, BASE_DIR / "models"/"orange_logistic_model.pkl")
joblib.dump(svm_model, BASE_DIR / "models"/"orange_svm_model.pkl")
joblib.dump(nb_model, BASE_DIR/"models"/"orange_naive_bayes_model.pkl")
joblib.dump(scaler, BASE_DIR/ "models"/"orange_scaler.pkl")
joblib.dump(encoder, BASE_DIR/"models"/"orange_encoder.pkl")


import json

metrics = {

    "Logistic Regression": {
        "accuracy": round(lr_accuracy * 100, 2),
        "precision": round(lr_precision * 100, 2),
        "recall": round(lr_recall * 100, 2),
        "f1_score": round(lr_f1 * 100, 2)
    },

    "SVM": {
        "accuracy": round(svm_accuracy * 100, 2),
        "precision": round(svm_precision * 100, 2),
        "recall": round(svm_recall * 100, 2),
        "f1_score": round(svm_f1 * 100, 2)
    },

    "Naive Bayes": {
        "accuracy": round(nb_accuracy * 100, 2),
        "precision": round(nb_precision * 100, 2),
        "recall": round(nb_recall * 100, 2),
        "f1_score": round(nb_f1 * 100, 2)
    }

}

with open(BASE_DIR / "models" / "orange_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)
