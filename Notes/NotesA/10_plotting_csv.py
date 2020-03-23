import csv
import matplotlib.pyplot as plt


with open("../Libraries_-_2019_Visitors_by_Location (1).csv") as f:
    reader = csv.reader(f)  # makes a reader object
    data = list(reader)


# plot the attendance data for our favorite library

header = data.pop(0)
#  print(data)
print(header)

print(data[0])
names = [x[0] for x in data]
print(names)

sulzer_index = names.index("Sulzer Regional Library")
print(sulzer_index)

sulzer_data = data[sulzer_index]
print(sulzer_data)

sulzer_by_month = sulzer_data[4:-1]
print(sulzer_by_month)

sulzer_by_month = [int(x) for x in sulzer_by_month]
print(sulzer_by_month)

month_numbers = [x for x in range(12)]

month_names = header[4:-1]
print(month_names)

plt.figure(1, tight_layout=True)  # tight_layout makes everything fit in figure

# plt.plot(month_numbers, sulzer_by_month)
plt.plot(month_numbers, sulzer_by_month, label="Sulzer")  # line plot
plt.xticks(month_numbers, month_names, rotation=75)

plt.title("Sulzer Visitors by Month", fontsize=20, color='blue')
plt.ylabel("Visitors")
plt.axis([-1, 12, 0, 40000]) # [xmin, xmax, ymin, ymax]
plt.legend(fancybox=True, shadow=True)


# Starting over with just header and data
# plot top 10 libraries for YTD totals
plt.figure(2, tight_layout=True, figsize=(14, 6))  # figsize in inches

print(header)
data.sort(key=lambda x: int(x[-1]))
print(data)

top_ten = data[-10:]
top_ten_ytd = [int(x[-1]) for x in top_ten]

top_ten_names = [x[0] for x in top_ten]
x_vals = [x for x in range(len(top_ten))]

plt.barh(x_vals, top_ten_ytd)  # barh is a horizontal bar graph
plt.yticks(x_vals, top_ten_names, fontsize=10)

plt.xlabel("Visitors YTD")
plt.title("Top Ten Most Visited Chicago Libraries")

plt.show()

