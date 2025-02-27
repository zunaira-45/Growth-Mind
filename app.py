import streamlit as st
import random
import time

# ──── PAGE CONFIG ────
st.set_page_config(page_title="Growth Mindset Challenge 🚀", page_icon="💡", layout="centered")

# ──── STYLING ────
st.markdown(
    """
    <style>
        .big-title {
            font-size: 36px; 
            font-weight: bold; 
            text-align: center; 
            color: #ffffff;
            background: linear-gradient(to right, #4A00E0, #8E2DE2);
            padding: 10px; 
            border-radius: 10px;
        }
        .quote-box {
            font-size: 22px;
            font-style: italic;
            text-align: center;
            color: #4CAF50;
            background-color: #F3F4F6;
            padding: 15px;
            border-left: 5px solid #4CAF50;
            border-radius: 8px;
        }
        .footer {
            text-align: center;
            font-size: 18px;
            color: #ffffff;
            background-color: #000000;
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .button {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# ──── HEADER ────
st.markdown('<div class="big-title">🚀 Growth Mindset Challenge - STEAM Lite</div>', unsafe_allow_html=True)

# ──── INSPIRATIONAL QUOTE ────
quotes = [
    "✨ Your mindset shapes your future! 🚀",
    "💡 Face challenges, learn, and grow! 🌱",
    "🔥 Every day is a new opportunity to become better!",
    "🌟 Success starts with the right mindset!",
    "🎯 Challenges are not obstacles, they are growth opportunities!"
]
st.markdown(f'<div class="quote-box">{random.choice(quotes)}</div>', unsafe_allow_html=True)
time.sleep(1)

# ──── USER INPUT: CHALLENGE ────
st.subheader("💪 What’s Your Challenge Today?")
challenge = st.text_input("Describe your challenge:", key="challenge")

if st.button("Enter Challenge"):
    if challenge:
        responses = [
            "💪 Amazing! Overcoming challenges makes you stronger!",
            "🌟 Great mindset! Every challenge is an opportunity to grow!",
            "🚀 Keep going! You're on the path to success!"
        ]
        st.success(random.choice(responses))
    else:
        st.warning("⚠️ Please describe your challenge! Your journey matters!")

# ──── USER INPUT: REFLECTION ────
st.subheader("📖 Reflection Time")
reflection = st.text_area("What did you learn today?", key="reflection")

if st.button("Enter Reflection"):
    if reflection:
        responses = [
            "📖 Self-reflection leads to self-improvement! Keep learning!",
            "🌱 Growth mindset is all about learning from experiences!",
            "🧠 Your insights are powerful! Keep pushing forward!"
        ]
        st.success(random.choice(responses))
    else:
        st.warning("⚠️ Reflecting helps you grow! Write something about your learning.")

# ──── USER INPUT: ACHIEVEMENTS ────
st.subheader("🏆 Share Your Achievements")
achievement = st.text_area("What accomplishment are you proud of?", key="achievement")

if st.button("Enter Achievement"):
    if achievement:
        responses = [
            "🎉 Congrats! Every step forward is worth celebrating!",
            "🎊 Your progress is inspiring! Keep up the great work!",
            "🏆 Well done! Success is built on small wins!"
        ]
        st.success(random.choice(responses))
    else:
        st.warning("⚠️ Acknowledge your achievements! They matter.")

# ──── FOOTER ────
st.markdown(
    '<div class="footer">🔥 Stay focused & keep growing!<br>✨ Made by Zunaira Hussain ✨</div>',
    unsafe_allow_html=True
)


