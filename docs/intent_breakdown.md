## what is intent distribution?
**Intent distribution is simply the frequency breakdown of user intents in your conversational dataset.**

It tells you what users are trying to do and how often each intent appears.

oncise takeaway
Intent distribution = count (or percentage) of each intent label across all messages.

📊 What it means in conversational analytics
When you classify each message into an intent like:

greeting

complaint

order_status

refund_request

product_question

chitchat

agent_transfer

…you can compute how often each one occurs.

This gives you:

Top user needs

Workload patterns

Where automation helps most

Where users struggle

Which intents dominate your traffic

🧮 Example (Python)
If your dataframe has a column intent:

python
intent_distribution = df['intent'].value_counts(normalize=True) * 100
print(intent_distribution)
Output:

Code
order_status       42.1%
refund_request     18.3%
product_question   15.7%
complaint          12.4%
greeting            7.5%
This is your intent distribution.

📈 Why it matters
Intent distribution is foundational for:

NLU model training (class imbalance detection)

Conversation design (which flows matter most)

Automation strategy (high-volume intents → bots)

Business insights (what customers care about)

Quality monitoring (where agents struggle)