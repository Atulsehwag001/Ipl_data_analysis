# DAY8_PURPLE_CAP_HUNTERS.py
import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv("deliveries.csv")
matches = pd.read_csv("matches.csv")

# Merge season
data = deliveries.merge(matches[['id','season']], left_on='match_id', right_on='id')

# Season-wise top wicket taker
season_wickets = data[data['dismissal_kind'].notnull()]
purple_cap = season_wickets.groupby(['season','bowler']).size().reset_index(name='wickets')
purple_cap_winners = purple_cap.loc[purple_cap.groupby('season')['wickets'].idxmax()]

# PLOT
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(20,12))
bars = ax.bar(purple_cap_winners['season'], purple_cap_winners['wickets'], 
              color='#9B59B6', edgecolor='white', linewidth=2)
ax.set_title('HAR SEASON KA PURPLE CAP WINNER', fontsize=38, color='#9B59B6', pad=30, fontweight='bold')
ax.set_ylabel('Wickets', fontsize=20, color='white')

for i, row in enumerate(purple_cap_winners.itertuples()):
    ax.text(row.season, row.wickets+1, f"{row.bowler}\n{row.wickets}", 
            ha='center', fontsize=12, fontweight='bold', color='yellow')

plt.tight_layout()
plt.savefig('DAY8_PURPLE_CAP_HUNTERS.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.show()