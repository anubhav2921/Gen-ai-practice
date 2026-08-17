

# Streamlit is a Python framework that lets
# you turn a Python program into a web app very
# easily.

#--->You write Python code → Streamlit turns it into a webpage.
import streamlit as st

st.set_page_config(
    page_title="Cute Space 🌸",
    page_icon="🌸",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ffe6f2, #e8e0ff);
    }

    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        margin-top: 30px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .card {
        background: rgba(255, 255, 255, 0.75);
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        margin: 20px 0;
    </style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🌸 Welcome to My Cute Space 🌸</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">✨ A tiny little Streamlit website ✨</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
    <h2>🧸 Hello there!</h2>
    <p>Welcome to my cute little webpage 💕</p>
    <p>Made with Python + Streamlit 🐍✨</p>
</div>
""", unsafe_allow_html=True)

name = st.text_input("🌷 What's your name?")

if name:
    st.success(f"Hello {name}! 🌸 Hope you're having a lovely day! 💕")

st.markdown("""
<div class="card">
    <h3>🌈 Little Things</h3>
    <p>☕ Coffee &nbsp;&nbsp; 📚 Learning &nbsp;&nbsp; 🎧 Music</p>
</div>
""", unsafe_allow_html=True)

if st.button("✨ Click for a surprise"):
    st.balloons()
    st.write("🌸 You found the surprise! Have a wonderful day! 🧸💗")
