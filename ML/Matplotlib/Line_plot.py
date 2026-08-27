import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Student Depression Dataset.csv")

# Age ko integer mein convert
df['Age'] = df['Age'].astype('int32')

# Age ke according sort
df = df.sort_values('Age')

# Line Plot
plt.plot(df['Age'], df['CGPA'])

plt.xlabel("Age")
plt.ylabel("CGPA")
plt.title("Age vs CGPA")
plt.grid(True)

plt.show()