import pandas as pd

df = pd.read_csv("youtube_tech_videos_20251120_133004.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df.describe())
print(df.isnull().sum())