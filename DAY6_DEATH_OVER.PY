# DAY6_DEATH_OVER_KATIL.py
import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv("deliveries.csv")
death = deliveries[deliveries['over'] >= 16]

# 1. MOST WICKETS IN DEATH
death_wickets = death[death['player_dismissed'].notnull()]
top_killers = death_wickets['bowler'].value_counts().head(8)

# 2. MOST EXPENSIVE BOWLERS
runs_given = death.groupby('bowler')['total_runs'].sum()
balls_bowled = death.groupby('bowler').size()
economy = (runs_given / (balls_bowled/6)).round(2)
most_expensive = economy.sort_values(ascending=False).head(8)

# 3. SIXES IN DEATH OVERS
death_sixes = death[death['batsman_runs'] == 6]
sixes_king_death = death_sixes['batsman'].value_counts().head(5)

# 4. BEST DEATH OVER PARTNERSHIPS
partnerships = death.groupby(['match_id', 'batting_team', 'over'])['total_runs'].sum()
big_partnerships = partnerships[partnerships > 25]

# PLOT
plt.style.use('dark_background')
fig = plt.figure(figsize=(24,18))
gs = fig.add_gridspec(2,2,hspace=0.3,wspace=0.3)

# CHART 1
ax1 = fig.add_subplot(gs[0,0])
ax1.barh(top_killers.index, top_killers.values, color='#FF00FF')
ax1.set_title('DEATH OVER MEIN WICKET KA BADSHAAH', fontsize=24, color='yellow', pad=20, fontweight='bold')
ax1.invert_yaxis()

# CHART 2
ax2 = fig.add_subplot(gs[0,1])
ax2.bar(most_expensive.index, most_expensive.values, color='#FF5733')
ax2.set_title('DEATH OVER MEIN SABSE MEHNGA BOWLER', fontsize=24, color='yellow', pad=20, fontweight='bold')
plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

# CHART 3
ax3 = fig.add_subplot(gs[1,0])
colors = ['#00FFFF','#FF00FF','#FFD700','#33FF57','#FF33A1']
ax3.pie(sixes_king_death.values, labels=sixes_king_death.index, autopct='%1.1f%%', colors=colors)
ax3.set_title('DEATH OVER SIXES KA RAKSHAS', fontsize=24, color='yellow', pad=20, fontweight='bold')

# CHART 4
ax4 = fig.add_subplot(gs[1,1])
ax4.bar(['20+ Run Over'], [len(big_partnerships)], color='#FFD700')
ax4.text(0, len(big_partnerships)+5, f"{len(big_partnerships)} TIMES!", fontsize=30, ha='center', color='white', fontweight='bold')
ax4.set_title('20+ RUNS IN SINGLE DEATH OVER', fontsize=24, color='yellow', pad=20, fontweight='bold')
ax4.set_ylim(0, len(big_partnerships)+50)

fig.suptitle('DAY 6/30 - DEATH OVER KATIL MODE', fontsize=40, color='#FF0000', fontweight='bold', y=0.98)
plt.tight_layout()
plt.subplots_adjust(top=0.90)
plt.savefig('DAY6_DEATH_OVER_KATIL.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.show()