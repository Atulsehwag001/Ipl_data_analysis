# DAY 15/30 – FASTEST 50s IN IPL HISTORY
# Atul Sehwag – 30 Days 2 Offers Challenge
# GitHub: https://github.com/AtulSehwag001/Ipl_data_analysis

import pandas as pd
import matplotlib.pyplot as plt

# Load data
deliveries = pd.read_csv("deliveries.csv")
matches = pd.read_csv("matches.csv")

# Fix column names
deliveries.columns = deliveries.columns.str.strip().str.lower()
matches.columns = matches.columns.str.strip().str.lower()

# DEBUG: Print columns
print("deliveries columns:", deliveries.columns.tolist())
print("matches columns:", matches.columns.tolist())

# Merge
df = deliveries.merge(matches[['id', 'team1', 'team2', 'date']], 
                      left_on='match_id', right_on='id', how='left')

# Runs by batsman = batsman_runs
batter_runs = df.groupby(['match_id', 'batsman'])['batsman_runs'].sum().reset_index()

# Balls faced: exclude balls where wide_runs > 0
balls_faced = df[df['wide_runs'] == 0].groupby(['match_id', 'batsman']).size().reset_index()
balls_faced.rename(columns={0: 'balls_faced'}, inplace=True)

# Merge & filter 50+
fifties = batter_runs[batter_runs['batsman_runs'] >= 50].merge(balls_faced, on=['match_id', 'batsman'])

# Fastest 10
fastest_50s = fifties.sort_values('balls_faced').head(10)

# Add match info
fastest_50s = fastest_50s.merge(matches[['id', 'team1', 'team2', 'date']], 
                                left_on='match_id', right_on='id')

# Format
fastest_50s['Match'] = fastest_50s['team1'] + ' vs ' + fastest_50s['team2']
fastest_50s['Year'] = pd.to_datetime(fastest_50s['date'], errors='coerce').dt.year

# Final result
result = fastest_50s[['batsman', 'batsman_runs', 'balls_faced', 'Match', 'Year']].copy()
result.columns = ['Batter', 'Runs', 'Balls', 'Match', 'Year']
print("\nFASTEST 50s:")
print(result)

# PLOT
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(20, 12))

bars = ax.bar(result['Batter'], result['Balls'], color='#00CED1', edgecolor='white', linewidth=1.5)

ax.set_title('FASTEST 50s IN IPL HISTORY\n(Least Balls to Reach 50)', 
             fontsize=38, color='#00CED1', pad=30, fontweight='bold')
ax.set_ylabel('Balls Faced', fontsize=20, color='white')
ax.set_xlabel('Batter', fontsize=20, color='white')

for i, balls in enumerate(result['Balls']):
    ax.text(i, balls + 1, f"{balls} balls", ha='center', color='yellow', 
            fontweight='bold', fontsize=16)

plt.xticks(rotation=45, ha='right', color='white')
ax.grid(True, axis='y', color='gray', linestyle='--', alpha=0.3)
plt.tight_layout()

# Save PNG
plt.savefig('DAY15_FASTEST_50s.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.close()
print("\nPNG saved: 15_DAY15_FASTEST_50s.png")