# Histogram ka use numerical data ka distribution dekhne ke liye hota hai.

import matplotlib.pyplot as plt
import numpy as np

marks = np.array([45, 52, 55, 61, 63, 65, 67, 72, 75, 80, 85, 90])
avg = np.array([45, 52, 55, 61, 63, 65, 67, 72, 75, 80, 85, 90])
plt.hist(marks)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")

plt.show()