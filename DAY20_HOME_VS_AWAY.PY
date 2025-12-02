# DAY 20/30 – HOME vs AWAY WIN PERCENTAGE
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

# Tere exact file names
matches = pd.read_csv('matches.csv')

# Home team = Team1 (batting first or second, but home ground)
home_wins = matches[matches['winner'] == matches['team1']]
away_wins = matches[matches['winner'] == matches['team2']]

total = len(matches)
home_win_pct = round((len(home_wins) / total) * 100, 1)
away_win_pct = round((len(away_wins) / total) * 100, 1)

print(f"Total Matches: {total}")
print(f"Home Team Win % → {home_win_pct}%")
print(f"Away Team Win % → {away_win_pct}%")

# Killer Visual
plt.figure(figsize=(12, 9))
bars = plt.bar(['HOME ADVANTAGE', 'AWAY TEAM'], 
               [home_win_pct, away_win_pct], 
               color=['#32CD32', '#FF4500'], width=0.6)

plt.ylim(0, 100)
plt.title('DAY 20/30 CHALLENGE COMPLETE!\nGhar Ki Pitch Pe Jeet Kitni Asaan?', 
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 3,
             f'{height}%', ha='center', va='bottom', fontsize=45, fontweight='bold', color='white')

plt.ylabel('Win Percentage %', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY20_HOME_vs_AWAY.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY20_HOME_vs_AWAY.png")
plt.show()