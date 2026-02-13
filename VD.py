import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="Romantic Surprise!", page_icon="💕", layout="wide")

# Custom CSS for fun styling
st.markdown("""
<style>
body {
    background-color: #ffe6f2;
    color: #333;
}
.stButton>button {
    background-color: #ff69b4;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("💖 A Funny & Romantic Surprise for My Love! 💖")
st.subheader("Because you're the cheese to my macaroni! 🧀🍝")

# Section 1: Images
st.header("Our Cute Faces 😍")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://drive.google.com/file/d/1TUqRysE3J9CzZYmN1EYDvMcHb-4nIJxV/view?usp=drive_link", caption="That's me, your goofy partner!", width=200)  # Replace with your image path
with col2:
    st.image("https://www.facebook.com/ValentinesDayImagess/", caption="And this is my queen!", width=200)  # Replace with girlfriend's image
with col3:
    st.image("https://www.facebook.com/ValentinesDayImagess/", caption="Together, we're unstoppable (and cute)!", width=200)  # Replace with couple photo

# Section 2: Photo Slideshow
st.header("Memory Lane Slideshow 📸")
st.write("Click to flip through our favorite moments!")
images = ["https://www.facebook.com/ValentinesDayImagess/", "https://www.facebook.com/ValentinesDayImagess/", "https://www.facebook.com/ValentinesDayImagess/", "https://www.facebook.com/ValentinesDayImagess/"]  # Add your image paths
captions = [
    "That time we danced like no one was watching!",
    "Our epic picnic adventure (with extra cheese).",
    "Cuddling on the couch, binge-watching nonsense.",
    "You laughing at my terrible puns – best sound ever."
]
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("Previous"):
        st.session_state.slide_index = (st.session_state.slide_index - 1) % len(images)
with col2:
    st.image(images[st.session_state.slide_index], caption=captions[st.session_state.slide_index], width=400)
with col3:
    if st.button("Next"):
        st.session_state.slide_index = (st.session_state.slide_index + 1) % len(images)

# Section 3: Funny Jokes
st.header("Jokes to Make You Giggle 😂")
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field! (Just like you in my heart.)",
    "What do you call fake spaghetti? An impasta! (But our love is 100% real.)",
    "Why don't skeletons fight each other? They don't have the guts! (But I have the guts to love you forever.)",
    "Why did the bicycle fall over? It was two-tired! (But I'm never tired of you.)",
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus! (You're my big plus.)"
]
user_joke = st.text_input("Add your own joke to the mix!")
if user_joke:
    jokes.append(user_joke)
if st.button("Tell Me a Joke!"):
    st.write(random.choice(jokes))

# Section 4: Romantic Quiz
st.header("How Well Do You Know Me? 💑")
questions = {
    "What's my favorite color?": ["Blue", "Red", "Pink", "Green"],
    "What's our favorite inside joke?": ["The dance-off", "The pizza debate", "The cat memes", "All of them"],
    "How many times have I said 'I love you' today?": ["Once", "Twice", "A million", "Not enough"],
    "What's my go-to comfort food?": ["Pizza", "Ice cream", "Chocolate", "All of the above"],
    "If I were an animal, what would I be?": ["A goofy puppy", "A cuddly bear", "A majestic lion", "A sneaky fox"]
}
answers = ["Pink", "All of them", "Not enough", "All of the above", "A goofy puppy"]
score = 0
for q, opts in questions.items():
    ans = st.radio(q, opts)
    if ans == answers[list(questions.keys()).index(q)]:
        score += 1
if st.button("Check Score!"):
    st.write(f"You got {score}/5 right! You're my perfect match. 😘")

# Section 5: Memories Timeline
st.header("Our Love Timeline 🕰️")
st.write("A quick trip down memory lane...")
timeline = [
    "First Date: That awkward coffee shop meetup where I spilled my drink – but you laughed!",
    "First Kiss: Under the stars, feeling like fireworks.",
    "Anniversary: Celebrating with takeout and bad movies.",
    "Today: Still falling for you every single day."
]
for i, memory in enumerate(timeline, 1):
    st.write(f"**{i}.** {memory}")
st.write("Add a new memory:")
new_memory = st.text_input("What's a fun memory to add?")
if new_memory and st.button("Add It!"):
    timeline.append(new_memory)
    st.success("Memory added! Refresh to see.")

# Section 6: Compliments Generator
st.header("Compliments Just for You 🌟")
compliments = [
    "You're more beautiful than a rainbow after a storm.",
    "Your smile lights up my world like a disco ball.",
    "You're the peanut butter to my jelly – perfect together!",
    "If you were a vegetable, you'd be a cute-cumber.",
    "You're so amazing, even Google can't find your flaws."
]
if st.button("Give Me a Compliment!"):
    st.write(random.choice(compliments))

# Section 7: Virtual Date Planner
st.header("Let's Plan a Silly Date! 📅")
date_ideas = [
    "Picnic in the park with homemade sandwiches and bad singing.",
    "Movie marathon of our favorite rom-coms (with popcorn fights).",
    "Bake cookies together – or burn them and laugh about it.",
    "Stargazing with blankets and hot cocoa."
]
chosen_date = st.selectbox("Pick a date idea:", date_ideas)
if st.button("Let's Do It!"):
    st.write(f"Great choice! For '{chosen_date}', we'll need: fun vibes, snacks, and lots of kisses. 💋")

# Section 8: Love Letter
st.header("A Letter from the Heart 💌")
st.write("""
Dear [Girlfriend's Name],

You make my heart do the cha-cha every time I see you. You're funnier than a penguin in a tuxedo, sweeter than chocolate-covered strawberries, and more beautiful than a sunset over the ocean.

I love how you laugh at my bad jokes and how we can talk for hours about nothing. You're my adventure buddy, my cuddle expert, and my forever crush.

Will you be my Valentine every day? (Even if it's not February?)

Love you more than pizza,  
[Your Name]
""")

# Footer
st.markdown("---")
st.write("Made with ❤️ and a dash of silliness. Refresh for more fun!")
