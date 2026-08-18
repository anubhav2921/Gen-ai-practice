#Scaler Operation ---> 
import numpy as np

array = np.random.random((3, 3)) * 100

print("Array:")
print(array)

print("\nGreater than 50:")
print(array > 50)

print("\nLess than 50:")
print(array < 50)

print("\nEqual to 50:")
print(array == 50)

print("\nGreater than or equal to 50:")
print(array >= 50)

print("\nLess than or equal to 50:")
print(array <= 50)

print("\nNot equal to 50:")
print(array != 50)

print(array*array)


max_colum = np.max(array, axis=0)
print("\n max_colum:")
print(max_colum)


max_row = np.max(array, axis=1)
print("\n max_row:")
print(max_row)

#Sum()-------> calculate the sum of all value given in matrix

sum_row = np.sum(array, axis=1)
print("\n sum_row:")
print(sum_row)

sum_colum = np.sum(array, axis=0)
print("\n sum_colum:")
print(sum_colum)


import numpy as np

array = np.random.random((3, 3)) * 100

print("Array:")
print(array)

# Product of all elements
print("Product:", np.prod(array))

# Sum of all elements
print("Sum:", np.sum(array))

# Minimum value
print("Minimum:", np.min(array))

# Maximum value
print("Maximum:", np.max(array))

# Mean
print("Mean:", np.mean(array))

# Standard deviation
print("Standard deviation:", np.std(array))

# Variance
print("Variance:", np.var(array))

# Product row-wise
print("Product of each row:", np.prod(array, axis=1))

# Product column-wise
print("Product of each column:", np.prod(array, axis=0))