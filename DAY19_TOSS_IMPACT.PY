# DAY 19/30 – TOSS IMPACT ON WIN %
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

# Tere exact file names
deliveries = pd.read_csv('deliveries.csv')   # ← ye hai tera ball-by-ball
matches = pd.read_csv('matches.csv')         # ← ye hai tera matches file

# Toss winner vs Match winner
toss_win_and_match_win = matches[matches['toss_winner'] == matches['winner']]
toss_lose_but_match_win = matches[matches['toss_winner'] != matches['winner']]

total_matches = len(matches)
toss_win_percentage = round((len(toss_win_and_match_win) / total_matches) * 100, 1)
toss_lose_percentage = round((len(toss_lose_but_match_win) / total_matches) * 100, 1)

print(f"Total Matches: {total_matches}")
print(f"Toss jeetne ke baad match jeetne ka % → {toss_win_percentage}%")
print(f"Toss haarne ke baad bhi match jeetne ka % → {toss_lose_percentage}%")

# Killer PNG
plt.figure(figsize=(12, 9))
bars = plt.bar(['Toss Jeeta\nPhir Match Jeeta', 'Toss Haara\nPhir bhi Jeeta'],
               [toss_win_percentage, toss_lose_percentage],
               color=['#00FF7F', '#FF4500'], width=0.55)

plt.ylim(0, 100)
plt.title('DAY 19/30 CHALLENGE COMPLETE!\nToss Ka Asar Match Pe?', 
          fontsize=22, fontweight='bold', color='white', pad=40)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{height}%', ha='center', va='bottom', fontsize=40, fontweight='bold', color='white')

plt.ylabel('Win %', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY19_TOSS_IMPACT.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY19_TOSS_IMPACT.png")
plt.show()