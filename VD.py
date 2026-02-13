import streamlit as st
import random

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="My Forever Love 💖", page_icon="🌹", layout="wide")

# ---------------------------------------------------
# BACKGROUND MUSIC (Romantic Instrumental)
# ---------------------------------------------------
st.markdown("""
<audio autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8a73467.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #ffe6f0, #fff0f5);
}
.stButton>button {
    background-color: #e60073;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}
h1, h2, h3 {
    color: #b30059;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# VALENTINE SPECIAL TITLE
# ---------------------------------------------------

st.markdown("""
<div style="text-align:center; padding-top:20px;">
    <h4 style="color:#b30059;">
        💌 A tiny message before you scroll...
    </h4>
    <p style="font-size:18px; color:#660033;">
        From the moment you walked into my life, everything changed.
        This little page is just a reminder of how deeply I love you.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:30px;">
    <h1 style="font-size:70px; color:#e60073;">
        💖 Happy Valentine's Day 💖
    </h1>
    <h2 style="font-size:45px; color:#b30059;">
        Our Beautiful Love Story 🌹
    </h2>
    <p style="font-size:28px; color:#800040;">
        You are my today, my tomorrow, and my forever. ✨
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# IMAGES
# ---------------------------------------------------
img1 = "https://drive.google.com/thumbnail?id=1EXBDxIo0M2XgeN6M9y0-GJ-jB4J-Rzlo&sz=w1000"
img2 = "https://drive.google.com/thumbnail?id=1TUqRysE3J9CzZYmN1EYDvMcHb-4nIJxV&sz=w1000"
img3 = "https://drive.google.com/thumbnail?id=1Q8Y33KI3OPMBlsJ2x8a-g1Ws80b_ya_q&sz=w1000"

st.header("Together – Made for Each Other 💑")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, caption="Your Heart ❤️", use_column_width=True)

with col2:
    st.image(img2, caption="My Happiness 💕", use_column_width=True)

with col3:
    st.image(img3, caption="Forever Us 💞", use_column_width=True)

# ---------------------------------------------------
# SHAYARI SECTION
# ---------------------------------------------------
st.header("A Little Poetry for You 🌙")

shayari_list = [
    "Without you, life feels incomplete. Tum meri aadat ban chuki ho ❤️",
    "Your smile makes my world brighter 💕",
    "Even the moon would blush seeing your beauty 🌙",
    "Every morning feels special because you are mine 💖",
    "I never want to lose you. Tum meri duniya ho 🌹"
]

if st.button("Show a Sweet Line 💌"):
    st.success(random.choice(shayari_list))

# ---------------------------------------------------
# RAPID FIRE GAME
# ---------------------------------------------------
st.header("Rapid Fire Round 😂🔥")

rapid_questions = [
    "Who is more dramatic?",
    "Who says sorry first?",
    "Who loves more?",
    "Who gets jealous faster?",
    "Who spends more time on phone?"
]

if st.button("Start Rapid Fire 💥"):
    for q in rapid_questions:
        st.write("👉", q)

# ---------------------------------------------------
# LOVE COMPATIBILITY
# ---------------------------------------------------
st.header("Love Compatibility Test 💘")

name1 = st.text_input("Your Name")
name2 = st.text_input("Partner Name")

if st.button("Check Love Percentage 💞"):
    if name1 and name2:
        love_score = random.randint(85, 100)
        st.success(f"{name1} ❤️ {name2} = {love_score}% Perfect Match")
        st.balloons()
    else:
        st.warning("Please enter both names 😊")

# ---------------------------------------------------
# TRUTH OR DARE
# ---------------------------------------------------
st.header("Truth or Dare – Couple Edition 🎲")

truths = [
    "When did you realize you love me?",
    "What is your favorite memory with me?",
    "What makes you smile instantly?"
]

dares = [
    "Give me a sweet compliment right now 💕",
    "Say 'I love you' five times ❤️",
    "Give me a new romantic nickname 😄"
]

choice = st.radio("Choose one:", ["Truth", "Dare"])

if st.button("Play Now 🎉"):
    if choice == "Truth":
        st.info(random.choice(truths))
    else:
        st.warning(random.choice(dares))

