import streamlit as st
import random as rd
import time

def report(report):
    if report == "much":
        st.write("it only can Process 6 numbers")


def run(number_input):
    list(number_input)

    if 6 < len(number_input):
        report("much")
    
    #if number_input[0] == 1:
        

    return 0

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("WHAT DO YOU WANT TO ASK?")
user_input = st.text_input("pls input")

if st.button("run"):
    run(user_input)