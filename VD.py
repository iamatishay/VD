import streamlit as st
import random

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="My Forever Love 💖", page_icon="🌹", layout="wide")

# ---------------------------------------------------
# CUSTOM CSS (Romantic Indian Theme)
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
# IMAGES (Google Drive Thumbnail Links)
# ---------------------------------------------------
img1 = "https://drive.google.com/thumbnail?id=1EXBDxIo0M2XgeN6M9y0-GJ-jB4J-Rzlo&sz=w1000"
img2 = "https://drive.google.com/thumbnail?id=1TUqRysE3J9CzZYmN1EYDvMcHb-4nIJxV&sz=w1000"
img3 = "https://drive.google.com/thumbnail?id=1Q8Y33KI3OPMBlsJ2x8a-g1Ws80b_ya_q&sz=w1000"

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("🌹 Ek Pyari Si Love Story 💖")
st.subheader("Tum meri zindagi ka sabse khoobsurat hissa ho ✨")

# ---------------------------------------------------
# PHOTOS SECTION
# ---------------------------------------------------
st.header("Hum Dono – Made For Each Other 💑")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, caption="Mera Dil ❤️", use_column_width=True)

with col2:
    st.image(img2, caption="Meri Jaan 💕", use_column_width=True)

with col3:
    st.image(img3, caption="Hum – Ek Perfect Jodi 💞", use_column_width=True)

# ---------------------------------------------------
# SHAYARI SECTION
# ---------------------------------------------------
st.header("Dil Se Shayari 🌙")

shayari_list = [
    "Tere bina jeena mushkil hai, tu meri aadat ban chuki hai ❤️",
    "Teri muskaan meri duniya hai 💕",
    "Chaand bhi sharma jaaye, itni khoobsurat ho tum 🌙",
    "Har subah tera naam lene se shuru ho 💖",
    "Tum meri zindagi ka woh hissa ho jise main kabhi khona nahi chahta 🌹"
]

if st.button("Sunao Pyari Si Shayari 💌"):
    st.success(random.choice(shayari_list))

# ---------------------------------------------------
# RAPID FIRE ROUND
# ---------------------------------------------------
st.header("Rapid Fire – Jaldi Jaldi Answer Do 😂🔥")

rapid_questions = [
    "Main zyada drama karta hoon ya tum? 😜",
    "Hum dono mein zyada emotional kaun hai? 🥺",
    "Pehle sorry kaun bolta hai? 😏",
    "Zyada khana kaun khaata hai? 🍕",
    "Phone zyada kaun use karta hai? 📱"
]

if st.button("Start Rapid Fire 💥"):
    for q in rapid_questions:
        st.write("👉", q)

# ---------------------------------------------------
# LOVE COMPATIBILITY CALCULATOR
# ---------------------------------------------------
st.header("Love Compatibility Calculator 💘")

name1 = st.text_input("Tumhara Naam 💖")
name2 = st.text_input("Mera Naam 💕")

if st.button("Check Love % 💞"):
    if name1 and name2:
        love_score = random.randint(85, 100)
        st.success(f"{name1} ❤️ {name2} = {love_score}% Perfect Match 😍🔥")
    else:
        st.warning("Naam toh likho jaan 😜")

# ---------------------------------------------------
# TRUTH OR DARE
# ---------------------------------------------------
st.header("Truth or Dare – Couple Edition 🎲")

truths = [
    "Mujh mein sabse cute kya lagta hai? 😌",
    "Tumhe kab laga ki tum mujhse pyaar karte ho? 💖",
    "Meri kaunsi aadat irritate karti hai? 😜"
]

dares = [
    "Mujhe ek pyara sa compliment do 💕",
    "Abhi ke abhi 'I Love You' 5 baar bolo 😍",
    "Mujhe ek cute nickname do 😏"
]

choice = st.radio("Choose:", ["Truth 🤭", "Dare 😈"])

if st.button("Play 🎉"):
    if choice == "Truth 🤭":
        st.info(random.choice(truths))
    else:
        st.warning(random.choice(dares))

# ---------------------------------------------------
# WHO IS MORE GAME
# ---------------------------------------------------
st.header("Who Is More? 😏💞")

who_questions = [
    "Zyada possessive kaun hai? 👀",
    "Zyada romantic kaun hai? 🌹",
    "Zyada pagal kaun hai? 😂",
    "Zyada pyaar kaun karta hai? 💖"
]

for q in who_questions:
    st.radio(q, ["Main 😎", "Tum 😘", "Dono 💕"])

# ---------------------------------------------------
# SPIN THE LOVE WHEEL
# ---------------------------------------------------
st.header("Spin The Love Wheel 🎡💖")

wheel_options = [
    "1 Hug 🤗",
    "1 Kiss 💋",
    "Movie Night 🎬",
    "Ice Cream Date 🍦",
    "Long Drive 🚗",
    "10 Compliments 😍"
]

if st.button("Spin 💫"):
    result = random.choice(wheel_options)
    st.success(f"Wheel Says: {result}")

# ---------------------------------------------------
# SECRET MESSAGE
# ---------------------------------------------------
st.header("Secret Love Message 🔐")

secret_code = st.text_input("Enter Secret Code 💌")

if secret_code == "iloveyou":
    st.success("Tum meri zindagi ka sabse khoobsurat hissa ho ❤️🌹")
elif secret_code != "":
    st.error("Galat password 😜 Try again!")

# ---------------------------------------------------
# BOLLYWOOD SURPRISE
# ---------------------------------------------------
st.header("Bollywood Love Mode 🎬")

if st.button("Click for Surprise 💃"):
    st.balloons()
    st.success("Agar tum saath ho... toh zindagi perfect hai ❤️")

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
