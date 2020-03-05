# Sorting
import random
import time

# Swap values
a = 1
b = 2

temp = a
a = b
b = temp

print(a, b)

# pythonic way
a, b = b, a  # works only in Python
print(a, b)

# make a random list of 100 numbers with values from 1 to 99
my_list = [random.randrange(1, 100) for x in range(1000)]
my_list2 = my_list[:]
my_list3 = my_list[:]
print(my_list)

total_iterations = 0
start_time = time.perf_counter()


#  SELECTION SORT
for cur_pos in range(len(my_list)):
    min_pos = cur_pos  # current dancer is the assumed lowest
    for scan_pos in range(cur_pos + 1, len(my_list)):
        total_iterations += 1
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos  # if we find a lower dancer, we update the min
    my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]  # swap dancers

#print(my_list)
print("Selection sort time:", time.perf_counter() - start_time)
print("Selection sort iterations:", total_iterations)


# INSERTION SORT
total_iterations = 0
start_time = time.perf_counter()

for key_pos in range(1, len(my_list2)):
    key_val = my_list2[key_pos]  # key dancer
    scan_pos = key_pos - 1  # look to the dancer's left
    while scan_pos >= 0 and key_val < my_list2[scan_pos]:
        total_iterations += 1
        my_list2[scan_pos + 1] = my_list2[scan_pos]  # move the scan position left
        scan_pos -= 1
    my_list2[scan_pos + 1] = key_val  # commit the move

# print(my_list2)
print("Insertion sort time:", time.perf_counter() - start_time)
print("Insertion sort iterations:", total_iterations)


start_time = time.perf_counter()
my_list3.sort()
print("Python sort time:", time.perf_counter() - start_time)


# Optional function parameters
print("Hello", end=" ")  # default end is "\n"
print("World", end="!\n")
print("Hello", "World", sep="Big", end="!!!\n")  # default sep is space

def hello(name, time_of_day="morning"):
    print("Hello", name, "good", time_of_day)

hello("Star", "afternoon")
hello("Mia")
hello("James", time_of_day="evening")



# Lambda Functions
# When you need a function, but don't want to make a function
# Also called anonymous functions

# lambda parameter: returned
double_me = lambda x: x * 2
print(double_me(5))

product = lambda a, b: a * b
print(product(4, 6))

# Real world sorting with Python
my_list = [random.randrange(1, 100) for x in range(100)]
print(my_list)

my_2dlist = [[random.randrange(1, 100), random.randrange(1, 100)] for x in range(100)]
print(my_2dlist)

# sort method (changes the list in place)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_2dlist.sort(key=lambda a: a[0])
print(my_2dlist)
my_2dlist.sort(key=lambda a: a[1])
print(my_2dlist)
my_2dlist.sort(reverse=True, key=lambda a: sum(a))
print(my_2dlist)


# Sorted function (Returns a new list)
new_list = sorted(my_2dlist, reverse=True, key=lambda x: abs(x[0] - x[1]))
print(new_list)







