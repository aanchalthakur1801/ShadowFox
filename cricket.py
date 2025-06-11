import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ipl_2025_fielding_data.xlsx")

df.columns = df.columns.str.strip()

weights = {
    "Clean Pick": 1,
    "Good Throw": 2,
    "Catch": 5,
    "Drop Catch": -4,
    "Stumping": 5,
    "Run Out": 6,
    "Missed Run Out": -3,
    "Direct Hit": 4
}

players = df["Player Name"].unique()
performance_scores = {}

for player in players:
    pdata = df[df["Player Name"] == player]
    ps = 0
    ps += (pdata["Pick"] == "Clean Pick").sum() * weights["Clean Pick"]
    ps += (pdata["Pick"] == "Good Throw").sum() * weights["Good Throw"]
    ps += (pdata["Pick"] == "Catch").sum() * weights["Catch"]
    ps += (pdata["Pick"] == "Drop Catch").sum() * weights["Drop Catch"]
    ps += (pdata["Throw"] == "Stumping").sum() * weights["Stumping"]
    ps += (pdata["Throw"] == "Run Out").sum() * weights["Run Out"]
    ps += (pdata["Throw"] == "Missed Run Out").sum() * weights["Missed Run Out"]
    ps += pdata["Runs"].sum()
    performance_scores[player] = ps

for player, score in performance_scores.items():
    print(f"{player}: Performance Score = {score}")

names = list(performance_scores.keys())
scores = list(performance_scores.values())

plt.bar(names, scores, color='skyblue')
plt.xlabel('Player')
plt.ylabel('Performance Score')
plt.title('Fielding Performance (IPL Final 2025)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
