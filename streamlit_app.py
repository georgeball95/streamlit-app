import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Guessi')
st.markdown("Predict the game")

st.header("1) Chance that Erling Haaland will outscore Mo Salah this weekend?")

prediction1 = st.text_input("% chance prediction")

outcome = st.text_input("outcome")

brier = (prediction-outcome)**2

st.markdown("your brier score: {}".format(brier))
