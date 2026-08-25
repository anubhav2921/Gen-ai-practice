import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5]
loss = [0.9, 0.7, 0.55, 0.4, 0.3]

plt.plot(
    epochs,
    loss,
    color="blue",
    marker="o",
    markersize=8,
    markerfacecolor="red",
    linewidth=3
)

plt.xlabel("Epoch", color="green", fontsize=12)
plt.ylabel("Loss", color="purple", fontsize=12)
plt.title("GenAI Model Training Loss", color="darkorange", fontsize=16)

plt.grid(True, color="gray", linestyle="--", alpha=0.5)

plt.show()