"""
=========================================
Prediction Module
=========================================

Purpose:
    Predict apple quality using
    the trained AI model.

Author: Nishant Kumar
"""

import joblib
import numpy as np
import pandas as pd

def load_saved_files():
    """
    Load the trained model, scaler,
    and label encoder.
    """

    print("=" * 60)
    print("Loading Saved AI Model")
    print("=" * 60)

    model = joblib.load("../models/apple_model.pkl")
    scaler = joblib.load("../models/apple_scaler.pkl")
    encoder = joblib.load("../models/apple_encoder.pkl")

    print("Model Loaded Successfully!")

    return model, scaler, encoder

def get_user_input():
    """
    Get feature values from the user.
    """

    print("\n" + "=" * 60)
    print("Enter Apple Information")
    print("=" * 60)

    size = float(input("Size         : "))
    weight = float(input("Weight       : "))
    sweetness = float(input("Sweetness    : "))
    crunchiness = float(input("Crunchiness  : "))
    juiciness = float(input("Juiciness    : "))
    ripeness = float(input("Ripeness     : "))
    acidity = float(input("Acidity      : "))

    features = pd.DataFrame(
        [[
            size,
            weight,
            sweetness,
            crunchiness,
            juiciness,
            ripeness,
            acidity
        ]],
        columns=[
            "Size",
            "Weight",
            "Sweetness",
            "Crunchiness",
            "Juiciness",
            "Ripeness",
            "Acidity"
        ]
    )

    return features



def predict_quality(model, scaler, encoder, features):
    """
    Predict apple quality.
    """

    print("\n" + "=" * 60)
    print("Predicting Apple Quality")
    print("=" * 60)

    # Scale features
    features_scaled = scaler.transform(features)

    # Predict class
    prediction = model.predict(features_scaled)

    # Predict probabilities
    probabilities = model.predict_proba(features_scaled)

    # Decode prediction
    quality = encoder.inverse_transform(prediction)[0]

    print("Prediction Complete!")

    return quality, probabilities[0]


if __name__ == "__main__":

    model, scaler, encoder = load_saved_files()

    features = get_user_input()

    quality, probabilities = predict_quality(
        model,
        scaler,
        encoder,
        features
    )

    bad_probability = probabilities[0] * 100
    good_probability = probabilities[1] * 100

    confidence = max(good_probability, bad_probability)

    print("\n" + "=" * 60)
    print("APPLE QUALITY PREDICTION")
    print("=" * 60)

    print(f"Prediction : {quality.upper()}")
    print(f"Confidence : {confidence:.2f}%")

    print("\nProbabilities")
    print("-" * 60)
    print(f"GOOD : {good_probability:.2f}%")
    print(f"BAD  : {bad_probability:.2f}%")