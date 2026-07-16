
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Load data
df = pd.read_csv("data/twcs_intent_simulated.csv")

# Sidebar navigation
st.sidebar.title("📊 Dashboard Navigation")

page = st.sidebar.radio(
    # add an emoji to the title
    "📊 Go to:",
    [
        "Key Metrics",
        "Intent Distribution",
        "Fallback & Low Confidence",
        "User vs Company Behavior",
        "Time-based Trends",
        "Conversation-level Insights",
        "Filtered View"
    ]
)

# -----------------------------
# PAGE 1 — KEY METRICS
# -----------------------------
if page == "Key Metrics":
    st.title("📈 Key Metrics Overview")

    col1, col2 = st.columns(2)

    with col1:
        fallback_rate = df["is_fallback"].mean()
        st.metric("Fallback Rate", f"{fallback_rate:.2%}")

        # create a pie chart for fallback distribution
        fallback_counts = df["is_fallback"].value_counts()
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(fallback_counts, labels=["Not Fallback", "Fallback"], autopct="%1.1f%%", colors=["#4CAF50", "#F44336"])
        ax.set_title("Fallback Distribution")
        st.pyplot(fig)
        

    with col2:
        low_conf_rate = df["is_low_conf"].mean()
        st.metric("Low Confidence Rate", f"{low_conf_rate:.2%}")

        # create a pie chart for confidence distribution high, low and medium
        df["confidence_category"] = pd.cut(df["confidence"], bins=[0, 0.6, 0.8, 1], labels=["Low", "Medium", "High"])
        conf_counts = df["confidence_category"].value_counts()
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(conf_counts, labels=conf_counts.index, autopct="%1.1f%%", colors=["#FFC107", "#2196F3", "#4CAF50"])
        ax.set_title("Confidence Distribution")
        st.pyplot(fig)

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📌 Summary")
        st.write(
            f"""
            - Total messages: **{len(df)}**  
            - Total intents: **{df['intent'].nunique()}**  
            - User messages: **{df['is_user'].mean():.2%}**  
            - Company messages: **{1 - df['is_user'].mean():.2%}**
            """
        )

    with col2:
        st.subheader("📊 Intent Distribution")
        st.write(
            f"""
            - Most common intent: **{df['intent'].mode()[0]}**
            - Least common intent: **{df['intent'].value_counts().idxmin()}**
            - Low confidence → model classified, but weakly
            - Fallback → model could not classify/unknown intent
            """)

