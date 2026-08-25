# ============================================================
# PANDAS COMPLETE NOTES
# Student Depression Dataset
# ============================================================


# ============================================================
# 1. IMPORT PANDAS
# ============================================================

import pandas as pd


# ============================================================
# 2. READ DATASET
# ============================================================

# Read CSV file
df = pd.read_csv('Student Depression Dataset.csv')

# Display complete DataFrame
print(df)


# ============================================================
# 3. BASIC INFORMATION
# ============================================================

# Number of rows and columns
print(df.shape)

# Column names
print(df.columns)

# Data types of all columns
print(df.dtypes)

# Complete information about dataset
print(df.info())

# Statistical summary
print(df.describe())


# ============================================================
# 4. VIEW DATA
# ============================================================

# First 5 rows
print(df.head())

# First 10 rows
print(df.head(10))

# Last 5 rows
print(df.tail())

# Last 10 rows
print(df.tail(10))

# Display 5 random rows
print(df.sample(5))


# ============================================================
# 5. SELECT COLUMNS
# ============================================================

# Select one column
print(df['Gender'])

# Select multiple columns
print(df[['Gender', 'Age', 'City']])

# Select important columns
print(
    df[
        [
            'Gender',
            'Age',
            'City',
            'CGPA',
            'Depression'
        ]
    ]
)


# ============================================================
# 6. SELECT ROWS USING loc
# ============================================================

# Select first row
print(df.loc[0])

# Select rows 0 to 4
print(df.loc[0:4])

# Select rows and columns
print(
    df.loc[
        0:4,
        ['Gender', 'Age', 'City']
    ]
)


# ============================================================
# 7. SELECT ROWS USING iloc
# ============================================================

# Select first row
print(df.iloc[0])

# Select first 5 rows
print(df.iloc[0:5])

# Select first row and first column
print(df.iloc[0, 0])

# Select first 5 rows and first 3 columns
print(df.iloc[0:5, 0:3])


# ============================================================
# 8. FILTERING DATA
# ============================================================

# ------------------------------------------------------------
# One condition
# ------------------------------------------------------------

# Male students
print(
    df[df['Gender'] == 'Male']
)

# Students younger than 24
print(
    df[df['Age'] < 24]
)

# Students from Pune
print(
    df[df['City'] == 'Pune']
)


# ------------------------------------------------------------
# AND (&)
# ------------------------------------------------------------

# Male AND age below 24
print(
    df[
        (df['Gender'] == 'Male') &
        (df['Age'] < 24)
    ]
)

# Male + age below 24 + Pune
print(
    df[
        (df['Gender'] == 'Male') &
        (df['Age'] < 24) &
        (df['City'] == 'Pune')
    ]
)


# ------------------------------------------------------------
# OR (|)
# ------------------------------------------------------------

# Male OR Female
print(
    df[
        (df['Gender'] == 'Male') |
        (df['Gender'] == 'Female')
    ]
)

# Pune OR Delhi
print(
    df[
        (df['City'] == 'Pune') |
        (df['City'] == 'Delhi')
    ]
)


# ------------------------------------------------------------
# NOT (~)
# ------------------------------------------------------------

# Students who are NOT male
print(
    df[
        ~(df['Gender'] == 'Male')
    ]
)


# ============================================================
# 9. FILTER USING isin()
# ============================================================

# Students from Pune or Delhi
print(
    df[
        df['City'].isin(['Pune', 'Delhi'])
    ]
)

# Students with selected degrees
print(
    df[
        df['Degree'].isin(['B.Tech', 'B.Sc'])
    ]
)


# ============================================================
# 10. FILTER USING between()
# ============================================================

# Age between 18 and 24
print(
    df[
        df['Age'].between(18, 24)
    ]
)

# CGPA between 7 and 10
print(
    df[
        df['CGPA'].between(7, 10)
    ]
)


# ============================================================
# 11. FILTER USING query()
# ============================================================

# Age below 24
print(
    df.query('Age < 24')
)

