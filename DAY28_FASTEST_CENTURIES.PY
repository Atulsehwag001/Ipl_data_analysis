# DAY 28/30 – FASTEST CENTURIES IN IPL HISTORY
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')

# Batsman-wise runs per match
batsman_match_runs = deliveries.groupby(['match_id', 'batsman'])['batsman_runs'].sum()
batsman_match_balls = deliveries.groupby(['match_id', 'batsman']).size()

# Find centuries (100+ runs in a match)
centuries = batsman_match_runs[batsman_match_runs >= 100].reset_index()
centuries = centuries.merge(batsman_match_balls.reset_index(name='balls'), 
                           on=['match_id', 'batsman'])

# Top 10 fastest centuries
fastest = centuries.nsmallest(10, 'balls').copy()
fastest['label'] = fastest['batsman'] + ' → ' + fastest['balls'].astype(str) + ' balls'

print("Fastest IPL Centuries:")
print(fastest[['label', 'batsman_runs', 'balls']])

# Killer Visual – Lightning style
plt.figure(figsize=(12, 9))
bars = plt.barh(fastest['label'][::-1], fastest['balls'][::-1], 
                color='#00FFFF', height=0.65)   # Cyan lightning color

plt.title('DAY 28/30 CHALLENGE COMPLETE!\nIPL Ki Sabse Tez Centuries!',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    width = int(bar.get_width())
    plt.text(width + 1, bar.get_y() + bar.get_height()/2,
             f'{width} balls', ha='left', va='center', 
             fontsize=36, fontweight='bold', color='white')

plt.xlabel('Balls Faced to Reach 100', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY28_FASTEST_CENTURIES.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY28_FASTEST_CENTURIES.png")
