# ============================================================
#             MATPLOTLIB - COMPLETE LINE GRAPH
# ============================================================

# Import Matplotlib
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. DATA
# ------------------------------------------------------------

# X-axis data
epochs = [1, 2, 3, 4, 5]

# Y-axis data
loss = [0.9, 0.7, 0.55, 0.4, 0.3]


# ------------------------------------------------------------
# 2. CREATE FIGURE
# ------------------------------------------------------------

# Create a figure and set its size
plt.figure(figsize=(10, 6))


# ------------------------------------------------------------
# 3. LINE PLOT
# ------------------------------------------------------------

plt.plot(
    epochs,                 # X-axis values
    loss,                   # Y-axis values

    color="red",            # Line color

    linestyle="-",          # Line style
                            # "-"  = solid
                            # "--" = dashed
                            # ":"  = dotted
                            # "-." = dash-dot

    linewidth=3,            # Line thickness

    marker="h",             # Marker shape
                            # "h" = hexagon
                            # "o" = circle
                            # "^" = triangle
                            # "s" = square
                            # "*" = star
                            # "D" = diamond

    markersize=10,          # Marker size

    markerfacecolor="yellow",  # Marker inside color

    markeredgecolor="black",   # Marker border color

    markeredgewidth=2,      # Marker border thickness

    alpha=0.9,              # Transparency

    label="Training Loss"   # Name for legend
)


# ------------------------------------------------------------
# 4. X-AXIS LABEL
# ------------------------------------------------------------

plt.xlabel(
    "Epoch",                # X-axis name
    color="green",          # Text color
    fontsize=13,            # Text size
    fontweight="bold"       # Bold text
)


# ------------------------------------------------------------
# 5. Y-AXIS LABEL
# ------------------------------------------------------------

plt.ylabel(
    "Loss",
    color="purple",
    fontsize=13,
    fontweight="bold"
)


# ------------------------------------------------------------
# 6. TITLE
# ------------------------------------------------------------

plt.title(
    "GenAI Model Training Loss",
    color="darkorange",
    fontsize=18,
    fontweight="bold"
)


# ------------------------------------------------------------
# 7. X-AXIS LIMIT
# ------------------------------------------------------------

# Set minimum and maximum values of X-axis
plt.xlim(0, 6)


# ------------------------------------------------------------
# 8. Y-AXIS LIMIT
# ------------------------------------------------------------

# Set minimum and maximum values of Y-axis
plt.ylim(0, 1)


# ------------------------------------------------------------
# 9. X-AXIS TICKS
# ------------------------------------------------------------

# Set specific values on X-axis
plt.xticks(
    [1, 2, 3, 4, 5],
    fontsize=11
)


# ------------------------------------------------------------
# 10. Y-AXIS TICKS
# ------------------------------------------------------------

# Set specific values on Y-axis
plt.yticks(
    [0, 0.2, 0.4, 0.6, 0.8, 1.0],
    fontsize=11
)


# ------------------------------------------------------------
# 11. GRID
# ------------------------------------------------------------

plt.grid(
    True,                   # Turn grid ON

    color="gray",           # Grid color

    linestyle="--",         # Dashed grid

    linewidth=0.8,          # Grid thickness

    alpha=0.5               # Grid transparency
)


# ------------------------------------------------------------
# 12. LEGEND
# ------------------------------------------------------------

# Display the label defined inside plt.plot()
plt.legend(
    fontsize=11,
    loc="upper right"
)


# ------------------------------------------------------------
# 13. ADD TEXT
# ------------------------------------------------------------

# Add text at a particular X,Y position
plt.text(
    3.2,
    0.65,
    "Loss is decreasing",
    fontsize=11,
    color="blue"
)


# ------------------------------------------------------------
# 14. ANNOTATION
# ------------------------------------------------------------

# Point to an important location on the graph
plt.annotate(
    "Lowest Loss",
    xy=(5, 0.3),             # Point being highlighted
    xytext=(4, 0.5),         # Position of the text

    arrowprops=dict(
        arrowstyle="->",
        color="black"
    ),

    fontsize=11,
    color="darkgreen"
)


# ------------------------------------------------------------
# 15. HORIZONTAL LINE
# ------------------------------------------------------------

# Draw a horizontal reference line
plt.axhline(
    y=0.5,
    color="blue",
    linestyle="--",
    alpha=0.6
)


# ------------------------------------------------------------
# 16. VERTICAL LINE
# ------------------------------------------------------------

# Draw a vertical reference line
plt.axvline(
    x=3,
    color="purple",
    linestyle=":",
    alpha=0.6
)


# ------------------------------------------------------------
# 17. FILL AREA
# ------------------------------------------------------------

# Fill the area below the line
plt.fill_between(
    epochs,
    loss,
    alpha=0.15
)


# ------------------------------------------------------------
# 18. SAVE GRAPH
# ------------------------------------------------------------

# Save the graph as an image
plt.savefig(
    "genai_training_loss.png",

    dpi=300,                # Image quality

    bbox_inches="tight"     # Remove unnecessary empty space
)


# ------------------------------------------------------------
# 19. DISPLAY GRAPH
# ------------------------------------------------------------

plt.show()


# ------------------------------------------------------------
# 20. CLOSE GRAPH
# ------------------------------------------------------------

# Close the current figure after displaying/saving it
# plt.close()