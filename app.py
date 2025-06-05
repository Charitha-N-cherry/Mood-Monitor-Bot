import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import time

# Load the sentiment-analyzed CSV
df = pd.read_csv("reddit_posts_with_sentiment.csv")  # Replace with your actual CSV file name

# Calculate total and negative posts
total_posts = len(df)
negative_count = (df["sentiment"] == "negative").sum()
threshold = total_posts * 0.25  # 25% threshold

# Motivational quotes
quotes = [
    "You’ve got this 💪",
    "Keep going, brighter days are ahead 🌞",
    "Every day is a fresh start 🌱",
    "Believe in your potential 🌟",
    "You are stronger than you think 🛡️",
    "Difficult roads often lead to beautiful destinations 🚀"
]

# Add a background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
    }
    </style>
    """, unsafe_allow_html=True)

# Styled Header and Text
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌐 Mood Monitor</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555;'>Analyze your Reddit activity for sentiment trends!</h3>", unsafe_allow_html=True)

# Add a line break
st.markdown("<hr>", unsafe_allow_html=True)

# Explanation Text
st.markdown("<p style='font-size:18px; color: #333;'>This app helps you track the sentiment of Reddit posts and provide motivational quotes if you are consuming too much sad content. 💭</p>", unsafe_allow_html=True)

# App layout
st.write(f"Total Posts Analyzed: **{total_posts}**")
st.write(f"Number of Negative Posts: **{negative_count}**")
st.write(f"Threshold for Motivation: **{int(threshold)}**")

# Logic
if negative_count > threshold:
    st.warning("⚠️ You've been reading a lot of sad content lately.")
    st.success("💡 Here's something uplifting for you:")
    st.markdown(f"### 👉 {random.choice(quotes)}")
else:
    st.balloons()
    st.info("✅ You're doing fine. Stay positive! 🌸")

# Pie Chart for Sentiment Distribution
sentiment_counts = df["sentiment"].value_counts()
fig, ax = plt.subplots()

# Define custom colors
colors = ['#FF6347', '#90EE90', '#1E90FF']

# Create Pie Chart
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')

# Add Title
st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Sentiment Distribution 📊</h3>", unsafe_allow_html=True)
st.pyplot(fig)

# Filter by Sentiment
selected_sentiment = st.selectbox("Filter by Sentiment", df["sentiment"].unique())
filtered_df = df[df["sentiment"] == selected_sentiment]
st.dataframe(filtered_df)

# Show raw data with checkbox
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Progress bar to simulate processing (optional)
if st.button("Start Processing"):
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.05)  # Simulating delay
        progress_bar.progress(i + 1)
    st.write("✅ Data processing complete!")

