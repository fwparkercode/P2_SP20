# LISTS
import random

my_names = ["Abe", "Bev", "Cam", "Dan", "Eve", "Flo"]
my_numbers = [5, 9, 12, 6, -3, 6]

# Indexing lists
print(my_names)
print(my_names[5])  # Cam
print(my_names[-1])  # Flo
print(my_names[:3])  # Abe to Cam
print(my_names[3:5])  # Dan and Eve
print(my_names[:])  # Everybody

# copy a list
my_copy = my_names  # No!!! Stop it!
my_copy.append("Gil")
print(my_copy)
print(my_names)
my_copy = my_names[:]  # Do it this way!
my_names.append("Hal")
print(my_copy)
print(my_names)

# 2d lists
my_2d = [["Peanut", "Butter", "Jelly"], [8, "Hello"], ["Spam", "Eggs"]]
print(my_2d[1]) # [8, "Hello"]
print(my_2d[1][1])  # Hello
my_2d[1].append("Bye")
print(my_2d)

# if in
if "Hal" in my_names:
    print("Hal is in my_names")


# LIST FUNCTIONS
print(len(my_names))  # length of the list (not the last index)
print(min(my_numbers))  # lowest value
print(max(my_numbers))  # highest
print(sum(my_numbers))

print(min(my_names))  # first in alphabetical order
my_names.append("aaron")
print(min(my_names))  # first in alphabetical order


# LIST METHODS
print(my_names.index("Cam"))  # returns the index of "Cam"
my_names.append("Cam")
print(my_names.index("Cam"))  # only sees the first instance
print(my_names.count("Cam"))  # number of instances
print(my_names.count("Mia"))

my_names.append("Deb")
del my_names[my_names.index("aaron")]
print(my_names)
my_names.sort()
print(my_names)
my_names.reverse()
print(my_names)


# MODIFYING LISTS
del my_names[4]
print(my_names)

my_names.pop()  # pops one off the end of the list
print(my_names)

end_of_list = my_names.pop()  # pops off end AND RETURNS IT
print(my_names)
print(end_of_list)

front_of_list = my_names.pop(0)  # pop by index
print(front_of_list)
print(my_names)


# concatenation
first = "Francis"
last = "Parker"
print(first + last)  # smooshes them together

print(my_names + my_numbers)


# ITERATING THROUGH LISTS
# make a list of numbers 0 through 9
# make empty list, make for loop, append the index to the for loop

my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)


# print every item in the list you just created (use a FOR EACH loop)
# FOR EACH only looks at a copy of each item in the list
for item in my_list:
    item += 1
    print(item)

print(my_list)

# add one to every item in the list (use an INDEX VARIABLE loop)
# This is how we modify a list in a loop
for i in range(len(my_list)):
    my_list[i] += 1

print(my_list)

#  LIST COMPREHENSIONS

# make a list of numbers 0 to 100
my_list = []

for i in range(101):
    my_list.append(i)

print(my_list)

# using list comprehension
# [OUTPUT for item in loop]
my_list = [x for x in range(101)]
print(my_list)




# make a list 0 to 100 squared
my_list = []

for i in range(101):
    my_list.append(i ** 2)

print(my_list)

my_list = [x ** 2 for x in range(101)]
print(my_list)


# make a list of 1 to 100 squared, but filter out the odd numbers
my_list = []

for i in range(101):
    if(i ** 2) % 2 == 0:
        my_list.append(i ** 2)

print(my_list)

my_list = [x ** 2 for x in range(101) if x ** 2 % 2 == 0]


# roll a single die 100 times and add it to a list
my_list = []

for i in range(100):
    my_list.append(random.randrange(1, 7))

print(my_list)

my_list = [random.randrange(1, 7) for x in range(100)]
print(my_list)


# roll two die and add them to a list
my_list = []

for i in range(100):
    my_list.append([random.randrange(1, 7), random.randrange(1, 7)])

print(my_list)



my_list = [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)]
print(my_list)


# go back through list and make a new list of sums of two die
my_sums = [sum(x) for x in my_list]
print(my_sums)


# make a list from the 100 rolls that shows only the doubles
my_doubles = [x for x in my_list if x[0] == x[1]]
print(my_doubles)


# all at once
# roll 100 pairs and only put in the doubles

my_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)] for x in range(100)] if x[0] == x[1]]

print(my_list)


#  Working with Strings is a lot like lists
first = "Francis"
last = "Parker"
print(first[0])
first = first.upper()
print(first + last)
print(last[-2:])

for letter in first:
    print(letter)

if "N" in first:
    print("YES")

