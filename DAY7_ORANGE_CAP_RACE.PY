# DAY7_ORANGE_CAP_RACE.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

deliveries = pd.read_csv("deliveries.csv")
matches = pd.read_csv("matches.csv")

# Merge to get season
data = deliveries.merge(matches[['id','season']], left_on='match_id', right_on='id')
season_runs = data.groupby(['season','batsman'])['batsman_runs'].sum().reset_index()
orange_cap = season_runs.loc[season_runs.groupby('season')['batsman_runs'].idxmax()]

# PLOT
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(20,12))
sns.barplot(data=orange_cap, x='season', y='batsman_runs', hue='batsman', dodge=False, palette='rainbow', ax=ax)
ax.set_title('HAR SEASON KA ORANGE CAP WINNER', fontsize=36, color='orange', pad=30, fontweight='bold')
ax.set_ylabel('Runs', fontsize=20, color='white')
ax.set_xlabel('Season', fontsize=20, color='white')
ax.legend(title='Orange Cap Winner', title_fontsize=16, fontsize=14, loc='upper left')

for i, row in orange_cap.iterrows():
    ax.text(row['season']-2008, row['batsman_runs']+20, f"{row['batsman']}\n{row['batsman_runs']}", 
            ha='center', fontsize=12, fontweight='bold', color='white')

plt.tight_layout()
plt.savefig('DAY7_ORANGE_CAP_RACE.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.show()