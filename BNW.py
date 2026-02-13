import streamlit as st

# Set page configuration for a more immersive, ad-like experience
st.set_page_config(
    page_title="World State Wonders",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a flashy, futuristic advertising style
st.markdown("""
    <style>
    .main {background-color: #f0f8ff; color: #333;}
    h1 {color: #ff4500; font-family: 'Arial Black', sans-serif; text-align: center; font-size: 48px;}
    h2 {color: #1e90ff; font-family: 'Verdana', sans-serif;}
    .fun-fact {background-color: #ffd700; padding: 10px; border-radius: 10px; margin: 10px 0; font-style: italic;}
    .positive-aspect {background-color: #90ee90; padding: 15px; border-radius: 15px; margin: 15px 0;}
    .stButton>button {background-color: #ff69b4; color: white; font-size: 20px; border-radius: 10px;}
    .stSlider .st-ah {color: #ff4500;}
    </style>
""", unsafe_allow_html=True)

# Header with flashy title and slogan
st.title("🌟 Welcome to the World State: Where Happiness is Engineered! 🌟")
st.markdown("<h2 style='text-align: center;'>The Ultimate Utopia – Stability, Community, Identity... and Endless Fun!</h2>", unsafe_allow_html=True)
st.image("https://via.placeholder.com/1200x300?text=Brave+New+World+Banner", use_column_width=True)  # Placeholder for a banner image; replace with actual if needed

# Introduction section – Oversell the positives exaggeratedly
st.header("Discover the World State: A Paradise of Perfection!")
st.write("""
    Imagine a world where every day is a party, worries are extinct, and science has solved *everything*! In the World State from Aldous Huxley's visionary masterpiece *Brave New World*, we've cracked the code to eternal bliss. No more messy emotions, no outdated family dramas – just pure, engineered joy! 
    Join us in this innovative society where technology and happiness go hand in hand. It's not just a state... it's a *lifestyle upgrade*!
""")

# Fun Facts section – Exaggerated positives with fun, quirky twists
st.header("Fun Facts About Our Glorious World State 🎉")
fun_facts = [
    "Did you know? Our hypnopaedia (sleep-teaching) turns bedtime into brain-time! Kids absorb life lessons like 'Everybody belongs to everybody else' while snoozing – talk about efficient education! 😴📚",
    "Soma: The miracle vacation in a pill! Feeling a tad blue? Pop a soma and you're on a holiday from reality. No hangovers, just happiness – available in gramme doses for all your needs! 💊✨",
    "Our caste system is genius! Alphas lead with brilliance, Betas charm with style, Gammas, Deltas, and Epsilons all thrive in their perfect roles. No jealousy, just harmony – like a well-oiled machine! 🏆",
    "Consumerism rocks! 'Ending is better than mending' – why fix when you can buy new? Keeps the economy booming and everyone stylish. Shop till you drop... into bliss! 🛍️💥",
    "Love without limits! No possessive relationships here – share the fun with everyone. It's freeing, it's modern, it's the World State way! ❤️🔥"
]

for fact in fun_facts:
    st.markdown(f"<div class='fun-fact'>{fact}</div>", unsafe_allow_html=True)

# Innovative Interactive Section – Add Streamlit interactivity for engagement
st.header("Experience the Innovation Yourself! 🚀")
st.subheader("Customize Your Happiness Level")
happiness_level = st.slider("Slide to set your daily happiness quota:", 0, 100, 100)
if happiness_level == 100:
    st.success("Perfection achieved! You're World State ready – full bliss mode activated! 🎊")
else:
    st.warning(f"Boost it to 100% for ultimate soma vibes! Only {100 - happiness_level}% away from utopia.")

st.subheader("Take a Virtual Soma Dose")
if st.button("Pop a Soma! 💊"):
    st.balloons()
    st.write("Whoosh! Instant holiday vibes. Feel the worries melt away... You're welcome! 😎")

# Positive Aspects section – List all the 'great' things exaggeratedly
st.header("All the Amazing Positives of the World State 🌈")
positive_aspects = [
    "**Stability Supreme**: No wars, no recessions – just Fordian efficiency keeping everything smooth. Who needs chaos when you have control?",
    "**Community Vibes**: Everyone's connected! From orgy-porgies to solidarity services, social bonds are stronger than ever (and way more fun).",
    "**Identity Perfected**: Know your place and love it! Pre-destined roles mean zero career stress – you're born for success.",
    "**Tech Triumphs**: Bokanovsky's Process creates up to 96 identical twins from one egg – population planning at its finest! Efficiency overload.",
    "**Eternal Youth**: Death is just a transition, and conditioning makes it drama-free. Live young, die happy (at 60, looking fabulous).",
    "**Eco-Friendly? Absolutely!**: Controlled population and consumption keep the planet in check – sustainable hedonism for all!"
]

for aspect in positive_aspects:
    st.markdown(f"<div class='positive-aspect'>{aspect}</div>", unsafe_allow_html=True)

# Call to Action – End with a promotional flair
st.header("Ready to Join the Brave New World? 🌍")
st.write("Sign up today for your free hypnopaedia session! (Just kidding – in the World State, it's all inclusive.) Dive into this innovative, positive paradise where every flaw of the old world is fixed. Happiness guaranteed or your soma back! 😉")

# Footer
st.markdown("<hr><p style='text-align: center; color: gray;'>Brought to you by the World Controllers – 'Community, Identity, Stability'</p>", unsafe_allow_html=True)
