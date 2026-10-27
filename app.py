"""
=========================================
Flask Web Application
=========================================

Purpose:
    Web interface for Apple Quality
    Prediction.

Author: Nishant Kumar
"""
from src.database import configure_database, db
from src.models import PredictionHistory







import joblib
import numpy as np

from flask import Flask, render_template, request



from src.config import (
    FORM_OPTIONS,
    REQUIRED_FIELDS,
    FIELD_LABELS,
    INPUT_FIELDS
)

app = Flask(__name__)




configure_database(app)
with app.app_context():
    db.create_all()




def orange_quality_grade(score):

    if score == 5.0:
        return "🏆 Premium"

    elif score == 4.5:
        return "⭐ Excellent"

    elif score == 4.0:
        return "🟢 Very Good"

    elif score == 3.5:
        return "🟢 Good"

    elif score == 3.0:
        return "🟡 Average"

    elif score == 2.5:
        return "🟠 Below Average"

    elif score == 2.0:
        return "🔶 Poor"

    else:
        return "🔴 Very Poor"




@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        beverage = request.form.get("beverage")

        if beverage not in ["apple", "banana", "milk", "orange"]:
            return render_template(
                "index.html",
                beverage="",
                options={},
                error="Please select a beverage."
            )

        required_fields = REQUIRED_FIELDS[beverage]

        for field in required_fields:

            value = request.form.get(field)

            if value is None or value.strip() == "":

                field_name = FIELD_LABELS.get(field, field)

                if field in ["variety", "region", "ripeness_category"]:
                    error = f"Please select {field_name}."
                else:
                    error = f"Please enter {field_name}."

                return render_template(
                    "index.html",
                    beverage=beverage,
                    options=FORM_OPTIONS.get(beverage, {}),
                    error=error
                )

        logistic_model = joblib.load(
            f"models/{beverage}_logistic_model.pkl"
        )

        svm_model = joblib.load(
            f"models/{beverage}_svm_model.pkl"
        )

        naive_model = joblib.load(
            f"models/{beverage}_naive_bayes_model.pkl"
        )

        scaler = joblib.load(
            f"models/{beverage}_scaler.pkl"
        )

        encoder = joblib.load(
            f"models/{beverage}_encoder.pkl"
        )

        categorical_encoders = None

        if beverage == "orange":

            categorical_encoders = joblib.load(
                f"models/{beverage}_categorical_encoders.pkl"
            )


        feature_values = []


        for field in INPUT_FIELDS[beverage]:

            value = request.form[field]

            if (
                beverage == "orange"
                and field in categorical_encoders
            ):

                value = categorical_encoders[field].transform(
                    [value]
                )[0]

            feature_values.append(float(value))

        user_input = np.array([feature_values])

        user_input = scaler.transform(user_input)

        # Logistic Regression
        lr_prediction = logistic_model.predict(user_input)
        lr_confidence = logistic_model.predict_proba(user_input).max() * 100
        lr_result = encoder.inverse_transform(lr_prediction)[0]

        # Support Vector Machine
        svm_prediction = svm_model.predict(user_input)
        svm_confidence = svm_model.predict_proba(user_input).max() * 100
        svm_result = encoder.inverse_transform(svm_prediction)[0]

        # Gaussian Naive Bayes
        nb_prediction = naive_model.predict(user_input)
        nb_confidence = naive_model.predict_proba(user_input).max() * 100
        nb_result = encoder.inverse_transform(nb_prediction)[0]


        if beverage == "orange":

            lr_result = (
                f"{orange_quality_grade(lr_result)} "
                f"({lr_result}/5)"
            )

            svm_result = (
                f"{orange_quality_grade(svm_result)} "
                f"({svm_result}/5)"
            )

            nb_result = (
                f"{orange_quality_grade(nb_result)} "
                f"({nb_result}/5)"
            )

        else:

            lr_result = str(lr_result).upper()
            svm_result = str(svm_result).upper()
            nb_result = str(nb_result).upper()



        history = PredictionHistory(

            beverage=beverage.title(),

            logistic_quality=lr_result,
            logistic_confidence=float(round(lr_confidence, 2)),

            svm_quality=svm_result,
            svm_confidence=float(round(svm_confidence, 2)),

            naive_quality=nb_result,
            naive_confidence=float(round(nb_confidence, 2))

        )

        db.session.add(history)
        db.session.commit()





        options = FORM_OPTIONS.get(beverage, {})
        return render_template(
            "index.html",

            beverage=beverage,
            options=options,

            lr_prediction=lr_result,
            lr_confidence=round(lr_confidence, 2),

            svm_prediction=svm_result,
            svm_confidence=round(svm_confidence, 2),

            nb_prediction=nb_result,
            nb_confidence=round(nb_confidence, 2)
        )

    beverage = request.args.get("beverage", "")

    options = FORM_OPTIONS.get(beverage, {})

    return render_template(
        "index.html",
        beverage=beverage,
        options=FORM_OPTIONS.get(beverage, {}),
    )


@app.route("/history")
def history():

    predictions = (
        PredictionHistory.query
        .order_by(PredictionHistory.created_at.desc())
        .all()
    )

    return render_template(
        "history.html",
        history=predictions
    )


@app.route("/analytics")
def analytics():

    all_predictions = PredictionHistory.query.all()

    beverages = ["Apple", "Banana", "Milk", "Orange"]
    total_predictions = len(all_predictions)

    beverage_counts = {
        "Apple": 0,
        "Banana": 0,
        "Milk": 0,
        "Orange": 0
    }


    logistic_total = 0
    svm_total = 0
    naive_total = 0

    for prediction in all_predictions:

        if prediction.beverage in beverage_counts:
            beverage_counts[prediction.beverage] += 1

        logistic_total += prediction.logistic_confidence
        svm_total += prediction.svm_confidence
        naive_total += prediction.naive_confidence

    if total_predictions > 0:

        logistic_average = round(
            logistic_total / total_predictions,
            2
        )

        svm_average = round(
            svm_total / total_predictions,
            2
        )

        naive_average = round(
            naive_total / total_predictions,
            2
        )

    else:

        logistic_average = 0
        svm_average = 0
        naive_average = 0


    return render_template(

        "analytics.html",

        total_predictions=total_predictions,

        logistic_average=logistic_average,
        svm_average=svm_average,
        naive_average=naive_average,

        beverages=beverages,
        beverage_counts=[
            beverage_counts[beverage] for beverage in beverages
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)