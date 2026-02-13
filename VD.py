

import streamlit as st
import random

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="Our Love Game Zone 💖", page_icon="🌹", layout="wide")

# ---------------------------------------------------
# BACKGROUND MUSIC (Instrumental)
# ---------------------------------------------------
st.markdown("""
<audio autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8a73467.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# CSS STYLE
# ---------------------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #ffe6f0, #fff5f8);
}
.stButton>button {
    background-color: #c2185b;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}
h1, h2, h3 {
    text-align: center;
    color: #ad1457;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🌹 Welcome to Our Love Game Zone 💖")
st.subheader("Romance + Fun + Thoda Sa Drama 😌")

# ---------------------------------------------------
# GAME 1 – LOVE QUIZ (With Score)
# ---------------------------------------------------
st.header("Game 1: How Well Do You Know Me? 🤔")

questions = {
    "What is my favorite comfort food?": ["Pizza", "Ice Cream", "Chocolate", "All of them"],
    "Who says sorry first?": ["Me", "You", "Depends", "No one 😅"],
    "What do I love the most about you?": ["Your smile", "Your nature", "Your eyes", "Everything"]
}

answers = ["All of them", "Me", "Everything"]

score = 0
for i, (q, options) in enumerate(questions.items()):
    selected = st.radio(q, options, key=f"quiz{i}")
    if selected == answers[i]:
        score += 1

if st.button("Check Quiz Score 💕"):
    st.success(f"You scored {score}/{len(questions)} ❤️")
    if score == len(questions):
        st.balloons()
        st.success("Perfect! You truly know me inside out 😘")

# ---------------------------------------------------
# GAME 2 – LOVE COMPATIBILITY
# ---------------------------------------------------
st.header("Game 2: Love Compatibility 💘")

name1 = st.text_input("Your Name")
name2 = st.text_input("My Name")

if st.button("Calculate Love % 💞"):
    if name1 and name2:
        percentage = random.randint(85, 100)
        st.success(f"{name1} ❤️ {name2} = {percentage}% Perfect Match ✨")
    else:
        st.warning("Enter both names jaan 😄")

# ---------------------------------------------------
# GAME 3 – TRUTH OR DARE
# ---------------------------------------------------
st.header("Game 3: Truth or Dare 🎲")

truths = [
    "When did you first fall for me? 💖",
    "What is your favorite memory of us?",
    "What makes you jealous? 😜"
]

dares = [
    "Send me a cute selfie right now 😍",
    "Say I love you 5 times ❤️",
    "Give me a new romantic nickname 💕"
]

choice = st.radio("Choose one:", ["Truth 🤍", "Dare 💋"])

if st.button("Play Truth/Dare 🎉"):
    if choice == "Truth 🤍":
        st.info(random.choice(truths))
    else:
        st.warning(random.choice(dares))

# ---------------------------------------------------
# GAME 4 – SPIN THE LOVE WHEEL
# ---------------------------------------------------
st.header("Game 4: Spin the Love Wheel 🎡")

wheel_options = [
    "1 Warm Hug 🤗",
    "Movie Night Together 🎬",
    "Ice Cream Date 🍦",
    "Long Drive Under Stars 🚗✨",
    "10 Sweet Compliments 😍"
]

if st.button("Spin Now 💫"):
    result = random.choice(wheel_options)
    st.success(f"Wheel Says: {result}")

# ---------------------------------------------------
# GAME 5 – WHO IS MORE?
# ---------------------------------------------------
st.header("Game 5: Who Is More? 😏")

who_questions = [
    "Who is more dramatic? 🎭",
    "Who is more romantic? 🌹",
    "Who gets angry faster? 😅",
    "Who loves more? ❤️"
]

for i, q in enumerate(who_questions):
    st.radio(q, ["Me 😎", "You 😘", "Both 💕"], key=f"who{i}")

# ---------------------------------------------------
# SECRET MESSAGE
# ---------------------------------------------------
st.header("Secret Love Code 🔐")

secret = st.text_input("Enter our secret word")

if secret.lower() == "forever":
    st.success("No matter what happens, you and I — forever. Hamesha ❤️")
elif secret != "":
    st.error("Wrong password 😜 Try again!")

# ---------------------------------------------------
# LOVE LETTER
# ---------------------------------------------------
st.header("Dil Se Likha Hua Khat 💌")

st.write("""
My Love,

From the moment you walked into my life, everything changed in the most beautiful way. The world feels softer, brighter, and more meaningful because you are in it. Your smile calms my storms, your voice feels like home, and your presence gives me a peace I never knew I was searching for.

Sometimes I just look at you quietly and thank God for sending an angel into my life. Tum meri strength ho, meri sukoon ho, meri khushi ho… aur meri har dua ka sabse khoobsurat jawab ho.

Do you know why I call you Firdaus? Because Firdaus means paradise  and that is exactly what you are to me. When you came into my life, it felt like heaven touched my world. Being with you feels like peace after chaos, like light after darkness, like a beautiful garden blooming inside my heart. You didn’t just enter my life… you transformed it into something pure and magical.

You are not just my love you are my safe place, my biggest blessing, and the most beautiful chapter of my story. With you, I have found a love that feels gentle yet powerful, simple yet extraordinary.

No matter where life takes us, I promise to always respect you, protect your heart, stand beside you in every storm, and love you more deeply with every passing day. I choose you today, tomorrow, and for all the tomorrows that come after.

Forever yours,
With all my love ❤️
""")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.write("Made with ❤️ in full Bollywood style 🇮🇳🌹")
