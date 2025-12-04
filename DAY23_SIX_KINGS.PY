# DAY 23/30 – MOST SIXES IN A SINGLE IPL SEASON
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')
matches    = pd.read_csv('matches.csv')

# Sixes count (batsman_runs == 6)
sixes = deliveries[deliveries['batsman_runs'] == 6]

# Add season from matches (tere CSV mein "id" hai)
sixes = sixes.merge(matches[['id', 'season']], left_on='match_id', right_on='id', how='left')

# Player + Season wise sixes
player_season_6s = sixes.groupby(['batsman', 'season']).size().reset_index(name='sixes')
top10 = player_season_6s.nlargest(10, 'sixes')

# Label banao → Player (Season)
top10['label'] = top10['batsman'] + ' (' + top10['season'].astype(str) + ')'

print("Most Sixes in a Single IPL Season:")
print(top10[['label', 'sixes']])

# Killer Visual – bilkul Day 20 jaisa style
plt.figure(figsize=(12, 9))
bars = plt.barh(top10['label'][::-1], top10['sixes'][::-1], color='#FF4500', height=0.6)

plt.title('DAY 23/30 CHALLENGE COMPLETE!\nEk Season Mein Sabse Zyada Chhakke Kisne Maare?',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    width = int(bar.get_width())
    plt.text(width + 1, bar.get_y() + bar.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=36, fontweight='bold', color='white')

plt.xlabel('Number of Sixes in a Season', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY23_SIX_KING_SEASON.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY23_SIX_KING_SEASON.png")
plt.show()