import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sample GenAI data
tokens = np.array([100, 200, 300, 400, 500, 600, 700])
response_time = 10 + tokens + 3 + np.random.randint(0, 300, 7)

# Create DataFrame
df = pd.DataFrame({
    "Tokens": tokens,
    "Response_Time": response_time
})

print(df)

# Scatter plot with half/gradient color
plt.scatter(
    df["Tokens"],
    df["Response_Time"],
    c=df["Tokens"],
    cmap="viridis"
)

plt.xlabel("Number of Tokens")
plt.ylabel("Response Time (seconds)")
plt.title("GenAI: Tokens vs Response Time")

plt.colorbar(label="Tokens")
plt.show()