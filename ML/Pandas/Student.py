import pandas as pd

df = pd.read_csv("Student Depression Dataset.csv")

# 1. First 5 rows
print("\n--- HEAD ---")
print(df.head())

# 2. Last 5 rows
print("\n--- TAIL ---")
print(df.tail())

# 3. Number of rows and columns
print("\n--- SHAPE ---")
print(df.shape)

# 4. Column names
print("\n--- COLUMNS ---")
print(df.columns.tolist())

# 5. Data types and non-null values
print("\n--- INFO ---")
print(df.info())

# 6. Statistical summary
print("\n--- DESCRIBE ---")
print(df.describe(include="all"))

# 7. Missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 8. Duplicate rows
print("\n--- DUPLICATES ---")
print(df.duplicated().sum())

# 9. Unique values
print("\n--- UNIQUE VALUES ---")
for col in df.columns:
    print(col, ":", df[col].nunique())

# 10. Target distribution
print("\n--- DEPRESSION DISTRIBUTION ---")
print(df["Depression"].value_counts())


print("\n------->Pandas sample() function, it is used to randomly select rows from a DataFrame.<---------------------\n")

print(df.sample(7))

import pandas as pd

data = {
    "Name": ["Amit", "Rahul", None, "Priya", "Neha"],
    "Age": [20, None, 22, 21, None],
    "Marks": [85, 90, None, 78, 95]
}

print(pd.DataFrame(data))