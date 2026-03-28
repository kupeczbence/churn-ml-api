import pandas as pd


def preprocess(df: pd.DataFrame):
    df = df.copy()

    # target mapping if present
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({"Churned": 1, "Stayed": 0})

    # drop id column
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    # fix TotalCharges
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

    # one-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    return df