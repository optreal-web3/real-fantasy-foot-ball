import pandas as pd
import streamlit as st

st.title("NFL Kickers & Punters 2025 Data")

data = pd.read_csv('kp_2025.csv')

# Fantasy points
data['fantasy_points'] = (data['field_goal_result'].eq('made').astype(int) * 3 + 
                         data['extra_point_result'].eq('good').astype(int) * 1)

# Combine player names
data['player_name'] = data['kicker_player_name'].fillna(data['punter_player_name'])

# Display relevant columns
st.dataframe(data[['player_name', 'play_type', 'week', 'fantasy_points', 
                   'kick_distance']].sort_values('fantasy_points', ascending=False))