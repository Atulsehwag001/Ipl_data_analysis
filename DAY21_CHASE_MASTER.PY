# DAY 21/30 – HIGHEST SUCCESSFUL RUN CHASES IN IPL
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv('deliveries.csv')
matches    = pd.read_csv('matches.csv')

# Total runs per ball
deliveries['total_runs'] = deliveries[['batsman_runs','wide_runs','bye_runs',
                                      'legbye_runs','penalty_runs']].sum(axis=1)

# Inning-wise score
inning = deliveries.groupby(['match_id','inning'])['total_runs'].sum().unstack(fill_value=0)
inning = inning.iloc[:, :2]                  # sirf inning 1 & 2
inning.columns = ['target','chased']
inning = inning.reset_index()

# YAHAN GALTI THI → tere CSV mein "id" hai, "match_id" nahi!
final = inning.merge(matches[['id','team1','team2','winner']], 
                     left_on='match_id', right_on='id', how='inner')

# Successful chase
chases = final[(final['winner'] == final['team2']) & (final['chased'] >= final['target'])]
top10 = chases.nlargest(10, 'target').copy()
top10['label'] = top10['team2'] + ' → ' + top10['target'].astype(int).astype(str)

print(top10[['label','target','chased']])

# Killer PNG – bilkul Day 20 jaisa
plt.figure(figsize=(12,9))
bars = plt.barh(top10['label'][::-1], top10['target'][::-1], color='#00FF7F', height=0.6)

plt.title('DAY 21/30 CHALLENGE COMPLETE!\nHighest Successful Run Chases in IPL',
          fontsize=22, fontweight='bold', color='white', pad=50)

for bar in bars:
    w = int(bar.get_width())
    plt.text(w + 3, bar.get_y() + bar.get_height()/2,
             f'{w}', ha='left', va='center', fontsize=36, fontweight='bold', color='white')

plt.xlabel('Target Successfully Chased', color='white', fontsize=14)
plt.tick_params(colors='white')
plt.gca().set_facecolor('#0F1117')
plt.gcf().set_facecolor('#0F1117')
plt.tight_layout()

plt.savefig('DAY21_CHASE_MASTERS.png', dpi=300, facecolor='#0F1117', bbox_inches='tight')
print("PNG saved: DAY21_CHASE_MASTERS.png")
plt.show()