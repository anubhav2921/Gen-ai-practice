import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Student Depression Dataset.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Count each satisfaction level
satisfaction_counts = (
    df["Study Satisfaction"]
    .dropna()
    .value_counts()
    .sort_index()
)

print(satisfaction_counts)
print(satisfaction_counts.values)

# Bar plot
bars = plt.bar(
    satisfaction_counts.index,
    satisfaction_counts.values
)

# Green shades
colors = plt.cm.Greens(
    [0.4, 0.55, 0.7, 0.85, 1.0][:len(bars)]
)

for bar, color in zip(bars, colors):
    bar.set_color(color)

# Labels
plt.xlabel("Study Satisfaction")
plt.ylabel("Number of Students")
plt.title("Students by Study Satisfaction")

plt.show()