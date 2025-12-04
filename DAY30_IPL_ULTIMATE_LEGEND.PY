# DAY 30/30 – IPL KA SABSE BADA ALL-ROUND LEGEND (RUNS + WICKETS)
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')
matches    = pd.read_csv('matches.csv')

# Batsman runs
runs = deliveries.groupby('batsman')['batsman_runs'].sum()

# Bowler wickets
wickets = deliveries[deliveries['player_dismissed'].notna() &
                    deliveries['dismissal_kind'].isin(['caught','bowled','lbw',
                                                      'stumped','caught and bowled','hit wicket'])]
wickets_count = wickets['bowler'].value_counts()

# Combine runs + wickets
combined = pd.concat([runs, wickets_count], axis=1).fillna(0)
combined.columns = ['runs', 'wickets']
combined = combined[(combined['runs'] >= 2000) | (combined['wickets'] >= 70)]

# Total impact score
combined['total_impact'] = combined['runs'] + (combined['wickets'] * 30)
top10 = combined.nlargest(10, 'total_impact')

print("IPL All-Time Greatest All-Round Impact Ranking:")
print(top10[['runs','wickets','total_impact']])

# Killer Final Visual – Rainbow gradient legend look
plt.figure(figsize=(14, 10))
colors = ['#FF0000','#FF4500','#FF8C00','#FFD700','#ADFF2F',
          '#00FF00','#00CED1','#1E90FF','#9932CC','#FF1493']

bars = plt.barh(top10.index[::-1], top10['total_impact'][::-1], 
                color=colors, height=0.7)

plt.title('DAY 30/30 CHALLENGE COMPLETE!\nIPL KA SABSE BADA LEGEND KAUN?',
          fontsize=26, fontweight='bold', color='white', pad=60)

for i, bar in enumerate(bars):
    width = int(bar.get_width())
    plt.text(width + 200, bar.get_y() + bar.get_height()/2,
             f'{width:,}', ha='left', va='center', 
             fontsize=38, fontweight='bold', color='white')

plt.xlabel('Impact Score (Runs + 30×Wickets)', color='white', fontsize=16)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY30_IPL_ULTIMATE_LEGEND.png', dpi=400, facecolor='#0F1117', bbox_inches='tight')
print("FINAL PNG saved: DAY30_IPL_ULTIMATE_LEGEND.png")
