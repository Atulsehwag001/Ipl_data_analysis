# DAY9_CENTURY_KINGS.py
import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv("deliveries.csv")

# Batsman runs per match
batsman_runs = deliveries.groupby(['match_id','batsman'])['batsman_runs'].sum().reset_index()
centuries = batsman_runs[batsman_runs['batsman_runs'] >= 100]
double_centuries = centuries[centuries['batsman_runs'] >= 200]

top_centurions = centuries['batsman'].value_counts().head(8)

# PLOT
plt.style.use('dark_background')
fig = plt.figure(figsize=(24,18))
gs = fig.add_gridspec(2,2,hspace=0.3,wspace=0.3)

ax1 = fig.add_subplot(gs[0,0])
bars = ax1.barh(top_centurions.index, top_centurions.values, color='#FFD700')
ax1.set_title('IPL MEIN SABSE ZYADA CENTURIES', fontsize=26, color='gold', pad=20, fontweight='bold')
ax1.invert_yaxis()

ax2 = fig.add_subplot(gs[0,1])
ax2.pie([len(centuries), len(double_centuries)], labels=['100+', '200+'], autopct='%1.1f%%',
        colors=['#00FF00','#FF0000'], textprops={'fontsize':20, 'fontweight':'bold', 'color':'white'})
ax2.set_title('CENTURY vs DOUBLE CENTURY', fontsize=26, color='white', pad=20)

fig.suptitle('DAY 9/30 - CENTURY KINGS', fontsize=40, color='#FFFFFF', fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig('DAY9_CENTURY_KINGS.png', dpi=600, bbox_inches='tight', facecolor='black')
plt.show()