import pandas as pd

df = pd.read_csv('Student Depression Dataset.csv')

print(df)

print(((df['Gender'] == 'Male') & 
       (df['Age'] < 24) & 
       (df['City'] == 'Pune')).sum())