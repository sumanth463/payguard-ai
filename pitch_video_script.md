# 5-Minute Pitch Video Script — PayGuard AI

Record your screen (share the browser tab showing the PayGuard AI demo + your code editor) while reading this. Speak naturally — don't sound robotic, pause where marked.

---

**[0:00–0:40] The Problem**

"Hi, I'm Sumanth, a final-year ECE student. For the AI Risk Manager track, I built PayGuard AI — an AI agent that flags risky payment transactions in real time and, more importantly, *explains why* in plain English.

Here's the problem: fraud detection models today are usually black boxes. A transaction gets blocked, but the support team — or the customer — has no idea why. That creates support overhead and erodes trust. PayGuard AI closes that gap."

**[0:40–1:30] How it works (high level)**

"PayGuard has two layers. First, a machine learning model — trained on a real anonymized transaction dataset — scores every transaction for fraud risk. Second, an explanation layer translates that score into a human-readable reason: was it the amount, the timing, or the pattern that looked off?

This mirrors how a real risk analyst thinks — not just 'this is risky' but 'this is risky *because*.'"

**[1:30–3:30] Live demo**

*(Switch to your browser at http://127.0.0.1:8000)*

"Let me show you live. I'll enter a transaction: ₹4,500, at 2 AM, just 15 seconds after the previous transaction on this account.

*(Click 'Run Risk Check')*

You can see PayGuard flags this as high risk, and gives a clear reason — the unusual hour and the rapid succession of transactions. This isn't a canned message, it's generated based on which specific signals triggered the flag.

Now let's try a normal one — ₹200, at 2 PM, an hour since the last transaction.

*(Run it)*

Marked as low risk, safe pattern. This is the kind of transparency that reduces false-positive complaints and builds trust in automated risk systems."

**[3:30–4:20] Technical build**

"Under the hood: a Random Forest classifier trained on transaction data, wrapped in a FastAPI backend, with a lightweight explanation engine that maps model signals to plain language. Everything's on GitHub — link is in the submission.

The biggest technical challenge was the dataset itself: to protect user privacy, real transaction features are anonymized. I solved this by combining the trained model's risk score with interpretable business-logic features — amount, timing, transaction velocity — that a real payments company like Razorpay would actually have access to, rather than relying only on the anonymized columns."

**[4:20–5:00] Why this matters for Razorpay / close**

"For a company processing payments at Razorpay's scale, this kind of explainable risk agent could reduce manual review time and give merchants clear, actionable reasons when a transaction is held — turning a black-box block into a trust-building interaction.

I'm a beginner in ML, but I built this end-to-end in a few days because I wanted to prove I could ship something real, not just learn in theory. I'd love the opportunity to keep building this at Razorpay. Thank you."

---

**Tips for recording:**
- Use your phone's built-in screen recorder, or download OBS Studio (free) if recording on a laptop.
- Do 2–3 practice runs before the real take — you'll sound way more natural.
- Keep total time under 5:00 — trim in any basic video editor (CapCut is free and easy) if you run over.
