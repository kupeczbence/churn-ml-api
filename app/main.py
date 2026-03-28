from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Customer Churn Prediction API")

model = joblib.load("model/churn_model.joblib")
feature_columns = joblib.load("model/feature_columns.joblib")


class Customer(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def read_root():
    return {"message": "Churn Prediction API is running"}


@app.post("/predict")
def predict(customer: Customer):
    data = pd.DataFrame([customer.dict()])

    # align with training columns
    for col in feature_columns:
        if col not in data.columns:
            data[col] = 0

    data = data[feature_columns]

    proba = model.predict_proba(data)[0][1]
    pred = model.predict(data)[0]

    return {
        "churn_probability": float(proba),
        "prediction": "Churned" if pred == 1 else "Stayed",
    }