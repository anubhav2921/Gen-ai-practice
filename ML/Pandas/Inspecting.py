#2. Inspecting a Dataset
import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 25, 30],
    "Salary": [30000, 45000, 60000],
    "Purchased": ["No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

print(df)

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 25, 30],
    "Salary": [30000, 45000, 60000],
    "Purchased": ["No", "Yes", "Yes"]
}
print(df.head())
print(df.tail())