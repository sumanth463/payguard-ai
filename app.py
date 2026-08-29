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
    hour_of_day: float = 12.0     # 0-23, defaults to noon
    time_since_last_txn: float = 3600.0  # seconds since the account's last transaction


def build_feature_row(txn: Transaction) -> pd.DataFrame:
    """
    The real dataset's columns (V1...V28) are anonymized PCA features we can't
    recreate from raw input. For the live demo, we approximate a feature vector
    using the transaction's Amount and Time, and zero out the anonymized
    components — the model still responds meaningfully to Amount/Time shifts,
    which is what we want for a demo. This is documented in the README/pitch
    as a known simplification of the public dataset's anonymized features.
    """
    row = {col: 0.0 for col in columns}
    row["Amount"] = txn.amount
    row["Time"] = txn.time_since_last_txn
    return pd.DataFrame([row])[columns]


def explain(txn: Transaction, risk_score: float) -> str:
    reasons = []
    if txn.amount > 2000:
        reasons.append("the amount is unusually large")
    if txn.hour_of_day < 5 or txn.hour_of_day > 23:
        reasons.append("it happened at an unusual hour")
    if txn.time_since_last_txn < 60:
        reasons.append("it followed the previous transaction unusually fast")

    if risk_score > 0.7:
        if not reasons:
            reasons.append("its overall pattern statistically resembles known fraud cases")
        return "Flagged as high risk because " + ", and ".join(reasons) + "."
    elif risk_score > 0.4:
        return "Marked as medium risk — some signals look slightly unusual, but not conclusive."
    else:
        return "Looks normal — consistent with the account's typical transaction pattern."


@app.post("/check")
def check_transaction(txn: Transaction):
    row = build_feature_row(txn)
    risk_score = float(model.predict_proba(row)[0][1])
    flagged = risk_score > 0.5
    return {
        "risk_score": round(risk_score, 3),
        "flagged": flagged,
        "explanation": explain(txn, risk_score),
    }


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")
