import pandas as pd

df = pd.read_csv('Student Depression Dataset.csv')

print(df)

print(((df['Gender'] == 'Male') & 
       (df['Age'] < 24) & 
       (df['City'] == 'Pune')).sum())

print(df.columns)

print(df.dtypes)

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

# Select rows and columns
print(
    df.loc[
        0:4,
        ['Gender', 'Age', 'City']
    ]
)

# Pune OR Delhi
print(
    df[
        (df['City'] == 'Pune') |
        (df['City'] == 'Delhi')
    ]
)
print(df['Sleep Duration'].unique())
 
#----->OUTPUT<-------
#<StringArray>
# ['5-6 hours', 'Less than 5 hours', '7-8 hours', 'More than 8 hours', 'Others']
# Length: 5, dtype: str



# Create a column that tells whether the student is an adult
df['Adult'] = df['Age'] >= 18

print(df[['Age', 'Adult']])