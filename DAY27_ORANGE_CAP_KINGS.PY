# DAY 27/30 – MOST RUNS IN IPL HISTORY (ALL TIME)
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')

# Total runs by each batsman (including wides/no-balls pe runs bhi count hote hain batsman ke)
runs = deliveries.groupby('batsman')['batsman_runs'].sum().nlargest(12)

print("Most Runs in IPL History:")
print(runs)

# Killer Visual – Orange Cap wala fire look
plt.figure(figsize=(12, 9))
bars = plt.barh(runs.index[::-1], runs.values[::-1], 
                color='#FF6B00', height=0.65)   # Pure Orange

plt.title('DAY 27/30 CHALLENGE COMPLETE!\nIPL Ke Run-Machine Kaun Hai?',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    width = int(bar.get_width())
    plt.text(width + 80, bar.get_y() + bar.get_height()/2,
             f'{width}', ha='left', va='center', 
             fontsize=38, fontweight='bold', color='white')

plt.xlabel('Total Runs Scored', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY27_ORANGE_CAP_KINGS.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY27_ORANGE_CAP_KINGS.png")
