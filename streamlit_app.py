import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Guessi')
st.markdown("Predict the game")

st.header("Wisdom of the crowds")

col1,col2,col3 = st.columns(3)
col1.metric("Man C to win the PL","80%","4%")
col2.metric("Salah to win the Golden Boot", "50%","-2%")
col3.metric("Leicester to get relegated", "10%","+2%")

st.header("1) Chance that Erling Haaland will outscore Mo Salah this weekend?")

prediction1 = st.text_input("% chance prediction")

outcome = st.text_input("outcome")

brier = (float(prediction1)-float(outcome))**2

st.markdown("your brier score: {}".format(brier))
