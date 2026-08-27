import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Student Depression Dataset.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Check column names
print(df.columns.tolist())

# Convert columns to numeric
df["Study Satisfaction"] = pd.to_numeric(
    df["Study Satisfaction"],
    errors="coerce"
)

df["CGPA"] = pd.to_numeric(
    df["CGPA"],
    errors="coerce"
)

# Remove missing values
df = df.dropna(subset=["Study Satisfaction", "CGPA"])

# Scatter plot
plt.scatter(
    df["Study Satisfaction"],
    df["CGPA"],
    marker="*"
)

plt.xlabel("Study Satisfaction")
plt.ylabel("CGPA")
plt.title("Study Satisfaction vs CGPA")

plt.show()

