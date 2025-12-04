# DAY 29/30 – MOST PLAYER OF THE MATCH AWARDS IN IPL
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv('matches.csv')

# Tere CSV mein column name "player_of_match" hai
pom = matches['player_of_match'].value_counts().head(12)

print("Most Player of the Match Awards:")
print(pom)

# Killer Visual – Golden trophy feel
plt.figure(figsize=(12, 9))
bars = plt.barh(pom.index[::-1], pom.values[::-1], 
                color='#FFD700', height=0.65)   # Pure Gold color

plt.title('DAY 29/30 CHALLENGE COMPLETE!\nIPL Ke Asli Match-Winner Kaun?',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    width = int(bar.get_width())
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2,
             f'{width}', ha='left', va='center', 
             fontsize=40, fontweight='bold', color='white')

plt.xlabel('Player of the Match Awards', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY29_POM_KINGS.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY29_POM_KINGS.png")
