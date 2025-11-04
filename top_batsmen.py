# IPL Top 10 Batsmen by Runs (2008-2023)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("deliveries.csv")
batsmen_runs = df.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 7))
batsmen_runs.plot(kind='bar', color='orange')
plt.title("IPL Top 10 Batsmen by Total Runs", fontsize=16)
plt.xlabel("Player", fontsize=12)
plt.ylabel("Total Runs", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()
plt.savefig("ipl_top_batsmen.png", dpi=300, bbox_inches='tight')
plt.show()

print("Chart बन गया! PNG सेव हो गया!")