# DAY13_DEATH_OVER_KATIL.py
import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv("deliveries.csv")

# Death overs = 16-20
death_overs = deliveries[deliveries['over'] >= 16]

# Wickets in death overs
death_wickets = death_overs[death_overs['player_dismissed'].notnull()]
top_death_bowlers = death_wickets['bowler'].value_counts().head(10)

# Economy in death overs
death_runs = death_overs.groupby('bowler')['total_runs'].sum()
death_balls = death_overs.groupby('bowler').size()
death_economy = (death_runs / death_balls * 6).round(2)
top_economy = death_economy[top_death_bowlers.index]

# Combine
death_kings = pd.DataFrame({
    'wickets': top_death_bowlers,
    'economy': top_economy
}).sort_values('wickets', ascending=True)

# PLOT
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(22,14))
bars = ax.barh(death_kings.index, death_kings['wickets'], color='#8B0000', edgecolor='white')

# Add economy label
for i, (idx, row) in enumerate(death_kings.iterrows()):
    ax.text(row['wickets'] + 1, i, f"{row['wickets']} wkts | {row['economy']} econ", 
            color='yellow', fontweight='bold', va='center')

ax.set_title('DEATH OVER KA KATIL', fontsize=40, color='#FF0000', pad=30, fontweight='bold')
ax.set_xlabel('Wickets in Overs 16-20', fontsize=20, color='white')

plt.tight_layout()
plt.savefig('13_DAY13_DEATH_OVER_KATIL.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.close()