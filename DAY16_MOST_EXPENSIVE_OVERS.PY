import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ← tera exact file name
df = pd.read_csv("deliveries.csv")

# total_runs bana lete hain (tere CSV ke columns ke hisaab se)
df['total_runs'] = df['batsman_runs'] + df['wide_runs'].fillna(0) + df['bye_runs'].fillna(0) + df['legbye_runs'].fillna(0) + df['penalty_runs'].fillna(0)

# 20+ runs wale overs
expensive = df.groupby(['match_id', 'over'])['total_runs'].sum().reset_index()
expensive = expensive[expensive['total_runs'] >= 20]
top10 = expensive.sort_values('total_runs', ascending=False).head(10)

plt.figure(figsize=(12,8))
sns.barplot(data=top10, 
            x='total_runs', 
            y=top10['match_id'].astype(str) + '.' + top10['over'].astype(str), 
            palette='Reds_r')

plt.title('Day 16/30 Challenge Complete!\nMost Expensive Overs in IPL History (20+ Runs in One Over!)', 
          fontsize=18, fontweight='bold', color='white', pad=20)
plt.xlabel('Runs', color='white')
plt.ylabel('Match.Over', color='white')
plt.tick_params(colors='white')
plt.gca().set_facecolor('black')
plt.gcf().set_facecolor('black')
plt.tight_layout()
plt.savefig('Day16_Most_Expensive_Overs.png', dpi=300, bbox_inches='tight')
plt.show()