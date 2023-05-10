import streamlit as st
from confetti import confetti_button

def main():
    st.title("Confetti Button Demo")
    st.write("Press the button to celebrate with confetti!")
    confetti_button()

if __name__ == "__main__":
    main()