# Male students below 24
print(
    df.query(
        "Gender == 'Male' and Age < 24"
    )
)

# Students from Pune
print(
    df.query(
        "City == 'Pune'"
    )
)


# ============================================================
# 12. COUNT FILTERED ROWS
# ============================================================

# Store filtered data
result = df[
    (df['Gender'] == 'Male') &
    (df['Age'] < 24) &
    (df['City'] == 'Pune')
]

# Display result
print(result)

# Number of matching rows
print(len(result))

# Alternative method
print(
    (
        (df['Gender'] == 'Male') &
        (df['Age'] < 24) &
        (df['City'] == 'Pune')
    ).sum()
)


# ============================================================
# 13. MISSING VALUES
# ============================================================

# Check missing values
print(df.isnull())

# Count missing values in each column
print(df.isnull().sum())

# Display only columns having missing values
missing = df.isnull().sum()

print(
    missing[missing > 0]
)

# Check total missing values
print(
    df.isnull().sum().sum()
)


# ============================================================
# 14. REMOVE MISSING VALUES
# ============================================================

# Remove rows containing missing values
df_clean = df.dropna()

print(df_clean)


# Remove rows only when ALL values are missing
df_clean = df.dropna(how='all')


# ============================================================
# 15. FILL MISSING VALUES
# ============================================================

# Fill missing values with 0
df.fillna(0)

# Fill missing City values
df['City'] = df['City'].fillna('Unknown')

# Fill missing Age with mean
df['Age'] = df['Age'].fillna(
    df['Age'].mean()
)


# ============================================================
# 16. DUPLICATE DATA
# ============================================================

# Check duplicate rows
print(df.duplicated())

# Count duplicate rows
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()


# ============================================================
# 17. SORTING
# ============================================================

# Sort age ascending
print(
    df.sort_values('Age')
)

# Sort age descending
print(
    df.sort_values(
        'Age',
        ascending=False
    )
)

# Sort by multiple columns
print(
    df.sort_values(
        ['City', 'Age']
    )
)


# ============================================================
# 18. UNIQUE VALUES
# ============================================================

# Unique genders
print(
    df['Gender'].unique()
)

# Unique cities
print(
    df['City'].unique()
)

# Unique degrees
print(
    df['Degree'].unique()
)

# Number of unique cities
print(
    df['City'].nunique()
)


# ============================================================
# 19. VALUE COUNTS
# ============================================================

# Number of students by gender
print(
    df['Gender'].value_counts()
)

# Number of students by city
print(
    df['City'].value_counts()
)

# Number of students by degree
print(
    df['Degree'].value_counts()
)

# Depression distribution
print(
    df['Depression'].value_counts()
)


# ============================================================
# 20. NUMERICAL FUNCTIONS
# ============================================================

# Average age
print(df['Age'].mean())

# Median age
print(df['Age'].median())

# Minimum age
print(df['Age'].min())

# Maximum age
print(df['Age'].max())

# Total age
print(df['Age'].sum())

# Number of age values
print(df['Age'].count())

# Standard deviation
print(df['Age'].std())

# Variance
print(df['Age'].var())


# ============================================================
# 21. IMPORTANT FUNCTIONS FOR CGPA
# ============================================================

# Average CGPA
print(
    df['CGPA'].mean()
)

# Highest CGPA
print(
    df['CGPA'].max()
)

# Lowest CGPA
print(
    df['CGPA'].min()
)

# Median CGPA
print(
    df['CGPA'].median()
)


# ============================================================
# 22. GROUPBY
# ============================================================

# Average age by gender
print(
    df.groupby('Gender')['Age'].mean()
)

# Average CGPA by gender
print(
    df.groupby('Gender')['CGPA'].mean()
)

# Number of students by city
print(
    df.groupby('City').size()
)

# Average CGPA by city
print(
    df.groupby('City')['CGPA'].mean()
)


# ============================================================
# 23. GROUPBY + AGG()
# ============================================================

# Multiple calculations for Age
print(
    df.groupby('Gender')['Age'].agg(
        ['mean', 'min', 'max', 'count']
    )
)

