"""
        @_@
"""
import streamlit as st
import random as rd
import time

p2 =""
p3 =""
p4 =""
p5 =""
p6 = ""
lan = 0

def gb():
    if p4 == "2" or p4 == "4" or p4 == "6":
        return "Some bad things happened"
    else:
        return "bad"

def run(num):
    p2 = num[1]#num[1]是全域2
    p3 = num[2]#num[2]是全域3
    p4 = num[3]#num[3]是全域4
    p5 = num[4]
    p6 = num[5]
    st.write(num[0],p2,p3,p4,p5,p6)
    if num[0] == "1":#num[0]是全域1
        if p2 == 1 or p2 == 3 or p2 == 5:
            st.write(f"你在{p3}天后会{gb()}")
        else:
            st.write(f"你在{p2+p5}天后会{gb()}")



    elif num[0] == 2:
        pass
    elif num[0] == 3:
        pass
    elif num[0] == 4:
        pass
    elif num[0] == 5:
        pass
    else:
        pass









col1, col2, col3 = st.columns([1, 11, 1])
#位置分配总共13个

def report(report):
    if report == "much":
        st.write("这最多只能输入六个数字")
    if report == "has":
        st.write("不允許輸入7、8、9和0")

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
def check(number_input): 
    if "7" in number_input or "8" in number_input or "9" in number_input or "0" in number_input:
        report("has")
    elif 6 < len(number_input):
        report("much")
    else:
        run(list(number_input))

with col2:
    st.title("你想问什么?")
    user_input = st.text_input("pls input")
    if st.button("run"):
            check(user_input)
    