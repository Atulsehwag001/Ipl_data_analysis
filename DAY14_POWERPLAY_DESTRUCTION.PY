# 14_DAY14_POWERPLAY_DESTRUCTION.py
import pandas as pd
import matplotlib.pyplot as plt

# Load data
deliveries = pd.read_csv("deliveries.csv")

# Powerplay = Overs 1-6
powerplay = deliveries[deliveries['over'] <= 6]

# Total runs by batting team in powerplay
pp_runs = powerplay.groupby('batting_team')['total_runs'].sum().nlargest(10)

# PLOT
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(20, 12))

# Bars
bars = ax.bar(pp_runs.index, pp_runs.values, color='#00CED1', edgecolor='white', linewidth=1.5)

# Title & Labels
ax.set_title('POWERPLAY DESTRUCTION (Overs 1-6)', 
             fontsize=38, color='#00CED1', pad=30, fontweight='bold')
ax.set_ylabel('Total Runs', fontsize=20, color='white')
ax.set_xlabel('Teams', fontsize=20, color='white')

# Add value on top of each bar
for i, (team, runs) in enumerate(pp_runs.items()):
    ax.text(i, runs + 80, f"{runs:,}", ha='center', color='yellow', 
            fontweight='bold', fontsize=14)

# Rotate team names
plt.xticks(rotation=45, ha='right', color='white')

# Grid for better look
ax.grid(True, axis='y', color='gray', linestyle='--', alpha=0.3)

# Tight layout
plt.tight_layout()

# Save PNG
plt.savefig('DAY14_POWERPLAY_DESTRUCTION.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.close()  # Important: close figure to free memory