# -----------------------------
# PAGE 2 — INTENT DISTRIBUTION
# -----------------------------
elif page == "Intent Distribution":
    st.title("📊 Intent Distribution")

    intent_counts = df["intent"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(x=intent_counts.index, y=intent_counts.values, ax=ax)
    #plt.title("Intent Distribution")
    plt.ylabel("Message Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    st.write("---")
    # intent distribution over time
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["date"] = df["created_at"].dt.date
    intent_time = df.groupby(["date", "intent"]).size().unstack(fill_value=0)
    st.write("Intent Distribution Over Time:")
    st.dataframe(intent_time)

    st.write("---")

    # create a line plot for intent distribution over time
    fig, ax = plt.subplots(figsize=(12, 4))
    intent_time.plot(ax=ax)
    plt.title("Intent Distribution Over Time")
    plt.ylabel("Message Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)


# -----------------------------
# PAGE 3 — FALLBACK & LOW CONFIDENCE
# -----------------------------
elif page == "Fallback & Low Confidence":
    st.title("⚠️ Fallback & Low Confidence Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Fallback by Intent")
        fb = df.groupby("intent")["is_fallback"].mean().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=fb.index, y=fb.values, ax=ax)
        plt.ylabel("Fallback Rate")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col2:
        st.subheader("Low Confidence by Intent")
        lc = df.groupby("intent")["is_low_conf"].mean().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=lc.index, y=lc.values, ax=ax)
        plt.ylabel("Low Confidence Rate")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # summarise fallback and low confidence rates
    st.write("---")
    st.write("### 📌 Summary")
    st.write(
        f"""
        - Overall Fallback Rate: **{df['is_fallback'].mean():.2%}**
        - Overall Low Confidence Rate: **{df['is_low_conf'].mean():.2%}**
        - Intent with highest fallback rate: **{fb.idxmax()}** ({fb.max():.2%})
        - Intent with highest low confidence rate: **{lc.idxmax()}** ({lc.max():.2%})
    """)
    # expplain what fallback and low confidence means
    st.write(
        """
        **Fallback**: The model could not classify the intent of the message, leading to a fallback response.  
        **Low Confidence**: The model classified the intent, but with low confidence, indicating uncertainty in the prediction.
        """
    )
    

# -----------------------------
# PAGE 4 — USER VS COMPANY BEHAVIOR
# -----------------------------
elif page == "User vs Company Behavior":
    st.title("👥 User vs Company Behavior")

    counts = df["is_user"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    # user color yellow and company color green
    sns.barplot(x=["User", "Company"], y=[counts.get(True, 0), counts.get(False, 0)], ax=ax, palette=["salmon", "steelblue"])
    # add y lablel
    plt.ylabel("Message Count")
    st.pyplot(fig)

    # Intent distribution for user vs company
    user_intent_counts = df[df["is_user"]]["intent"].value_counts().sort_values(ascending=False)
    company_intent_counts = df[df["is_company"]]["intent"].value_counts()

    st.write("---")
    # create a dataframe for plotting
    user_vs_company = pd.DataFrame({"company": company_intent_counts,
                                "user":user_intent_counts
                               }).sort_index()
    
    st.write("---")
    # create a stacked bar chart
    user_vs_company.plot(kind="bar", stacked=True, figsize=(10, 5))
    plt.title("Intent Distribution: User vs Company")   
    plt.ylabel("Message Count")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())

    st.write("---")
    # intent distribution for user vs company (normalized)
    user_vs_company_norm = user_vs_company.div(user_vs_company.sum(axis=1), axis=0)*100
    user_vs_company_norm.plot(kind="bar", stacked=False, figsize=(10, 5), color=["steelblue", "salmon"])
    plt.ylabel("Percentage")
    plt.xticks(rotation=45)
    plt.title("Normalized Intent Distribution: User vs Company")    
    st.pyplot(plt.gcf())
# create a summary explaining the differences in behavior
    st.write("---")
    st.write(
        """
        **Summary of User vs Company Behavior:**  
        - The message counts show the overall activity of users and companies.  
        - The intent distribution indicates the types of messages sent by users and companies.  
        - The normalized intent distribution provides insights into the relative proportions of intents for users and companies.
        """
    )


# -----------------------------
# PAGE 5 — TIME-BASED TRENDS
# -----------------------------
elif page == "Time-based Trends":
    st.title("⏳ Time-based Trends")

    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["date"] = df["created_at"].dt.date

    daily_counts = df.groupby("date").size()

    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(x=daily_counts.index, y=daily_counts.values, ax=ax)
    plt.title("Daily Message Counts")
    plt.ylabel("Message Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # create a line plot for daily fallback and low confidence rates
    daily_fallback = df.groupby("date")["is_fallback"].mean()
    daily_low_conf = df.groupby("date")["is_low_conf"].mean()
    st.write("---")
    st.write("### 🕒 Daily Fallback and Low Confidence Rates")
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(x=daily_fallback.index, y=daily_fallback.values, ax=ax, label="Fallback")
    sns.lineplot(x=daily_low_conf.index, y=daily_low_conf.values, ax=ax, label="Low Confidence")
    plt.title("Daily Fallback and Low Confidence Rates")
    plt.ylabel("Rate")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # create a line plot for daily user vs company message volume
    daily_user = df[df["is_user"]].groupby("date").size()
    daily_company = df[df["is_company"]].groupby("date").size()
    st.write("---")
    st.write("### 🕒 Daily User vs Company Message Volume")
    fig, ax = plt.subplots(figsize=(12, 4))
    sns.lineplot(x=daily_user.index, y=daily_user.values, ax=ax, label="User")
    sns.lineplot(x=daily_company.index, y=daily_company.values, ax=ax, label="Company")
    plt.title("Daily User vs Company Message Volume")
    plt.ylabel("Message Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # create a summary explaining the trends
    st.write("---")
    st.write(
        """
        **Summary of Time-based Trends:**  
        - The daily message counts show the overall activity over time.  
        - The daily fallback and low confidence rates indicate how often the model struggles to classify intents.  
        - The daily user vs company message volume provides insights into the interaction dynamics between users and the
    company per day.
        """
    )

# -----------------------------
# PAGE 6 — CONVERSATION-LEVEL INSIGHTS
# -----------------------------
elif page == "Conversation-level Insights":
    st.title("💬 Conversation-level Insights")
    # get the convo smaple csv
    df_convo = pd.read_csv("data/twcs_multiturn_sample.csv")

    conv_sizes = df_convo.groupby("conversation_id").size().sort_values(ascending=False)

    # create a bar chart for the top 10 longest conversations
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(x=conv_sizes.head(10).index, y=conv_sizes.head(10).values, ax=ax)
    plt.title("Top 10 Longest Conversations")
    plt.ylabel("Message Count") 
    plt.xlabel("Conversation ID")
    st.pyplot(fig)

    # conversation ID with highest message count
    longest_convo_id = conv_sizes.idxmax()
    longest_convo = df_convo[df_convo["conversation_id"] == longest_convo_id]
    st.write(f"### Longest Conversation (ID: {longest_convo_id})")
    st.dataframe(longest_convo[["tweet_id", "text", "is_user", "is_company", "intent", "confidence"]])

    # create a summary explaining the longest conversation along with the fallback and low confidence rates
    st.write("---")
    st.write(
        f"""
        **Summary of the Longest ConversationID - {longest_convo_id} :**  
        - Total messages: **{len(longest_convo)}**  
        - Fallback messages: **{longest_convo['is_fallback'].sum()}**  
        - Low confidence messages: **{longest_convo['is_low_conf'].sum()}**  
        - Fallback rate: **{longest_convo['is_fallback'].mean():.2%}**  
        - Low confidence rate: **{longest_convo['is_low_conf'].mean():.2%}**
        """
    )       

    

# -----------------------------
# PAGE 7 — FILTERED VIEW
# -----------------------------
elif page == "Filtered View":
    st.title("🔍 Filtered View")

    side = st.sidebar.selectbox("Message side", ["user", "company"])
    is_user_flag = True if side == "user" else False

    intent = st.sidebar.selectbox("Intent", df["intent"].unique())

    filtered = df[(df["is_user"] == is_user_flag) & (df["intent"] == intent)]

    st.write(f"### Showing {len(filtered)} messages for **{side}** with intent **{intent}**")
    st.dataframe(filtered[["tweet_id", "text", "Clean_text", "confidence"]].head(50))
