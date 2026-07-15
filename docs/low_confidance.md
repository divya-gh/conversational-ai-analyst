
## What is low‑confidence analysis ?

how often your NLU model is unsure about the user’s message, even if it does predict an intent.

Here’s the clean, practical definition you can use in your notebook.

🎯 What “low‑confidence analysis” means
It is the percentage of messages where the model assigned an intent, but the confidence score was below your threshold (commonly 0.5, 0.6, or 0.7).

In other words:

The model guessed an intent, but wasn’t confident enough.

This is different from fallback:

Fallback → model could not classify

Low confidence → model classified, but weakly

Both matter for NLU quality.

📘 Why it matters
Low‑confidence messages often indicate:

ambiguous user phrasing

overlapping intents

poorly trained intents

insufficient examples

noisy text (typos, slang, emojis)

intents that need merging or re‑labeling

A high low‑confidence rate means your bot is “guessing” too often.

🧮 How you compute it (typical pattern)
If your dataframe has:

intent_confidence → float between 0–1

threshold → e.g., 0.6

Then:

python
threshold = 0.6
df['is_low_conf'] = df['intent_confidence'] < threshold
low_conf_rate = df['is_low_conf'].mean() * 100
This gives you the percentage of low‑confidence messages.

📊 Example interpretation
If you get:

Code
low_conf_rate = 27.4%
It means:

27.4% of messages were classified with confidence below your threshold.

That’s a sign your NLU needs improvement.