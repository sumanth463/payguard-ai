# PayGuard AI — Real-Time Fraud Risk Explainer

An AI agent that looks at a payment transaction, decides if it's risky, and explains **why** in plain English — built for the Razorpay AI Builder Internship 2026 (Track 2: AI Risk Manager).

This README is written for a complete beginner. Follow it top to bottom in order. Don't skip steps.

---

## What you're building

1. A machine learning model that learns from real (anonymized) credit card transactions to spot fraud.
2. A small web server (API) that takes a transaction and returns: `risk_score`, `flagged` (yes/no), and a **plain-English reason**.
3. A simple webpage where you type in transaction details and see the AI's verdict live — this is what you'll record for your pitch video.

---

## Step 1 — Install Python (skip if you already have it)

1. Go to https://www.python.org/downloads/ and install Python 3.10 or newer.
2. During install, on Windows, **check the box "Add Python to PATH"**.
3. Verify it worked — open a terminal (Command Prompt / Terminal app) and type:
   ```
   python --version
   ```
   You should see something like `Python 3.11.5`.

## Step 2 — Get the project folder

You already have this folder (`payguard-ai`). Open a terminal **inside this folder**. On most systems:
- Right-click the folder → "Open in Terminal", or
- `cd path/to/payguard-ai`

## Step 3 — Install the required libraries

Run this in your terminal:
```
pip install -r requirements.txt
```
This installs: pandas, scikit-learn, fastapi, uvicorn, joblib.

## Step 4 — Get the dataset

We use a well-known public dataset of real anonymized credit card transactions (already labeled fraud/not-fraud).

1. Go to: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
2. Sign in with your existing Kaggle account.
3. Click **Download** (it's a ~150MB zip).
4. Unzip it. You'll get a file called `creditcard.csv`.
5. Put `creditcard.csv` inside this `payguard-ai` folder (same folder as `train_model.py`).

## Step 5 — Train the model

Run:
```
python train_model.py
```
This will:
- Load the transactions
- Train a classifier to detect fraud
- Print its accuracy
- Save the trained model as `fraud_model.pkl`

This takes 1–3 minutes. When it finishes you'll see something like:
```
Model trained. ROC-AUC: 0.97
Model saved to fraud_model.pkl
```

## Step 6 — Run the AI server

```
uvicorn app:app --reload
```
Leave this running. Open your browser to:
```
http://127.0.0.1:8000
```
You'll see the PayGuard AI demo page. Try submitting a transaction — it'll show you a risk score and an explanation.

## Step 7 — Push to GitHub (for the "GitHub Repository URL" field)

1. Go to https://github.com and log in (create an account if needed — use the same one as your GitHub profile: github.com/sumanth463).
2. Click **New repository**, name it `payguard-ai`, keep it Public, click **Create repository**.
3. Back in your terminal, inside the `payguard-ai` folder, run:
   ```
   git init
   git add .
   git commit -m "PayGuard AI - fraud risk explainer"
   git branch -M main
   git remote add origin https://github.com/sumanth463/payguard-ai.git
   git push -u origin main
   ```
4. **Important:** Do NOT upload `creditcard.csv` to GitHub (it's too large and not yours to redistribute). Delete it from the folder before `git add .`, or check that `.gitignore` (included) is excluding it.
5. Your repo URL is: `https://github.com/sumanth463/payguard-ai`

## Step 8 — Record your 5-minute pitch video

See `pitch_video_script.md` in this folder — it has a full script you can read from, structured in 5 sections timed to fit 5 minutes. Use your phone screen recorder or OBS Studio (free) to record your screen while you talk and demo the app from Step 6.

Upload it to YouTube (as Unlisted) or Google Drive with link sharing turned on, and use that link for "5-min Pitch Video Link."

## Step 9 — Fill out the form

Use `form_answers.md` in this folder — it has ready-to-paste answers for every text field.

---

## If something goes wrong

- **"pip not recognized"** → Python wasn't added to PATH. Reinstall Python and check that box.
- **"No module named pandas"** → run `pip install -r requirements.txt` again, make sure you're in the right folder.
- **Model training is slow/crashes** → your laptop may be low on RAM. Open `train_model.py` and change `sample_frac = 1.0` to `sample_frac = 0.3` near the top — this uses 30% of the data, still works fine.
- Stuck on anything → come back and tell me exactly what error you see. I'll fix it with you.
