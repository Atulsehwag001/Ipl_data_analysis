# DAY 17/30 – ROHIT SHARMA vs CHENNAI SUPER KINGS
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

# Tere exact file name
df = pd.read_csv('deliveries.csv')

# Rohit vs CSK filter
rohit_csk = df[(df['batsman'] == 'RG Sharma') & 
               (df['bowling_team'] == 'Chennai Super Kings')]

# Stats (tere CSV ke column names ke hisaab se)
runs = rohit_csk['batsman_runs'].sum()
balls = len(rohit_csk)
fours = len(rohit_csk[rohit_csk['batsman_runs'] == 4])
sixes = len(rohit_csk[rohit_csk['batsman_runs'] == 6])

# Dismissals count (tere CSV mein 'player_dismissed' column hai)
dismissed = rohit_csk['player_dismissed'].notna().sum()

sr = round((runs / balls) * 100, 2) if balls > 0 else 0
avg = round(runs / dismissed, 2) if dismissed > 0 else runs

print(f"Rohit Sharma vs CSK → {runs} runs | {balls} balls | SR {sr} | Avg {avg} | Out {dismissed} times")

# Killer Dashboard
plt.figure(figsize=(12, 9))
plt.text(0.5, 0.78, 'ROHIT SHARMA', fontsize=44, fontweight='bold', ha='center', color='#FFB81C')
plt.text(0.5, 0.68, 'vs CSK', fontsize=40, ha='center', color='yellow')
plt.text(0.5, 0.56, f'{runs} RUNS', fontsize=58, fontweight='bold', ha='center', color='white')
plt.text(0.5, 0.46, f'SR: {sr}  |  4s: {fours}  |  6s: {sixes}', fontsize=26, ha='center', color='white')
plt.text(0.5, 0.38, f'Avg: {avg}  |  Balls: {balls}  |  Out: {dismissed}x', fontsize=22, ha='center', color='#D3D3D3')
plt.title('DAY 17/30 CHALLENGE COMPLETE!', fontsize=20, color='white', pad=50)
plt.axis('off')
plt.gca().set_facecolor('#001E3C')
plt.tight_layout()
plt.savefig('DAY17_ROHIT_vs_CSK.png', dpi=300, facecolor='#001E3C', bbox_inches='tight')
print("PNG saved: DAY17_ROHIT_vs_CSK.png")
plt.show()