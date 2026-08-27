import matplotlib.pyplot as plt

# Example GenAI data
tokens = [100, 200, 300, 400, 500, 600, 700]
response_time = [1.2, 1.8, 2.1, 2.9, 3.4, 4.0, 4.6]

plt.scatter(tokens, response_time, marker='*',color = 'red')

plt.xlabel("Number of Tokens")
plt.ylabel("Response Time (seconds)")
plt.title("GenAI: Tokens vs Response Time")

plt.show()