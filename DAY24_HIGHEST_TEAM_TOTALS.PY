# DAY 24/30 – HIGHEST TEAM TOTALS IN IPL HISTORY
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')
matches    = pd.read_csv('matches.csv')

# Total runs per ball
deliveries['total_runs'] = deliveries[['batsman_runs','wide_runs','bye_runs',
                                      'legbye_runs','penalty_runs']].sum(axis=1)

# Inning-wise total
inning_total = deliveries.groupby(['match_id','inning'])['total_runs'].sum().unstack(fill_value=0)
inning_total = inning_total.iloc[:, :2]
inning_total.columns = ['team1_score', 'team2_score']
inning_total = inning_total.reset_index()

# Merge with matches (tere CSV mein "id" hai)
df = inning_total.merge(matches[['id','team1','team2','season']], 
                       left_on='match_id', right_on='id', how='inner')

# Team1 aur Team2 ke scores ko ek hi column mein daalo
team1 = df[['team1', 'team1_score', 'season']].rename(columns={'team1':'team','team1_score':'score'})
team2 = df[['team2', 'team2_score', 'season']].rename(columns={'team2':'team','team2_score':'score'})
all_scores = pd.concat([team1, team2], ignore_index=True)

# Top 10 highest totals
top10 = all_scores.nlargest(10, 'score').copy()
top10['label'] = top10['team'] + ' (' + top10['season'].astype(str) + ') → ' + top10['score'].astype(int).astype(str)

print("Highest Team Totals in IPL History:")
print(top10[['label']])

# Killer Visual – bilkul Day 20 jaisa style
plt.figure(figsize=(12, 9))
bars = plt.barh(top10['label'][::-1], top10['score'][::-1], color='#FFD700', height=0.6)

plt.title('DAY 24/30 CHALLENGE COMPLETE!\nIPL Ke Sabse Bade Team Totals',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    width = int(bar.get_width())
    plt.text(width + 3, bar.get_y() + bar.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=38, fontweight='bold', color='white')

plt.xlabel('Team Total Runs', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY24_HIGHEST_TEAM_TOTALS.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY24_HIGHEST_TEAM_TOTALS.png")
