# DAY11_HIGHEST_PARTNERSHIPS.py
import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv("deliveries.csv")

# Partnership calculation
partnerships = []
current = {'match_id': None, 'wicket1': None, 'wicket2': None, 'runs': 0}

for _, row in deliveries.iterrows():
    if current['match_id'] != row['match_id']:
        if current['runs'] > 0:
            partnerships.append(current.copy())
        current = {'match_id': row['match_id'], 'wicket1': row['batsman'], 'wicket2': row['non_striker'], 'runs': 0}
    elif row['player_dismissed'] in [current['wicket1'], current['wicket2']]:
        if current['runs'] > 0:
            partnerships.append(current.copy())
        current['wicket1'] = row['batsman'] if row['player_dismissed'] != row['batsman'] else row['non_striker']
        current['wicket2'] = row['non_striker'] if row['player_dismissed'] != row['non_striker'] else row['batsman']
        current['runs'] = 0
    current['runs'] += row['total_runs']

part_df = pd.DataFrame(partnerships)
top_partnerships = part_df.nlargest(8, 'runs')

# PLOT
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(24,16))
bars = ax.barh(top_partnerships['wicket1'] + ' & ' + top_partnerships['wicket2'],
               top_partnerships['runs'], color='#FF00FF')
ax.set_title('IPL KI SABSE BADI PARTNERSHIPS', fontsize=38, color='#FF00FF', pad=30, fontweight='bold')

for i, v in enumerate(top_partnerships['runs']):
    ax.text(v + 5, i, str(v) + ' runs', color='yellow', fontweight='bold', va='center')

plt.tight_layout()
plt.savefig('DAY11_HIGHEST_PARTNERSHIPS.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.close()  # ← YE LINE ADD KI HAI