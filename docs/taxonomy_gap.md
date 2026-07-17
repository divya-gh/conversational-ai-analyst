## Taxonomy Gap — Core Meaning
A taxonomy gap is the mismatch between:

what users actually say,
vs.

what your intent taxonomy is designed to understand.

In other words:

Users ask things your intent list does not cover.

This creates blind spots in your NLU.

🔍 Why taxonomy gaps matter
When your taxonomy doesn’t match real user behavior, you see:

high fallback rate

high low‑confidence rate

many messages classified as unknown

intents overloaded with unrelated messages

confusion between similar intents

poor routing and automation

longer conversations

lower resolution rate

Your analytics already show this pattern — unknown and technical_problem have high low‑confidence counts, which is a classic taxonomy gap signal.

🧩 Examples of taxonomy gaps
1. Missing intents
Users ask:

Code
“Can I change my email?”
But your taxonomy has no “account_update” intent.

→ Goes to fallback or unknown.

2. Overloaded intents
Everything vaguely technical gets dumped into technical_problem.

→ High low‑confidence
→ High fallback
→ Hard to automate

3. Ambiguous intent boundaries
You have:

billing_issue

refund_request

But users say:

Code
“I was charged twice, I want a refund.”
→ Model is unsure
→ Low confidence spikes

4. Intent too broad
general_query becomes a catch‑all bucket.

→ Taxonomy gap in disguise.

📊 How taxonomy gaps show up in your data
You already saw it:

Code
technical_problem    223
unknown              223
general_query        213
These three intents have the highest low‑confidence counts.

That is textbook taxonomy gap behavior.

🛠️ How to detect taxonomy gaps programmatically
You can compute:

1. High fallback rate per intent
python
fallback_by_intent = df.groupby("intent")["is_fallback"].mean()
2. High low‑confidence rate per intent
python
low_conf_by_intent = df.groupby("intent")["is_low_conf"].mean()
3. High message volume + high confusion
Combine:

volume

fallback

low confidence

This reveals overloaded or poorly defined intents.

🎯 How to fix taxonomy gaps
You improve your taxonomy by:

adding missing intents

splitting overloaded intents

merging redundant intents

tightening intent definitions

adding more training examples

improving entity extraction

This is how you evolve your NLU.

✔️ Summary (use this in your dashboard)
A taxonomy gap is the mismatch between user behavior and your intent taxonomy.
It shows up as:

high fallback

high low confidence

overloaded intents

many unknown classifications

Fixing taxonomy gaps improves accuracy, automation, and user experience.