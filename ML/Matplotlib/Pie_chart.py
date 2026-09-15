# ---> today we will be learing the Pia chart 

#1. What is a Pie Chart?
# A pie chart shows how a total is divided into different categories.

import matplotlib.pyplot as plt

skills = ["Python", "Java", "GenAI", "SQL"]
values = [40, 20, 25, 15]

plt.title("Pie Chart Example")
plt.pie(values)
plt.show()

