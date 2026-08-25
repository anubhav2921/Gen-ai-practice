# ============================================================
#       STUDENT DEPRESSION DATASET - MATPLOTLIB
# ============================================================

# Pandas import karo
import pandas as pd

# Matplotlib import karo
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. CSV FILE READ
# ------------------------------------------------------------

# CSV file ko read karo
df = pd.read_csv("Student Depression Dataset.csv")


# First 5 rows print karo
print(df.head())


# Column names print karo
print(df.columns)


# Dataset ka shape print karo
# 27901 rows, 18 columns
print(df.shape)


# ============================================================
# 2. DEPRESSION - BAR CHART
# ============================================================

# Depression column mein 0 aur 1 ka count
count = df["Depression"].value_counts()


# Figure ka size
plt.figure(figsize=(8, 5))


# Bar chart
plt.bar(
    count.index.astype(str),   # X-axis
    count.values,              # Y-axis

    color="red",               # Bar color
    edgecolor="black",         # Border color
    linewidth=2,               # Border thickness
    alpha=0.8                  # Transparency
)


# X-axis label
plt.xlabel(
    "Depression",
    fontsize=12,
    color="green"
)


# Y-axis label
plt.ylabel(
    "Number of Students",
    fontsize=12,
    color="purple"
)


# Title
plt.title(
    "Student Depression",
    fontsize=16,
    color="darkorange"
)


# Grid
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)


# Graph display
plt.show()


# ============================================================
# 3. AGE - HISTOGRAM
# ============================================================

plt.figure(figsize=(8, 5))


# Age distribution
plt.hist(
    df["Age"].dropna(),
    bins=10,
    color="skyblue",
    edgecolor="black",
    alpha=0.8
)


plt.xlabel("Age")
plt.ylabel("Number of Students")

plt.title(
    "Student Age Distribution",
    fontsize=16
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ============================================================
# 4. CGPA - HISTOGRAM
# ============================================================

plt.figure(figsize=(8, 5))


# CGPA distribution
plt.hist(
    df["CGPA"].dropna(),
    bins=10,
    color="orange",
    edgecolor="black",
    alpha=0.8
)


plt.xlabel("CGPA")
plt.ylabel("Number of Students")

plt.title(
    "Student CGPA Distribution",
    fontsize=16
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ============================================================
# 5. GENDER - BAR CHART
# ============================================================

gender_count = df["Gender"].value_counts()


plt.figure(figsize=(8, 5))


plt.bar(
    gender_count.index,
    gender_count.values,
    color="purple",
    edgecolor="black",
    linewidth=2
)


plt.xlabel("Gender")
plt.ylabel("Number of Students")

plt.title(
    "Students by Gender",
    fontsize=16
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ============================================================
# 6. DEPRESSION - PIE CHART
# ============================================================

plt.figure(figsize=(7, 7))


plt.pie(
    count.values,
    labels=count.index.astype(str),
    autopct="%1.1f%%",
    startangle=90
)


plt.title(
    "Depression Percentage",
    fontsize=16
)

plt.show()


# ============================================================
# 7. ACADEMIC PRESSURE - BAR CHART
# ============================================================

academic_count = df["Academic Pressure"].value_counts().sort_index()


plt.figure(figsize=(8, 5))


plt.bar(
    academic_count.index.astype(str),
    academic_count.values,
    color="green",
    edgecolor="black",
    linewidth=2
)


plt.xlabel("Academic Pressure")
plt.ylabel("Number of Students")

plt.title(
    "Academic Pressure Among Students",
    fontsize=16
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()


# ============================================================
# 8. STUDY SATISFACTION - BAR CHART
# ============================================================

satisfaction = df["Study Satisfaction"].value_counts().sort_index()


plt.figure(figsize=(8, 5))


plt.bar(
    satisfaction.index.astype(str),
    satisfaction.values,
    color="blue",
    edgecolor="black"
)


plt.xlabel("Study Satisfaction")
plt.ylabel("Number of Students")

plt.title(
    "Study Satisfaction Among Students",
    fontsize=16
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.show()