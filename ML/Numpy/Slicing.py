# NumPy Array Slicing
# Slicing means selecting a portion of an array.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])

arr[:3]      # first 3 elements
arr[2:]      # from index 2 to the end
arr[::2]     # every 2nd element
arr[::-1]    # reverse the array

import numpy as np

arrr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

import numpy as np

arrr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

for i in arrr:
    print(i)
