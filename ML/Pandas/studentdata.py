import pandas as pd

df = pd.read_csv("Student Depression Dataset.csv")

print(df)

df.nunique()
df["city"].value_counts()
df.describe(include="all")