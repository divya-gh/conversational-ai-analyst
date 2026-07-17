# conversational-ai-analyst
conversational data wrangling, intent‑level analytics, and data storytelling — using Python + NLU basics + dashboards.

# Conversational AI Analyst — Customer Support Insights Dashboard  
A data-driven conversational analytics project built to simulate how Conversational AI teams analyze customer support interactions, identify taxonomy gaps, evaluate fallback behavior, and generate actionable business insights.

🔗 **Live Dashboard:** https://conversational-ai-analyst.streamlit.app/

---

## 📌 Overview

This project analyzes real customer support conversations from Twitter (TWCS dataset) and simulates an intent classification workflow used by Conversational AI teams.  
It includes:

- Intent distribution analysis  
- Fallback & low-confidence detection  
- Taxonomy gap analysis  
- Overlapping intent evaluation  
- Business insights & recommendations  
- A fully interactive Streamlit dashboard  

The goal is to demonstrate the end-to-end workflow of a **Conversational AI Analyst**, including data cleaning, taxonomy evaluation, conversational insights, and dashboard storytelling.

---

## 🖼️ Dashboard Preview

> *(Replace the placeholder below with an actual screenshot once you upload it to your repo)*

![Dashboard Preview](assets/dashboard_preview.png)

---

## 🧠 Key Features

### **1. Intent Distribution**
Visualizes how customer messages are categorized across simulated intents.

### **2. Fallback & Low Confidence**
Shows where the model struggles — critical for improving NLU performance.

### **3. Taxonomy Gap Analysis**
Identifies missing intents such as:
- return_request  
- fraud_check  
- account_access_issue  
- technical_issue  
- shipping_delay  

### **4. Overlapping Intent Analysis**
Highlights confusion between:
- billing_issue ↔ refund_request  
- refund_request ↔ return_request  
- complaint ↔ technical_issue  

### **5. Business Insights**
Provides actionable recommendations for:
- improving customer experience  
- refining taxonomy  
- reducing fallback  
- enhancing routing workflows  

---

## 📂 Project Structure

```bash
conversational-ai-analyst/
│
├── app/
│   └── dashboard.py          # Streamlit dashboard
│
├── data/
│   └── twcs_intent_simulated.csv   # Cleaned + simulated intent dataset
│
├── notebooks/
│   ├── 01_cleaning.ipynb
│   ├── 02_exploration.ipynb
│   ├── 03_intent_simulation.ipynb
│   ├── 04_dashboard_metrics.ipynb
│   └── 05_insights.ipynb     # Day 6 taxonomy + business insights
│
├── reports/
│   └── insights.md           # Final Day 6 analysis
│
├── requirements.txt          # Dependencies for Streamlit Cloud
└── README.md                 # Project documentation
