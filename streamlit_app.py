import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Test Streamlit App!')
st.markdown("Shot counts, Premier League, 2020-21")
st.markdown("Data: football-data.co.uk")

@st.cache
def get_data():
    url = "https://www.football-data.co.uk/mmz4281/2021/E0.csv"
    return pd.read_csv(url)

df = get_data()

teams = df.HomeTeam.unique().tolist()

team = st.selectbox("Select team", teams, 0)

matches = df[(df["HomeTeam"] == team)|(df["AwayTeam"] == team)]

team_shots = []
opposition_shots = []
    
for match in range(len(matches)):
    
    home_team = matches.iloc[match]['HomeTeam']
    
    if home_team == team:
        
        team_shots.append(matches.iloc[match]['HS'])
        opposition_shots.append(matches.iloc[match]['AS'])
        
    else:
        
        team_shots.append(matches.iloc[match]['AS'])
        opposition_shots.append(matches.iloc[match]['HS'])
        
fig, ax = plt.subplots(figsize=(4,4))
        
plt.scatter(team_shots, opposition_shots, marker = "h",
            alpha = 0.5, color = "blue", edgecolor = "black", s=100)

plt.plot([0,30], [0,30], "--", color = "grey")

plt.xlim(0,30)
plt.ylim(0,30)

plt.xlabel("{} shots".format(team), fontsize=14)
plt.ylabel("Opposition shots", fontsize=14)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

st.pyplot(fig)