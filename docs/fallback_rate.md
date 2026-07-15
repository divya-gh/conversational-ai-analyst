## what is fallback rate?
Fallback rate is a core metric in conversational AI that tells you how often your bot fails to understand the user and falls back to a default response.

🎯 Concise takeaway
Fallback rate = % of messages where the NLU could not classify the intent confidently.

📘 What “fallback” means
A fallback happens when your system says something like:

“I didn’t understand that.”

“Can you rephrase?”

“I’m not sure how to help with that.”

Or triggers a fallback intent (often named fallback, unknown, no_intent, out_of_scope)

This is the bot’s safety net when intent detection fails.

📊 Formula
If your dataset has an intent column:

python
fallback_rate = (df['intent'] == 'fallback').mean() * 100
Example:

Code
Total messages: 10,000
Fallback messages: 800

Fallback rate = 800 / 10,000 = 8%
📈 Why fallback rate matters
A high fallback rate usually means:

Users ask things your bot wasn’t trained for

Your intents are too narrow

Your NLU model is underperforming

Your training data is insufficient

Your bot is receiving noisy or ambiguous messages

A low fallback rate means:

Your bot understands users well

Your intents cover the domain

Your NLU confidence is strong

🎯 Healthy ranges
Typical benchmarks:

0–5% → Excellent

5–10% → Acceptable

10–20% → Needs improvement

20%+ → Users are struggling