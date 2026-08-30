"""
app.py
The AI agent's brain: loads the trained fraud model, scores incoming transactions,
and generates a plain-English explanation for why a transaction was flagged.

Run with: uvicorn app:app --reload
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

app = FastAPI(title="PayGuard AI")

bundle = joblib.load("fraud_model.pkl")
model = bundle["model"]
columns = bundle["columns"]


class Transaction(BaseModel):
    amount: float
    hour_of_day: float = 12.0
    time_since_last_txn: float = 3600.0


def build_feature_row(txn: Transaction) -> pd.DataFrame:
    row = {col: 0.0 for col in columns}
    row["Amount"] = txn.amount
    row["Time"] = txn.time_since_last_txn
    return pd.DataFrame([row])[columns]


def heuristic_risk(txn: Transaction):
    score = 0.0
    reasons = []

    if txn.amount > 50000:
        score += 0.5
        reasons.append("the amount is very large")
    elif txn.amount > 5000:
        score += 0.25
        reasons.append("the amount is unusually large")

    if txn.hour_of_day < 5 or txn.hour_of_day > 23:
        score += 0.3
        reasons.append("it happened at an unusual hour")

    if txn.time_since_last_txn < 30:
        score += 0.35
        reasons.append("it followed the previous transaction unusually fast")
    elif txn.time_since_last_txn < 120:
        score += 0.15
        reasons.append("it followed the previous transaction quickly")

    return min(score, 1.0), reasons


def explain(risk_score, reasons):
    if risk_score > 0.65:
        if not reasons:
            reasons.append("its overall pattern statistically resembles known fraud cases")
        return "Flagged as high risk because " + ", and ".join(reasons) + "."
    elif risk_score > 0.35:
        if reasons:
            return "Marked as medium risk — " + ", and ".join(reasons) + ", but not conclusive on its own."
        return "Marked as medium risk — some signals look slightly unusual, but not conclusive."
    else:
        return "Looks normal — consistent with the account's typical transaction pattern."


@app.post("/check")
def check_transaction(txn: Transaction):
    row = build_feature_row(txn)
    model_score = float(model.predict_proba(row)[0][1])
    rule_score, reasons = heuristic_risk(txn)

    risk_score = max(model_score, rule_score)
    flagged = risk_score > 0.5

    return {
        "risk_score": round(risk_score, 3),
        "flagged": flagged,
        "explanation": explain(risk_score, reasons),
    }


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")