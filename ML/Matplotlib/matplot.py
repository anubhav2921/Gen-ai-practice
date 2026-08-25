import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# READ CSV FILE
# =====================================================

df = pd.read_csv('Student Depression Dataset.csv')


# =====================================================
# DISPLAY DATA
# =====================================================

# Complete DataFrame
print(df)

# First 5 rows
print(df.head())

# First 10 rows
print(df.head(10))

# Last 5 rows
print(df.tail())

# Last 10 rows
print(df.tail(10))


# =====================================================
# DATA VISUALISATION
# =====================================================


# -----------------------------------------------------
# 1. BAR CHART - Gender
# -----------------------------------------------------

# Count Male/Female students
gender_count = df['Gender'].value_counts()

# Create bar chart
plt.bar(
    gender_count.index,
    gender_count.values
)

# Title
plt.title('Students by Gender')

# X-axis label
plt.xlabel('Gender')

# Y-axis label
plt.ylabel('Number of Students')

# Display graph
plt.show()