# DAY 18/30 – POWERPLAY vs DEATH OVERS COMPARISON
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('deliveries.csv')

# Total runs per ball
df['total_runs'] = df['batsman_runs'] + df['wide_runs'].fillna(0) + df['bye_runs'].fillna(0) + df['legbye_runs'].fillna(0) + df['penalty_runs'].fillna(0)

# Phase define
df['phase'] = df['over'].apply(lambda x: 'Powerplay (1-6)' if x <= 6 else 'Death (16-20)' if x >= 16 else 'Other')

# Sirf Powerplay aur Death
data = df[df['phase'] != 'Other']

# Runs aur Wickets
runs = data.groupby('phase')['total_runs'].sum()
wickets = data[data['player_dismissed'].notna()].groupby('phase').size()

print("Powerplay (1-6)  → Runs:", int(runs['Powerplay (1-6)']), " | Wickets:", wickets.get('Powerplay (1-6)', 0))
print("Death (16-20)    → Runs:", int(runs['Death (16-20)']), " | Wickets:", wickets.get('Death (16-20)', 0))

# Plot – tere wale killer style mein
plt.figure(figsize=(14, 8))

plt.subplot(1, 2, 1)
sns.barplot(x=['Powerplay', 'Death'], y=[runs['Powerplay (1-6)'], runs['Death (16-20)']], palette=['#00E0FF', '#FF3300'])
plt.title('Total Runs', fontsize=18, fontweight='bold', color='white')
plt.ylabel('')
plt.tick_params(colors='white')

plt.subplot(1, 2, 2)
sns.barplot(x=['Powerplay', 'Death'], y=[wickets.get('Powerplay (1-6)', 0), wickets.get('Death (16-20)', 0)], palette=['#FFD700', '#9C27B0'])
plt.title('Total Wickets', fontsize=18, fontweight='bold', color='white')
plt.ylabel('')
plt.tick_params(colors='white')

plt.suptitle('DAY 18/30 CHALLENGE COMPLETE!\nPowerplay vs Death Overs Battle', fontsize=22, fontweight='bold', color='white', y=1.02)
plt.gcf().set_facecolor('#0E1117')
plt.tight_layout()
plt.savefig('DAY18_POWERPLAY_vs_DEATH.png', dpi=300, facecolor='#0E1117', bbox_inches='tight')
print("PNG saved: DAY18_POWERPLAY_vs_DEATH.png")
plt.show()