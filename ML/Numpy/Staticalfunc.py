import numpy as np

array = np.random.random((3, 3)) * 100

print("Array:")
print(array)

print("Mean:", np.mean(array))
print("Median:", np.median(array))
print("Standard Deviation:", np.std(array))
print("Variance:", np.var(array))
print("Minimum:", np.min(array))
print("Maximum:", np.max(array))
print("25th Percentile:", np.percentile(array, 25))
print("50th Percentile:", np.percentile(array, 50))
print("75th Percentile:", np.percentile(array, 75))


# Using axis
# For a 3×3 array:
print(np.mean(array, axis=0))  # Column-wise
print(np.mean(array, axis=1))  # Row-wise