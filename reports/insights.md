# 📄 insights.md — Conversational AI Analyst Findings
🧩 1. Taxonomy Gap Analysis
This section identifies missing intents based on real user messages.
Even though the dataset used simulated labels, the text itself is real, so taxonomy gaps are real.

1.1 Missing Intent: Return Request
Examples from your dataset:

“trying to return a faulty item”

“by the time I get a refund…”

These messages clearly indicate product returns, which are not covered by existing intents.

Add: return_request

1.2 Missing Intent: Order Cancellation
Examples:

“is this a scam? I haven’t set up any prime subscription”

“was it delayed due to a payment issue?”

Users are asking to cancel or verify orders.

Add: order_cancellation

1.3 Missing Intent: Fraud Check
Examples:

“is this a scam?”

“I haven’t set up any prime subscription”

These messages indicate security concerns.

Add: fraud_check

1.4 Missing Intent: Account Access Issue
Examples:

“anything you need me to show to reinstate my account”

“I’m still waiting on my permanent token”

These are account recovery or login issues.

Add: account_access_issue

1.5 Missing Intent: Technical Issue
Examples:

“cannot scan with Windows 10”

“zero mainstream devices support…”

These are device or software problems.

Add: technical_issue

1.6 Missing Intent: Shipping / Delivery Delay
Examples:

“tracking numbers…”

“was it delayed due to a payment issue?”

These messages relate to delivery status.

Add: shipping_delay

1.7 Missing Intent: General Complaint / Experience Issue
Examples:

“that’s not how we want you to feel”

“apologies for the delay”

These are experience dissatisfaction messages.

Add: general_complaint

1.8 Missing Intent: Product Support Issue
Examples:

“gifting content on iOS”

“cannot scan with Windows 10”

These are product-specific support needs.

Add: product_support_issue

🔁 2. Overlapping Intent Analysis
This section identifies where existing intents blur together, causing confusion.

2.1 Billing Issue vs Refund Request
Examples:

“payment issue”

“temporary authorization was not…”

“refund was promised…”

These messages share language around:

payment

charge

refund

authorization

Recommendation:  
Merge into a broader intent: payment_issue  
Or define strict boundaries.

2.2 Refund Request vs Return Request
Examples:

“faulty item”

“refund was promised”

These are different intents but share similar language.

Recommendation:  
Split clearly:

refund_request → money back

return_request → item return

2.3 Complaint vs Technical Issue
Examples:

“cannot scan with Windows 10”

“zero mainstream devices support…”

Users complain about technical issues, causing overlap.

Recommendation:  
Add technical_issue to reduce confusion.

🛠 3. Recommendations
Based on taxonomy gaps and overlaps:

3.1 Add New Intents
return_request

order_cancellation

fraud_check

account_access_issue

technical_issue

shipping_delay

general_complaint

product_support_issue

3.2 Refine Existing Intents
Merge or clarify billing_issue and refund_request

Separate refund_request vs return_request

3.3 Improve Training Data
Use fallback/unknown messages as training goldmine

Add multilingual examples (Spanish, Turkish detected)

3.4 Improve Routing
Route technical issues to specialized support

Route fraud-related messages to security workflows

📊 4. Business Insights
This section translates your findings into business actions.

4.1 Operational Insight
High volume of messages about returns, refunds, and payment issues suggests friction in post‑purchase workflows.

Action:

Improve refund/cancellation processes

Provide clearer communication about payment verification

4.2 Product Insight
Technical issues around device compatibility (Windows 10, iOS gifting) indicate gaps in product documentation.

Action:

Publish troubleshooting guides

Improve proactive communication

4.3 Experience Insight
Many empathy-only responses (“sorry for the delay”) without resolution indicate a need for better resolution workflows, not just apology templates.

Action:

Train agents to provide actionable steps

Improve automated responses

4.4 Risk Insight
Fraud-related messages (“is this a scam?”) indicate brand trust issues.

Action:

Improve communication about legitimate messages

Add fraud-check automation