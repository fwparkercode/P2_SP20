# Plotting (with matplotlib)
import matplotlib.pyplot as plt

plt.figure(1)  # creates a new plot/window

plt.plot([1, 2, 3, 3]) # plots y against the index x
plt.plot([1, 2, 3, 4], [12, 8, 2, 1])  # ([x points], [y points])

plt.figure(2)  # new window/plot

x_points = [x for x in range(1, 11)]
y_points = [y ** 2 for y in x_points]

plt.plot(x_points, y_points, color='green', marker='*', markersize=10, linestyle='--', alpha=0.5)

# TALUNK (title, axes, labels, units, numbers, key)
plt.title("Example Plot")
plt.xlabel("Time (s)", color='red', fontsize=20)
plt.ylabel("Excitement (Yays!)")
plt.axis([0, 11, 0, 110])  # [xmin, xmax, ymin, ymax]

plt.show()