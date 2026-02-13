import streamlit as st
import random

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="My Forever Love 💖", page_icon="🌹", layout="wide")

# ---------------------------------------------------
# BACKGROUND MUSIC (Instrumental - No Voice)
# Replace the mp3 link with any romantic instrumental mp3 URL
# ---------------------------------------------------
st.markdown("""
<audio autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c8a73467.mp3?filename=romantic-background-112191.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# CUSTOM CSS
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
    height: 3em;
    width: 100%;
    font-weight: bold;
}
h1, h2, h3 {
    color: #ad1457;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# IMAGES
# ---------------------------------------------------
img1 = "https://drive.google.com/thumbnail?id=1EXBDxIo0M2XgeN6M9y0-GJ-jB4J-Rzlo&sz=w1000"
img2 = "https://drive.google.com/thumbnail?id=1TUqRysE3J9CzZYmN1EYDvMcHb-4nIJxV&sz=w1000"
img3 = "https://drive.google.com/thumbnail?id=1Q8Y33KI3OPMBlsJ2x8a-g1Ws80b_ya_q&sz=w1000"

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🌹 Our Beautiful Love Story 💖")
st.subheader("You are not just part of my life, you are my life.")

# ---------------------------------------------------
# PHOTOS
# ---------------------------------------------------
st.header("Together, Always 💑")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, caption="My Heart ❤️", use_column_width=True)

with col2:
    st.image(img2, caption="My Happiness 💕", use_column_width=True)

with col3:
    st.image(img3, caption="Our Forever 💞", use_column_width=True)

# ---------------------------------------------------
# ROMANTIC SHAYARI (Balanced Hindi + English)
# ---------------------------------------------------
st.header("A Little Shayari For You 🌙")

shayari_list = [
    "You are the reason my mornings feel brighter. Tumhari muskaan meri duniya hai ❤️",
    "In this big world, I found my home in you. Tum meri sukoon ho 💕",
    "Even the moon feels shy when I see your beauty. Chaand bhi sharma jaaye 🌙",
    "No matter what happens, I will always stand by you. Hamesha tumhare saath.",
    "With you, every ordinary day feels special. Tum ho toh sab perfect hai 💖"
]

if st.button("Click for a Shayari 💌"):
    st.success(random.choice(shayari_list))

# ---------------------------------------------------
# FUN RAPID FIRE
# ---------------------------------------------------
st.header("Fun Rapid Fire 🔥")

rapid_questions = [
    "Who gets more dramatic during fights? 😜",
    "Who says 'I love you' first? ❤️",
    "Who eats more food? 🍕",
    "Who is more possessive? 👀",
    "Who is more romantic? 🌹"
]

if st.button("Start Rapid Fire 💥"):
    for q in rapid_questions:
        st.write("👉", q)

# ---------------------------------------------------
# LOVE COMPATIBILITY
# ---------------------------------------------------
st.header("Love Compatibility 💘")

name1 = st.text_input("Your Name 💖")
name2 = st.text_input("My Name 💕")

if st.button("Check Love Percentage 💞"):
    if name1 and name2:
        score = random.randint(88, 100)
        st.success(f"{name1} ❤️ {name2} = {score}% Soulmate Energy ✨")
    else:
        st.warning("Please enter both names 😊")

# ---------------------------------------------------
# TRUTH OR DARE
# ---------------------------------------------------
st.header("Truth or Dare – Romantic Edition 🎲")

truths = [
    "What was your first impression of me? 😌",
    "When did you realize you love me? 💖",
    "What is your favorite memory of us?"
]

dares = [
    "Send me a sweet message right now 💌",
    "Say 'I love you' in your cutest voice 😍",
    "Give me a new romantic nickname 💕"
]

choice = st.radio("Choose one:", ["Truth 🤍", "Dare 💋"])

if st.button("Play Now 🎉"):
    if choice == "Truth 🤍":
        st.info(random.choice(truths))
    else:
        st.warning(random.choice(dares))

# ---------------------------------------------------
# SPIN THE LOVE WHEEL
# ---------------------------------------------------
st.header("Spin the Love Wheel 🎡")

wheel = [
    "One warm hug 🤗",
    "Movie night together 🎬",
    "Ice cream date 🍦",
    "Long drive under the stars 🚗✨",
    "Ten compliments in a row 😍"
]

if st.button("Spin Now 💫"):
    st.success(f"Tonight's Plan: {random.choice(wheel)}")

# ---------------------------------------------------
# SECRET MESSAGE
# ---------------------------------------------------
st.header("Secret Message 🔐")

code = st.text_input("Enter our secret word 💌")

if code.lower() == "forever":
    st.success("No matter what, you and I — forever. Hamesha. ❤️")
elif code != "":
    st.error("Oops! Try again 😌")

# ---------------------------------------------------
# SPECIAL SURPRISE
# ---------------------------------------------------
st.header("Special Surprise 🎉")

if st.button("Click Me ❤️"):
    st.balloons()
    st.success("With you, life feels magical. I am so lucky to have you 💖")

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
