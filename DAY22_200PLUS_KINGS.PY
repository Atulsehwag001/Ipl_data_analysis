# DAY 22/30 – TEAMS WITH MOST 200+ SCORES IN IPL
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')
matches    = pd.read_csv('matches.csv')

# Total runs per innings
deliveries['total_runs'] = deliveries[['batsman_runs','wide_runs','bye_runs',
                                      'legbye_runs','penalty_runs']].sum(axis=1)

inning_total = deliveries.groupby(['match_id','inning'])['total_runs'].sum().unstack(fill_value=0)
inning_total = inning_total.iloc[:, :2]
inning_total.columns = ['team1_score', 'team2_score']
inning_total = inning_total.reset_index()

# Merge with matches (tere CSV mein "id" hai match_id ki jagah)
df = inning_total.merge(matches[['id','team1','team2']], 
                       left_on='match_id', right_on='id', how='inner')

# 200+ scores by batting team
team1_200 = df[df['team1_score'] >= 200]['team1'].value_counts()
team2_200 = df[df['team2_score'] >= 200]['team2'].value_counts()
total_200 = (team1_200 + team2_200).fillna(0).astype(int)
total_200 = total_200.sort_values(ascending=False)

print("Teams with Most 200+ Scores:")
print(total_200)

# Killer Visual – bilkul Day 20 jaisa style
plt.figure(figsize=(12, 9))
bars = plt.barh(total_200.index[::-1], total_200.values[::-1], 
                color='#FF2D55', height=0.6)

plt.title('DAY 22/30 CHALLENGE COMPLETE!\nKaun Si Team Sabse Zyada 200+ Maarti Hai?',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    width = int(bar.get_width())
    plt.text(width + 1, bar.get_y() + bar.get_height()/2,
             f'{width}', ha='left', va='center', fontsize=36, fontweight='bold', color='white')

plt.xlabel('Number of 200+ Scores', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY22_200PLUS_KINGS.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY22_200PLUS_KINGS.png")
plt.show()