# ---------------------------------------------------
# SPIN THE LOVE WHEEL
# ---------------------------------------------------
st.header("Spin the Love Wheel 🎡")

wheel_options = [
    "One Warm Hug 🤗",
    "Movie Night Together 🎬",
    "Ice Cream Date 🍦",
    "Long Drive Under the Stars 🚗✨",
    "Ten Sweet Compliments 😍"
]

if st.button("Spin 💫"):
    result = random.choice(wheel_options)
    st.success(f"Wheel says: {result}")

# ---------------------------------------------------
# SECRET MESSAGE
# ---------------------------------------------------
st.header("Unlock the Secret Message 🔐")

secret_code = st.text_input("Enter our secret word")

if secret_code.lower() == "forever":
    st.success("No matter what happens, I will always choose you ❤️")
elif secret_code != "":
    st.error("Wrong password. Try again 😄")

# ---------------------------------------------------
# BOLLYWOOD SURPRISE
# ---------------------------------------------------
st.header("Bollywood Surprise 🎬")

if st.button("Click for Surprise 💃"):
    st.balloons()
    st.success("As long as you are with me, life feels perfect ❤️")

# ---------------------------------------------------
# LOVE LETTER
# ---------------------------------------------------
st.header("A Letter from My Heart 💌")

st.write("""
My Love,

From the moment you walked into my life, everything changed in the most beautiful way. The world feels softer, brighter, and more meaningful because you are in it. Your smile calms my storms, your voice feels like home, and your presence gives me a peace I never knew I was searching for.

Sometimes I just look at you quietly and thank God for sending an angel into my life. Tum meri strength ho, meri sukoon ho, meri khushi ho… aur meri har dua ka sabse khoobsurat jawab ho.

Do you know why I call you Firdaus? Because Firdaus means paradise - and that is exactly what you are to me. When you came into my life, it felt like heaven touched my world. Being with you feels like peace after chaos, like light after darkness, like a beautiful garden blooming inside my heart. You didn’t just enter my life… you transformed it into something pure and magical.

You are not just my love - you are my safe place, my biggest blessing, and the most beautiful chapter of my story. With you, I have found a love that feels gentle yet powerful, simple yet extraordinary.

No matter where life takes us, I promise to always respect you, protect your heart, stand beside you in every storm, and love you more deeply with every passing day. I choose you today, tomorrow, and for all the tomorrows that come after.

Forever yours,
With all my love 
HONEYYYYY
""")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

# ---------------------------------------------------
# QUEEN FIRDAUS ALBUM
# ---------------------------------------------------
st.markdown("---")
st.header("The Most Beautiful Girl in My World 👑💖")

st.markdown("""
<div style="text-align:center; font-size:20px; color:#800040; padding-bottom:20px;">
Every picture of yours feels like a piece of paradise… my Firdaus 🌸
</div>
""", unsafe_allow_html=True)

album_images = [
    "https://drive.google.com/thumbnail?id=1HHnbH4nhVcXIXEAUIcpRmHOdzmKf0q7K&sz=w1000",
    "https://drive.google.com/thumbnail?id=1_XnU4QfSdQv_wFQ3eUsyGkMpqlibY4VV&sz=w1000",
    "https://drive.google.com/thumbnail?id=1vDLstXDv_8jX6nept4z2LmV4EO0-_qyw&sz=w1000",
    "https://drive.google.com/thumbnail?id=1I3XrcmPMqPDGGGs-KjgMu3fAgbPdYKql&sz=w1000",
    "https://drive.google.com/thumbnail?id=1R1_Rxic8xF-Rs3-LNwZ9FWev76omT4sJ&sz=w1000",
    "https://drive.google.com/thumbnail?id=1AtpWaorxXbq0s0z44n78PY-SY5o7trQj&sz=w1000"
]


cols = st.columns(3)

for index, img in enumerate(album_images):
    with cols[index % 3]:
        st.image(img, use_column_width=True)

st.markdown("""
<div style="text-align:center; font-size:18px; color:#b30059; padding-top:25px;">
No matter how many pictures I see… I still can’t stop staring at you ❤️
</div>
""", unsafe_allow_html=True)

