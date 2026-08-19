import pandas as pd

df = pd.read_csv("youtube_tech_channels_20251120_133753.csv")

print("Average:", df["subscribers"].mean())
print("\n------>std() — Standard deviation<--------\n")
print(df[
    ["subscribers", "total_views", "total_videos"]
].std())
print("\n------>var() — Variance<--------\n")

print(df[
    ["subscribers", "total_views", "total_videos"]
].var())