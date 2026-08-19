import pandas as pd

# What is Standard Deviation?
# Standard deviation tells us how spread out the values are from the average (mean)
df = pd.read_csv("youtube_tech_channels_20251120_133753.csv")

print("Average:", df["subscribers"].mean())
print("Standard deviation:", df["subscribers"].std())

# print(df["column_name"].std())

print(df[
    ["subscribers", "total_views", "total_videos"]
].std())