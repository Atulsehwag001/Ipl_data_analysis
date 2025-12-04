# DAY 26/30 – MOST WICKETS IN IPL HISTORY (ALL TIME)
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')
matches    = pd.read_csv('matches.csv')

# Wicket lena = player_dismissed not null aur dismissal_kind wicket wala ho
wickets = deliveries[
    (deliveries['player_dismissed'].notna()) &
    (deliveries['dismissal_kind'].isin(['caught', 'bowled', 'lbw', 
                                        'stumped', 'caught and bowled', 
                                        'hit wicket']))
]

# Bowler wise wickets
top_bowlers = wickets['bowler'].value_counts().head(12)

print("Most Wickets in IPL History:")
print(top_bowlers)

# Killer Visual – Purple Cap wala feel
plt.figure(figsize=(12, 9))
bars = plt.barh(top_bowlers.index[::-1], top_bowlers.values[::-1], 
                color='#9B59B6', height=0.65)   # Purple color

plt.title('DAY 26/30 CHALLENGE COMPLETE!\nIPL Ke Sabse Bade Wicket-Taker Kaun?',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    width = int(bar.get_width())
    plt.text(width + 3, bar.get_y() + bar.get_height()/2,
             f'{width}', ha='left', va='center', 
             fontsize=38, fontweight='bold', color='white')

plt.xlabel('Total Wickets', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY26_PURPLE_CAP_KINGS.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY26_PURPLE_CAP_KINGS.png")
