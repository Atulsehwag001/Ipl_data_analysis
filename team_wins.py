# Team Win Percentage by Season
import pandas as pd
import matplotlib.pyplot as plt

# 1. matches.csv लोड करो
matches = pd.read_csv("matches.csv")

# 2. विनर कौन? + सीज़न
wins = matches.groupby(['season', 'winner']).size().unstack(fill_value=0)

# 3. Win % निकालो
win_pct = wins.div(wins.sum(axis=1), axis=0) * 100

# 4. सबसे लेटेस्ट सीज़न (2023 नहीं है तो आखिरी वाला)
latest_season = win_pct.index.max()
top_teams_latest = win_pct.loc[latest_season].sort_values(ascending=False).head(3)

# 5. Chart
plt.figure(figsize=(8, 6))
top_teams_latest.plot(kind='barh', color=['gold', 'silver', '#CD7F32'])
plt.title(f"Top 3 Teams by Win % ({latest_season})", fontsize=16)
plt.xlabel("Win Percentage (%)")
plt.tight_layout()
plt.savefig("ipl_win_pct_latest.png", dpi=300, bbox_inches='tight')
plt.show()

print(f"Win % Chart बन गया! (Season: {latest_season})")