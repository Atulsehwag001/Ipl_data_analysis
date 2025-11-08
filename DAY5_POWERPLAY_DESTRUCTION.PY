# DAY5_POWERPLAY_DESTRUCTION_MODE.py
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: DATA LOAD
deliveries = pd.read_csv("deliveries.csv")

# STEP 2: POWERPLAY = 1-6 OVERS
powerplay = deliveries[deliveries['over'] <= 6]

print(f"Total Powerplay balls: {len(powerplay)}")
print("Powerplay matches:", powerplay['match_id'].nunique())

# 1. TEAM WISE RUNS IN POWERPLAY
team_runs = powerplay.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)

# 2. SIXES IN POWERPLAY
sixes = powerplay[powerplay['batsman_runs'] == 6]
sixes_king_team = sixes['batting_team'].value_counts()
sixes_king_player = sixes['batsman'].value_counts().head(5)

# 3. STRIKE RATE IN POWERPLAY
balls_faced = powerplay.groupby(['batting_team', 'batsman']).size()
runs_scored = powerplay.groupby(['batting_team', 'batsman'])['batsman_runs'].sum()
sr = (runs_scored / balls_faced * 100).round(1)
top_sr = sr[sr > 150].sort_values(ascending=False).head(10)

# 4. BEST POWERPLAY BOWLERS (ECONOMY)
bowler_runs = powerplay.groupby('bowler')['total_runs'].sum()
bowler_balls = powerplay.groupby('bowler').size()
economy = (bowler_runs / (bowler_balls / 6)).round(2)
best_economy = economy[economy < 7].sort_values().head(8)

# NETFLIX LEVEL 4 CHARTS
plt.style.use('dark_background')
fig = plt.figure(figsize=(24, 18))
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

# CHART 1 - TEAM RUNS
ax1 = fig.add_subplot(gs[0, 0])
bars1 = ax1.barh(team_runs.head(10).index, team_runs.head(10), color='#00FFFF', height=0.7)
ax1.set_title('POWERPLAY MEIN SABSE ZYADA RUNS', fontsize=24, color='yellow', pad=20, fontweight='bold')
ax1.set_xlabel('Total Runs', fontsize=14, color='white')
ax1.invert_yaxis()
for bar in bars1:
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
             str(int(bar.get_width())), va='center', color='white', fontweight='bold', fontsize=12)

# CHART 2 - SIXES KING
ax2 = fig.add_subplot(gs[0, 1])
bars2 = ax2.bar(sixes_king_team.head(8).index, sixes_king_team.head(8), color='#FF00FF')
ax2.set_title('POWERPLAY MEIN SIXES KA BADSHAAH', fontsize=24, color='yellow', pad=20, fontweight='bold')
ax2.set_ylabel('Sixes', fontsize=14, color='white')
plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
for bar in bars2:
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
             str(int(bar.get_height())), ha='center', color='white', fontweight='bold')

# CHART 3 - STRIKE RATE KINGS
ax3 = fig.add_subplot(gs[1, 0])
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD700']
ax3.pie(sixes_king_player.values, labels=sixes_king_player.index, autopct='%1.1f%%', 
        colors=colors, textprops={'color':"white", 'fontsize':14, 'fontweight':'bold'})
ax3.set_title('POWERPLAY SIXES KA PERSONAL BADSHAAH', fontsize=24, color='yellow', pad=30, fontweight='bold')

# CHART 4 - BEST ECONOMY
ax4 = fig.add_subplot(gs[1, 1])
bars4 = ax4.bar(best_economy.index, best_economy.values, color='#FFD700')
ax4.set_title('POWERPLAY MEIN SABSE KANJOOS BOWLERS', fontsize=24, color='yellow', pad=20, fontweight='bold')
ax4.set_ylabel('Economy Rate', fontsize=14, color='white')
plt.setp(ax4.get_xticklabels(), rotation=45, ha='right')
for bar in bars4:
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 0.3, 
             str(bar.get_height()), ha='center', color='black', fontweight='bold', fontsize=12)

# MAIN TITLE
fig.suptitle('DAY 5/30 - POWERPLAY DESTRUCTION MODE', 
             fontsize=40, color='#FF0000', fontweight='bold', y=0.98)

plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.savefig('DAY5_POWERPLAY_DESTRUCTION.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.show()
