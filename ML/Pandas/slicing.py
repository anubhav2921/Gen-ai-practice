import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("youtube_tech_channels_20251120_133753.csv")

avg = df["subscribers"].mean()

print("Average subscribers:", avg)

plt.bar(["Average Subscribers"], [avg])
plt.ylabel("Subscribers")
plt.title("Average YouTube Channel Subscribers")
plt.show()