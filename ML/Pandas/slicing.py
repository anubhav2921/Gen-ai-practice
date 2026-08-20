import pandas as pd

df = pd.read_csv("youtube_tech_channels_20251120_133753.csv")
print(df.loc[0:4, ["channel_name", "subscribers"]])

print(df[[
    "channel_name",
    "subscribers",
    "total_views"
]])

print(df.iloc[
    [0, 3, 7],
    [1, 3, 4]
])


df = pd.read_csv("youtube_tech_channels_20251120_133753.csv")

print(df.index)

print(df["channel_id"].is_unique)


print(df.head())       # first 5
print("---------><---------------------------")
print(df.tail())       # last 5
print("---------><---------------------------")

print(df)              # DataFrame
print("---------><---------------------------")

print(df.to_string())  # complete DataFrame