# DAY12_BOUNDARIES_KA_RAJA.py
import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv("deliveries.csv")

# Count 4s and 6s per batsman
fours = deliveries[deliveries['batsman_runs'] == 4].groupby('batsman').size()
sixes = deliveries[deliveries['batsman_runs'] == 6].groupby('batsman').size()
boundaries = pd.DataFrame({'fours': fours, 'sixes': sixes}).fillna(0)
boundaries['total'] = boundaries['fours'] + boundaries['sixes']
top_boundaries = boundaries.nlargest(10, 'total').sort_values('total', ascending=True)

# PLOT
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(20,14))
bars = ax.barh(top_boundaries.index, top_boundaries['total'], color='#FF4500', edgecolor='white')

# Add 4s + 6s labels
for i, (idx, row) in enumerate(top_boundaries.iterrows()):
    ax.text(row['total'] + 5, i, f"4s: {int(row['fours'])} | 6s: {int(row['sixes'])}", 
            color='yellow', fontweight='bold', va='center')

ax.set_title('IPL MEIN BOUNDARIES KA RAJA', fontsize=38, color='#FF4500', pad=30, fontweight='bold')
ax.set_xlabel('Total Boundaries (4s + 6s)', fontsize=20, color='white')

plt.tight_layout()
plt.savefig('12_DAY12_BOUNDARIES_KA_RAJA.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.close()
# plt.show()  # comment out to avoid pop-up