import matplotlib.pyplot as plt
import random

plt.figure(1)  # create a new window/plot

plt.plot([120, 40, 10, 0])  # plot y against the index
plt.plot([1, 2, 3, 4, 5, 6], [1, 4, 9, 16, 25, 36])  # plot x vs y

plt.figure(2)  # make second window

x1 = [x for x in range(1, 11)]
y1 = [y ** 2 for y in x1]

plt.plot(x1, y1, color='green', marker='*', markersize=10, linestyle=':', alpha=0.5, label="myPlot")

#  title axes label unit numbers key (TALUNK)
plt.xlabel('time (seconds)')
plt.ylabel('excitement level (YAYS)')
plt.title('Example Plot')
plt.axis([0, 11, 0, 120])  # [xmin, xmax, ymin, ymax]

plt.show()  # opens the window/plot

