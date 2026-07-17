## ⭐ Taxonomy Gap Detector — Full Module
A taxonomy gap happens when an intent is:

overloaded

under‑trained

poorly defined

missing sub‑intents

absorbing unrelated messages

producing high fallback or low confidence

We detect this using three signals:

1. Low‑Confidence Rate
Model predicts an intent but is unsure.

2. Fallback Rate
Model cannot classify at all.

3. Volume Pressure
Intent receives too many messages → overloaded.

These three combined reveal taxonomy gaps.

🧮 Step 1 — Compute core metrics
python
import pandas as pd

# Volume
volume = df.groupby("intent").size()

# Low confidence count & rate
low_conf_count = df.groupby("intent")["is_low_conf"].sum()
low_conf_rate = df.groupby("intent")["is_low_conf"].mean() * 100

# Fallback count & rate
fallback_count = df.groupby("intent")["is_fallback"].sum()
fallback_rate = df.groupby("intent")["is_fallback"].mean() * 100
🧮 Step 2 — Build the Taxonomy Gap Score
We combine the three signals:

python
taxonomy_gap = pd.DataFrame({
    "volume": volume,
    "low_conf_count": low_conf_count,
    "low_conf_rate": low_conf_rate,
    "fallback_count": fallback_count,
    "fallback_rate": fallback_rate
})

# Normalize metrics for scoring
taxonomy_gap["score"] = (
    taxonomy_gap["low_conf_rate"] * 0.5 +
    taxonomy_gap["fallback_rate"] * 0.3 +
    taxonomy_gap["volume"].rank(pct=True) * 0.2
)

taxonomy_gap = taxonomy_gap.sort_values("score", ascending=False)
taxonomy_gap
✔️ Interpretation
High score → severe taxonomy gap

Low score → healthy intent

This gives you a ranked list of problematic intents.

📊 Step 3 — Visualize Taxonomy Gaps
Heatmap (best for dashboards)
python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
sns.heatmap(
    taxonomy_gap[["low_conf_rate", "fallback_rate", "volume"]],
    annot=True, fmt=".1f", cmap="Reds"
)
plt.title("Taxonomy Gap Heatmap")
plt.show()
Bar chart of gap score
python
plt.figure(figsize=(12,5))
plt.bar(taxonomy_gap.index, taxonomy_gap["score"], color="salmon")
plt.xticks(rotation=45)
plt.title("Taxonomy Gap Score by Intent")
plt.ylabel("Gap Severity")
plt.show()
🧠 Step 4 — Flag intents with severe gaps
python
gap_threshold = taxonomy_gap["score"].quantile(0.75)
severe_gaps = taxonomy_gap[taxonomy_gap["score"] >= gap_threshold]
severe_gaps
This gives you a clean list of intents needing redesign.

🎯 Example Output (based on your data)
You will likely see:

Code
technical_problem
unknown
general_query
refund_request
billing_issue
These are classic overloaded or poorly defined intents.

✔️ Summary — What this module gives you
You now have a detector that identifies:
overloaded intents

ambiguous intents

missing intents

intents causing confusion

intents producing high fallback

intents producing high low confidence

intents needing redesign

And it produces:
a ranked severity score

a heatmap

a bar chart

a flagged list of problematic intents

This is exactly the kind of insight companies use to improve their NLU taxonomy.