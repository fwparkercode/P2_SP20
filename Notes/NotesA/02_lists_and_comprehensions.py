# LISTS
import random

my_list = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [5, 9, 12, 6, 3, -3, 4]

# using indices
print(my_list[1])  # Bev
print(my_list[-1])  # Gus
print(my_list[1:4])  # Bev to Dan as a list
print(my_list[-3:])  # Eve to Gus


my_copy = my_list  # does not create a copy, just another link to the original
my_copy.append("Hal")
print(my_copy)
print(my_list)

my_copy = my_list[:]  # DO THIS!
my_copy.append("Ida")
print(my_copy)
print(my_list)

# 2d lists
my_2d = [["Abe", 8], ["Bev", 7], ["Cam", 4]]
print(my_2d[1][0])
my_2d[2].append("Wilson")
print(my_2d)

# If in
if "Abe" in my_list:
    print("Abe is there")

if "abe" in my_list:
    print("abe is there")

if random.randrange(10) in [3, 5, 6, 8, 9]:
    print("yay!")


# LIST FUNCTIONS
print(len(my_list))  # returns the length of a list
print(min(my_numlist))  # returns the lowest
print(max(my_numlist))  # highest value
print(max(my_list))  # highest alphabetically
print(sum(my_numlist))  # sums the list

# LIST METHODS
print(my_list.index("Cam"))  # returns the index of the found object
my_list.append("Cam")  # two cams?
print(my_list.index("Cam"))  # only returns the first one
print(my_list.count("Cam"))  # returns the number of "Cam"s
print(my_list.count("Abe"))

my_list.append("Deb")
my_list.sort()  # orders the list
print(my_list)
my_list.reverse()  # reverse the current order
print(my_list)

# manipulating the list
my_list.pop()  # pops one off the end of the list
print(my_list)
my_person = my_list.pop()  # returns the popped item
print(my_person)
print(my_list)
front_of_line = my_list.pop(0)
print(front_of_line)
print(my_list)

# destroy an item
del my_list[1]
print(my_list)

# concatenation
first = "Francis"
last = "Parker"
print(first, last)
print(first + last)  # smooshed 2 strings together

print(my_list + my_numlist)


#  ITERATING THROUGH A LIST