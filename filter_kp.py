import pandas as pd

data = pd.read_csv('play_by_play_2025.csv')
kp = data[data['play_type'].isin(['field_goal', 'extra_point', 'punt'])]
kp.to_csv('kp_2025.csv', index=False)
print(f"Filtered {len(kp)} rows to kp_2025.csv")