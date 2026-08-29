"""
train_model.py
Trains a fraud-detection classifier on the Kaggle "Credit Card Fraud Detection" dataset
and saves it to fraud_model.pkl for the API (app.py) to use.

Beginner note: just run `python train_model.py` after placing creditcard.csv in this folder.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report
import joblib

# If your laptop is slow, lower this (e.g. 0.3 = use 30% of the data)
sample_frac = 1.0

print("Loading dataset...")
df = pd.read_csv("creditcard.csv")

if sample_frac < 1.0:
    df = df.sample(frac=sample_frac, random_state=42)

# Features: all columns except the label
X = df.drop(columns=["Class"])
y = df["Class"]  # 1 = fraud, 0 = normal

print(f"Loaded {len(df)} transactions ({y.sum()} fraud cases).")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Training model (RandomForest)...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    class_weight="balanced",  # important: fraud is rare, this handles imbalance
    random_state=42,
    n_jobs=-1,
)
model.fit(X_train, y_train)

# Evaluate
probs = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, probs)
print(f"\nModel trained. ROC-AUC: {auc:.3f}")
print("\nClassification report:")
print(classification_report(y_test, model.predict(X_test)))

# Save model + the feature column order (needed by the API)
joblib.dump({"model": model, "columns": list(X.columns)}, "fraud_model.pkl")
print("\nModel saved to fraud_model.pkl")
