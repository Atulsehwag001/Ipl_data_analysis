# DAY4_SUPER_OVER_PERFECT_ADJUSTED.py
import pandas as pd
import matplotlib.pyplot as plt

# DATA LOAD
deliveries = pd.read_csv("deliveries.csv")
matches = pd.read_csv("matches.csv")

# SUPER OVER BALLS
super_over_balls = deliveries[deliveries['is_super_over'] == 1]
super_over_match_ids = super_over_balls['match_id'].unique()
super_matches = matches[matches['id'].isin(super_over_match_ids)]

# 1. TEAM RUNS
team_runs = super_over_balls.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)

# 2. TOP BOWLERS
wickets = super_over_balls[super_over_balls['player_dismissed'].notnull()]
top_bowlers = wickets['bowler'].value_counts().head(8)

# 3. SIXES KING
sixes = super_over_balls[super_over_balls['batsman_runs'] == 6]
six_king = sixes['batsman'].value_counts().head(5)

# 4. WIN %
win_count = super_matches['winner'].value_counts()
played = pd.concat([super_matches['team1'], super_matches['team2']]).value_counts()
win_pct = (win_count / played * 100).round(1).fillna(0)
win_pct = win_pct[win_pct.index.isin(team_runs.index)].sort_values(ascending=False)

# PERFECT ADJUSTED NETFLIX CHART
plt.style.use('dark_background')
fig = plt.figure(figsize=(24, 18))
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

# CHART 1 - HORIZONTAL BAR (TOP LEFT)
ax1 = fig.add_subplot(gs[0, 0])
bars1 = ax1.barh(team_runs.head(10).index, team_runs.head(10), color='#00FFFF', height=0.7)
ax1.set_title('SUPER OVER ME SABSE ZYADA RUNS', fontsize=22, color='yellow', pad=20, fontweight='bold')
ax1.set_xlabel('Total Runs', fontsize=14, color='white')
ax1.tick_params(axis='y', labelsize=12, colors='white')
ax1.invert_yaxis()
for i, bar in enumerate(bars1):
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
             str(int(bar.get_width())), va='center', color='white', fontweight='bold')

# CHART 2 - VERTICAL BAR (TOP RIGHT)
ax2 = fig.add_subplot(gs[0, 1])
bars2 = ax2.bar(top_bowlers.index, top_bowlers.values, color='#FF00FF')
ax2.set_title('SUPER OVER WICKET MACHINE', fontsize=22, color='yellow', pad=20, fontweight='bold')
ax2.set_ylabel('Wickets', fontsize=14, color='white')
plt.setp(ax2.get_xticklabels(), rotation=45, ha='right', fontsize=11, color='white')
for bar in bars2:
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, 
             str(int(bar.get_height())), ha='center', color='white', fontweight='bold')

# CHART 3 - PIE CHART (BOTTOM LEFT)
ax3 = fig.add_subplot(gs[1, 0])
colors_pie = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFD700']
wedges, texts, autotexts = ax3.pie(six_king.values, labels=six_king.index, autopct='%1.1f%%', 
                                  colors=colors_pie, textprops={'color':"white", 'fontsize':14, 'fontweight':'bold'})
ax3.set_title('SIXES KA BAADSHAH', fontsize=22, color='yellow', pad=30, fontweight='bold')

# CHART 4 - WIN % (BOTTOM RIGHT)
ax4 = fig.add_subplot(gs[1, 1])
bars4 = ax4.bar(win_pct.head(8).index, win_pct.head(8).values, color='#FFD700')
ax4.set_title('SUPER OVER JEETNE KA %', fontsize=22, color='yellow', pad=20, fontweight='bold')
ax4.set_ylabel('Win %', fontsize=14, color='white')
plt.setp(ax4.get_xticklabels(), rotation=45, ha='right', fontsize=11, color='white')
for bar in bars4:
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, 
             f"{bar.get_height()}%", ha='center', color='white', fontweight='bold', fontsize=12)

# MAIN TITLE
fig.suptitle('DAY 4/30 - SUPER OVER KA RAJA BAN GAYA!', 
             fontsize=36, color='#FF0000', fontweight='bold', y=0.98)

# FINAL TOUCH
plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.savefig('DAY4_SUPER_OVER_PERFECT_GOD.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.show()