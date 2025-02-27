import time
import random

# ─────────────── ST.01: Introduction ───────────────
def st_intro():
    animated_text("🚀 ST.01: Welcome to the Growth Mindset Challenge! 🚀\n")
    time.sleep(1)
    animated_text("💡 ST.02: Motivational Quote of the Day: " + random.choice(QUOTES) + "\n")
    time.sleep(1)

# ─────────────── ST.02: Motivational Quotes ───────────────
QUOTES = [
    "🚀 Your only limit is your mind! 🌟",
    "💡 Success is the sum of small efforts, repeated daily! 💪",
    "🌱 Growth begins at the end of your comfort zone! 🔥",
    "🏆 Believe in yourself and you are halfway there! ✨"
]

# ─────────────── ST.03: Responses for Sections ───────────────
RESPONSES = {
    "challenge": [
        "💪 ST.04: That's a great challenge! Overcoming it will make you stronger!",
        "🌱 ST.05: Amazing! Taking on challenges means you're growing!",
        "🚀 ST.06: Keep pushing forward! Every challenge is a step toward success!",
        "🔥 ST.07: You got this! Stay focused and keep going!"
    ],
    "reflection": [
        "📖 ST.08: Self-reflection is the key to improvement! Keep learning!",
        "🌟 ST.09: Your growth is evident! Keep reflecting and growing!",
        "🧠 ST.10: Great insights! Every lesson learned brings new wisdom!",
        "💪 ST.11: You're becoming better every day! Keep up the amazing work!"
    ],
    "achievement": [
        "🎉 ST.12: Congratulations! Your hard work is paying off!",
        "🎊 ST.13: Well done! Every achievement deserves to be celebrated!",
        "💡 ST.14: Success is built on small wins! Keep going!",
        "🌟 ST.15: You're making incredible progress! Keep shining!"
    ]
}

# ─────────────── ST.16: Animated Text Function ───────────────
def animated_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")

# ─────────────── ST.17: Question Function ───────────────
def st_ask_question(category, question):
    while True:
        animated_text(question)
        answer = input("👉 Your Answer: ").strip()
        if answer:
            print(random.choice(RESPONSES[category]))
            print("\n" + "-" * 50 + "\n")
            time.sleep(1.5)
            break
        else:
            print("⚠️ ST.18: Please enter a valid response! Your input matters! 🙏\n")

# ─────────────── ST.19: Main Challenge ───────────────
def st_growth_mindset_challenge():
    st_intro()
    st_ask_question("challenge", "💪 ST.20: What is your challenge today?")
    st_ask_question("reflection", "📖 ST.21: Reflect on your learning. What did you learn today?")
    st_ask_question("achievement", "🏆 ST.22: Share something about your accomplishments!")

    # ─────────────── ST.23: Closing Message ───────────────
    animated_text("🔥 ST.24: Keep striving! Every day is a new opportunity to grow! 🔥")
    animated_text("✨ ST.25: Made by Zunaira Hussain ✨\n")

# ─────────────── ST.26: Run the Challenge ───────────────
if __name__ == "__main__":
    st_growth_mindset_challenge()
