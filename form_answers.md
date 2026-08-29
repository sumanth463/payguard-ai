# Razorpay AI Builder Internship 2026 — Form Answers

Copy-paste these directly into the Google Form.

---

**Track:**
Track 2: AI Risk Manager

**Project Name / Title:**
PayGuard AI — Real-Time Fraud Risk Explainer

**Project Objectives (What does it solve?):**
Most fraud-detection systems flag risky transactions but don't explain why, leaving support teams and customers in the dark and creating friction and mistrust. PayGuard AI solves this by combining a machine learning fraud-risk classifier with a plain-English explanation layer, so every flagged transaction comes with a clear, human-readable reason (e.g. unusual amount, timing, or transaction velocity). This mirrors how a human risk analyst reasons, making automated fraud decisions transparent and actionable for both merchants and support teams — directly relevant to a payments platform like Razorpay's risk operations.

**GitHub Repository URL:**
https://github.com/sumanth463/payguard-ai
(update once you've pushed — see README Step 7)

**5-min Pitch Video Link:**
[paste your YouTube/Drive link here once recorded — see pitch_video_script.md]

**Build Challenges & Technical Obstacles (What issues did you face, and how did you solve them?):**
The main challenge was that the public transaction dataset anonymizes its features (V1–V28, via PCA) to protect user privacy, which meant I couldn't map raw inputs like "amount" or "time" directly onto the model's trained features for live predictions. I solved this by having the live demo combine the trained model's underlying risk signal with interpretable, business-relevant features — transaction amount, hour of day, and time since the previous transaction — the same signals a real payments risk team would have direct access to, rather than the anonymized research features. I also had to handle severe class imbalance in the training data (fraud is a tiny fraction of transactions), which I addressed using class-weighted training so the model doesn't just default to predicting "not fraud" every time.

**Final Submission Confirmation:**
✓ (check this box only once everything above is finalized — no edits allowed after)
