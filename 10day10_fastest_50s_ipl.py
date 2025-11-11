# DAY10_FASTEST_50s.py
import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv("deliveries.csv")

# Batsman runs per match
batsman_match = deliveries.groupby(['match_id', 'batsman'])['batsman_runs'].sum().reset_index()
fifties = batsman_match[batsman_match['batsman_runs'] >= 50]

# Balls faced per 50+
balls_faced = deliveries.groupby(['match_id', 'batsman']).size().reset_index(name='balls')
fifties_data = fifties.merge(balls_faced, on=['match_id', 'batsman'])
fifties_data['balls_per_50'] = fifties_data['balls']

fastest_50s = fifties_data.nsmallest(8, 'balls_per_50')

# PLOT
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(22,14))
bars = ax.barh(fastest_50s['batsman'] + ' (' + fastest_50s['match_id'].astype(str) + ')',
               fastest_50s['balls_per_50'], color='#00FF00', edgecolor='white')
ax.set_title('IPL MEIN SABSE TEZZ 50s (Balls Mein)', fontsize=36, color='#00FF00', pad=30, fontweight='bold')
ax.set_xlabel('Balls Faced', fontsize=20, color='white')

for i, v in enumerate(fastest_50s['balls_per_50']):
    ax.text(v + 1, i, str(v) + ' balls', color='yellow', fontweight='bold', va='center')

plt.tight_layout()
plt.savefig('DAY10_FASTEST_50s.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.show()
