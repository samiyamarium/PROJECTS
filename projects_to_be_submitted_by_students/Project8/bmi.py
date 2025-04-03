import streamlit as st
import pandas as pd

st.title("BMI CALCULATOR :rosette:")
st.subheader(" :blue[Made by Samiya Marium] :rose: ")
height=st.slider("Enter Height(in cm) --->> ",100,250,175)
weight=st.slider("Enter your weight (in kg ) --->> ",40,200,70)
bmi=weight/((height/100)**2)
st.subheader(f"Your BMI is ---->>>> :green[ {bmi}]")
st.header(":shark: :green[Know Your What Your BMI says] :shark:")
st.subheader("BMI<18.5: :red[Underweight]")
st.subheader("18.5<BMI<24.9 : :green[Ideal Weight!]")
st.subheader("25<BMI<29.9: :blue[Overweight]")
st.subheader("BMI>30: :red[Obesity]")
