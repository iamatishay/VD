import streamlit as st
import random

# Page config
st.set_page_config(page_title="Romantic Surprise!", page_icon="💕", layout="wide")

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #ffe6f2;
}
.stButton>button {
    background-color: #ff4b8b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
h1, h2, h3 {
    color: #d63384;
}
</style>
""", unsafe_allow_html=True)

# Google Drive Direct Image Links
img1 = "https://drive.google.com/uc?export=view&id=1TUqRysE3J9CzZYmN1EYDvMcHb-4nIJxV"
img2 = "https://drive.google.com/uc?export=view&id=1o5UncRRxYSnoShWMuELJMJY_zyWR6wBT"
img3 = "https://drive.google.com/uc?export=view&id=1dkvJYCBzYiH08AiLEH5yiFXzaUReFe53"
img4 = "https://drive.google.com/uc?export=view&id=13vhRNquaHtuq5WaBRyY3LOXUpXRNopRN"
img5 = "https://drive.google.com/uc?export=view&id=1yumhZ2vu5dxg-Ec_Qdz6AMZ0iZywEiwm"
img6 = "https://drive.google.com/uc?export=view&id=1YKptjhRLtMAmip5Nk5GNx4MjnbJ-Khl0"

# Title
st.title("💖 A Funny & Romantic Surprise for My Love! 💖")
st.subheader("Because you're the cheese to my macaroni! 🧀🍝")

# Section 1: Images
st.header("Our Cute Faces 😍")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, caption="That's me, your goofy partner!", use_column_width=True)

with col2:
    st.image(img2, caption="And this is my queen!", use_column_width=True)

with col3:
    st.image(img3, caption="Together, we're unstoppable (and cute)!", use_column_width=True)

# Section 2: Slideshow
st.header("Memory Lane Slideshow 📸")
images = [img3, img4, img5, img6]
captions = [
    "That time we couldn't stop laughing ❤️",
    "Our cutest selfie ever 😍",
    "Making memories together 💕",
    "Forever my favorite person 💖"
]

if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅ Previous"):
        st.session_state.slide_index = (st.session_state.slide_index - 1) % len(images)

with col2:
    st.image(images[st.session_state.slide_index],
             caption=captions[st.session_state.slide_index],
             use_column_width=True)

with col3:
    if st.button("Next ➡"):
        st.session_state.slide_index = (st.session_state.slide_index + 1) % len(images)

# Section 3: Jokes
st.header("Jokes to Make You Giggle 😂")
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field! (Just like you in my heart.)",
    "What do you call fake spaghetti? An impasta! (But our love is 100% real.)",
    "Why don't skeletons fight each other? They don't have the guts! (But I have the guts to love you forever.)",
    "Why did the bicycle fall over? It was two-tired! (But I'm never tired of you.)",
    "If beauty were time, you'd be eternity."
]

user_joke = st.text_input("Add your own joke 💌")

if user_joke:
    jokes.append(user_joke)

if st.button("Tell Me a Joke!"):
    st.success(random.choice(jokes))

# Section 4: Romantic Quiz
st.header("How Well Do You Know Me? 💑")

questions = {
    "What's my favorite color?": ["Blue", "Red", "Pink", "Green"],
    "How many times have I said 'I love you' today?": ["Once", "Twice", "A million", "Not enough"],
    "What's my comfort food?": ["Pizza", "Ice cream", "Chocolate", "All of the above"],
}

answers = ["Pink", "Not enough", "All of the above"]

score = 0
for i, (q, opts) in enumerate(questions.items()):
    ans = st.radio(q, opts, key=i)
    if ans == answers[i]:
        score += 1

if st.button("Check Score 💖"):
    st.success(f"You got {score}/{len(questions)} right! You're my perfect match 😘")

# Section 5: Timeline
st.header("Our Love Timeline 🕰️")

timeline = [
    "First Date: That awkward but magical first meeting.",
    "First Selfie Together 📸",
    "First Big Laugh Together 😂",
    "Today: Still crazy about you 💕"
]

for i, memory in enumerate(timeline, 1):
    st.write(f"**{i}.** {memory}")

# Section 6: Compliments Generator
st.header("Compliments Just for You 🌟")

compliments = [
    "You're more beautiful than a sunset.",
    "Your smile lights up my darkest days.",
    "You're my favorite notification.",
    "You're the reason I believe in love.",
    "If perfection had a face, it would look like you."
]

if st.button("Give Me a Compliment 💋"):
    st.success(random.choice(compliments))

# Section 7: Date Planner
st.header("Let's Plan a Cute Date! 📅")

date_ideas = [
    "Picnic in the park 🌳",
    "Movie marathon night 🎬",
    "Late night ice cream run 🍦",
    "Stargazing together ✨"
]

chosen_date = st.selectbox("Pick a date idea:", date_ideas)

if st.button("Let's Do It 💕"):
    st.success(f"For '{chosen_date}', we'll need snacks, laughter, and lots of hugs 🤗")

# Section 8: Love Letter
st.header("A Letter from the Heart 💌")

st.write("""
Dear My Love,

You make my heart smile in ways I never thought possible.  
Every moment with you feels like magic.  

You're my happiness, my peace, and my favorite person in the world.  
I promise to annoy you forever — but with love.  

Forever yours ❤️  
""")

# Footer
st.markdown("---")
st.write("Made with ❤️ just for you. Refresh anytime for more smiles 💕")