# Multiple calculations for CGPA
print(
    df.groupby('Gender')['CGPA'].agg(
        ['mean', 'min', 'max']
    )
)


# ============================================================
# 24. GROUPBY MULTIPLE COLUMNS
# ============================================================

print(
    df.groupby(
        ['Gender', 'City']
    )['Age'].mean()
)


# ============================================================
# 25. APPLY()
# ============================================================

# Add 1 to every age
df['New_Age'] = df['Age'].apply(
    lambda x: x + 1
)

print(df)


# Create age category
def age_category(age):

    # If age is below 18
    if age < 18:
        return 'Below 18'

    # If age is 18 to 24
    elif age <= 24:
        return '18-24'

    # If age is above 24
    else:
        return '25+'


df['Age_Category'] = df['Age'].apply(
    age_category
)

print(df)


# ============================================================
# 26. STRING FUNCTIONS
# ============================================================

# Convert city to uppercase
print(
    df['City'].str.upper()
)

# Convert city to lowercase
print(
    df['City'].str.lower()
)

# Check whether city contains Pune
print(
    df['City'].str.contains(
        'Pune',
        na=False
    )
)

# Length of city names
print(
    df['City'].str.len()
)

# Replace text
df['City'] = df['City'].str.replace(
    'Pune',
    'PUNE',
    regex=False
)


# ============================================================
# 27. DATA TYPES
# ============================================================

# Check data type
print(
    df['Age'].dtype
)

# Convert Age to integer
df['Age'] = df['Age'].astype(int)

# Convert Age to string
df['Age'] = df['Age'].astype(str)

# Convert safely to numeric
df['Age'] = pd.to_numeric(
    df['Age'],
    errors='coerce'
)


# ============================================================
# 28. RENAME COLUMNS
# ============================================================

# Rename one column
df = df.rename(
    columns={
        'Age': 'Student_Age'
    }
)

# Rename multiple columns
df = df.rename(
    columns={
        'Gender': 'Sex',
        'CGPA': 'Student_CGPA'
    }
)


# ============================================================
# 29. ADD COLUMNS
# ============================================================

# Create new column
df['Age_Double'] = df['Student_Age'] * 2


# Create Boolean column
df['Is_Adult'] = (
    df['Student_Age'] >= 18
)


# ============================================================
# 30. DELETE COLUMNS
# ============================================================

# Delete one column
df = df.drop(
    columns=['Age_Double']
)

# Delete multiple columns
df = df.drop(
    columns=[
        'Is_Adult',
        'New_Age'
    ],
    errors='ignore'
)


# ============================================================
# 31. INDEX
# ============================================================

# Set City as index
# df = df.set_index('City')

# Reset index
# df = df.reset_index()

# Reset index without keeping old index
df = df.reset_index(drop=True)


# ============================================================
# 32. CONCAT
# ============================================================

# Combine DataFrames vertically
# result = pd.concat(
#     [df1, df2],
#     ignore_index=True
# )


# ============================================================
# 33. MERGE
# ============================================================

# Combine DataFrames using a common column
# result = pd.merge(
#     df1,
#     df2,
#     on='id',
#     how='inner'
# )


# ============================================================
# 34. PIVOT TABLE
# ============================================================

# Average CGPA by gender
pivot = pd.pivot_table(
    df,
    values='Student_CGPA',
    index='Gender',
    aggfunc='mean'
)

print(pivot)


# ============================================================
# 35. CROSSTAB
# ============================================================

# Count Gender vs Depression
cross = pd.crosstab(
    df['Gender'],
    df['Depression']
)

print(cross)


# ============================================================
# 36. COPY
# ============================================================

# Create independent copy
new_df = df.copy()


# ============================================================
# 37. SAVE DATA
# ============================================================

# Save as CSV
df.to_csv(
    'output.csv',
    index=False
)

# Save as Excel
df.to_excel(
    'output.xlsx',
    index=False
)

# Save as JSON
df.to_json(
    'output.json'
)