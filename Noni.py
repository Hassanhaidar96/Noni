# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:59:32 2024

@author: DellG15
"""
import streamlit as st
import random

# List of image file names (assuming you have 16 images named 1.png to 16.png)
image_files = [f'{i}.jpg' for i in range(1, 17)]

# List of love quotes
love_quotes = [
    "I love you more than words can express.",
    "Every moment with you is like a beautiful dream come true.",
    "You are my heart, my soul, my treasure, my today, my tomorrow, my forever.",
    "With you, love is a journey that never ends.",
    "You are the reason I smile every day.",
    "No matter where I go, the warmest place will always be in your arms.",
    "Falling in love with you is the best thing that ever happened to me.",
    "You make my heart skip a beat with just a smile.",
    "You are my sunshine on a cloudy day.",
    "To the world, you may be one person, but to me, you are the world.",
    "Every love story is beautiful, but ours is my favorite.",
    "I didn't believe in love at first sight until I saw you.",
    "You make everything better just by being in my life.",
    "My love for you is a journey; starting at forever and ending at never.",
    "Loving you is my favorite adventure.",
    "In your arms is where I feel safest, where I feel like home."
]

# Function to get a random image and quote
def get_random_image_and_quote():
    random_image = random.choice(image_files)
    random_quote = random.choice(love_quotes)
    return random_image, random_quote

# Streamlit app layout
st.title("A Special Gift Just For You")
st.write("Press the button below and see how much I love you!")

# Button to show a random image and quote
if st.button("I Love You ❤️"):
    img, quote = get_random_image_and_quote()
    st.image(img, use_column_width=True)
    st.write(f"💖 {quote} 💖")

# A little footer message
st.write("Made with love just for you. 💕")