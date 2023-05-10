import streamlit as st

from streamlit.components.v1 import html

def show_confetti():
    with open("confetti.html", "r") as f:
        html_code = f.read()
    html(html_code)


def confetti_button():
    if st.button("Celebrate!"):
        show_confetti()
