# 1. First: Understand DataFrames
# A Pandas DataFrame is basically a table.
import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 25, 30],
    "Salary": [30000, 45000, 60000],
    "Purchased": ["No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

print(df)

#   Name  Age  Salary Purchased
# 0    A   20   30000        No
# 1    B   25   45000       Yes
# 2    C   30   60000       Yes
# PS C:\practice-gen-ai\ML\Pandas> 

