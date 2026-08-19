import pandas as pd

df = pd.read_csv("youtube_tech_channels_20251120_133753.csv")

print(df.columns.tolist())

print(df["subscribers"].sum())


print("Total subscribers:", df["subscribers"].sum())

print("Average subscribers:", df["subscribers"].mean())
print("Maximum subscribers:", df["subscribers"].max())
print("Minimum subscribers:", df["subscribers"].min())
print("Median subscribers:", df["subscribers"].median())

# sum()     → total
# mean()    → average
# max()     → highest
# min()     → lowest
# median()  → middle value


print(df["subscribers"].std())