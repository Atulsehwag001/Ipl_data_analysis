# DAY 25/30 – MOST DUCKS IN IPL HISTORY
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')
matches    = pd.read_csv('matches.csv')

# Duck = batsman out on 0 (player_dismissed hai aur runs 0)
ducks = deliveries[(deliveries['batsman_runs'] == 0) & 
                  (deliveries['player_dismissed'].notna()) &
                  (deliveries['dismissal_kind'] != 'run out')]   # run out ko duck nahi maante

# Count ducks per player
duck_kings = ducks.groupby('batsman').size().nlargest(12)

# Top 12 (kyunki 10 se zyada log 15+ ducks maare hain)
top12 = duck_kings.reset_index(name='ducks')
top12['label'] = top12['batsman'] + ' → ' + top12['ducks'].astype(str)

print("Most Ducks in IPL History:")
print(top12[['label']])

# Killer Visual – bilkul Day 20 jaisa dark + red fire style
plt.figure(figsize=(12, 9))
bars = plt.barh(top12['label'][::-1], top12['ducks'][::-1], 
                color='#FF0033', height=0.65)

plt.title('DAY 25/30 CHALLENGE COMPLETE!\nIPL Mein Sabse Zyada Duck Kisne Khaye?',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.4, bar.get_y() + bar.get_height()/2,
             f'{int(width)}', ha='left', va='center', 
             fontsize=36, fontweight='bold', color='white')

plt.xlabel('Number of Ducks', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY25_DUCK_KINGS.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY25_DUCK_KINGS.png")
