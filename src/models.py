from datetime import datetime

from src.database import db


class PredictionHistory(db.Model):

    __tablename__ = "prediction_history"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    beverage = db.Column(
        db.String(50),
        nullable=False
    )

    logistic_quality = db.Column(
        db.String(30),
        nullable=False
    )

    logistic_confidence = db.Column(
        db.Float,
        nullable=False
    )

    svm_quality = db.Column(
        db.String(30),
        nullable=False
    )

    svm_confidence = db.Column(
        db.Float,
        nullable=False
    )

    naive_quality = db.Column(
        db.String(30),
        nullable=False
    )

    naive_confidence = db.Column(
        db.Float,
        nullable=False
    )