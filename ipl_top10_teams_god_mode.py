# IPL TOP 10 TEAMS – ULTIMATE FINAL (LEFT SIDE TOTAL RUNS BHI DIKHEGA)
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

df = pd.read_csv("deliveries.csv")
top_teams = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False).head(10)

plt.style.use('default')
fig, ax = plt.subplots(figsize=(18, 11))

colors = ['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4','#FECA57','#DDA0DD','#98D8C8','#F7DC6F','#BB8FCE','#85C1E2']
bars = ax.bar(top_teams.index, top_teams.values, color=colors, edgecolor='black', linewidth=2.5, alpha=0.98)

# Background
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# Grid
ax.grid(True, axis='y', alpha=0.4, linestyle='-', linewidth=1.2, color='#95a5a6')

# Title
ax.set_title("IPL All-Time: Top 10 Teams by Total Runs Scored", 
             fontsize=30, fontweight='bold', pad=50, color='#2c3e50')

# X-axis
ax.set_xlabel("Team", fontsize=18, fontweight='bold', labelpad=20, color='#2c3e50')
plt.xticks(rotation=38, ha='right', fontsize=14, fontweight='bold')

# Y-AXIS – TOTAL RUNS LEFT SIDE MEIN BHI DIKHEGA, FULL BOLD
ax.set_ylabel("Total Runs", fontsize=22, fontweight='bold', labelpad=30, color='#2c3e50')
ax.tick_params(axis='y', which='major', labelsize=16, width=3, length=10, color='#2c3e50')
ax.yaxis.set_tick_params(pad=15)

# Value labels on top
for i, (team, runs) in enumerate(top_teams.items()):
    ax.text(i, runs + 500, f'{runs:,}', 
            ha='center', va='bottom', fontsize=16, fontweight='bold', color='#2c3e50',
            path_effects=[path_effects.withStroke(linewidth=8, foreground='white')])

# Footer
plt.figtext(0.5, 0.02, "Made by AtulSehwag001 | Day 3/30 | #30Days2Offers | GitHub: AtulSehwag001", 
            ha='center', fontsize=14, style='italic', color='#7f8c8d')

# Final Pro Touch
plt.tight_layout(rect=[0, 0.06, 1, 0.93])
plt.savefig("IPL_TOP10_TEAMS_GOD_MODE.png", dpi=600, bbox_inches='tight', facecolor='white')
plt.show()

print("BHAI – AB YE CHART DEKHTE HI HR KO DIL SE 'SELECTED' NIKAL AAYEGA!")