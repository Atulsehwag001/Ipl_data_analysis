# IPL Top 10 Bowlers by Wickets
import pandas as pd
import matplotlib.pyplot as plt

# 1. डेटा लोड करो
df = pd.read_csv("deliveries.csv")

# 2. विकेट्स गिनो (जब dismissal_kind में 'bowled', 'caught', 'lbw' हो)
wickets = df[df['dismissal_kind'].isin(['bowled', 'caught', 'lbw', 'stumped', 'caught and bowled'])]
bowler_wickets = wickets.groupby('bowler')['dismissal_kind'].count().sort_values(ascending=False).head(10)

# 3. Chart बनाओ
plt.figure(figsize=(12, 7))
bowler_wickets.plot(kind='bar', color='purple')
plt.title("IPL Top 10 Bowlers by Wickets", fontsize=16)
plt.xlabel("Bowler", fontsize=12)
plt.ylabel("Total Wickets", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()
plt.savefig("ipl_top_bowlers.png", dpi=300, bbox_inches='tight')
plt.show()

print("Top 10 Bowlers Chart बन गया!")