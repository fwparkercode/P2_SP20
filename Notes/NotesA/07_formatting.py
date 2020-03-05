# FORMATTING

import random

# round(n, digits)
print(round(243.2434235, 2))

# format method (a string method)
a = 234.53465
b = 24987978234
print("My number is {}!!".format(a))
print("My numbers are {} and {}.".format(a, b))
print("My numbers are {1} and {0}. {1} is my favorite".format(a, b))  # you can specify the order

# numerical_order:spaceholder+justification+sign+width+commas+precision+datatype+notation

# justification and spacing
# ^center, >right, <left
for i in range(20):
    c = random.randrange(2000)
    #print("{:6}".format(c))  # six spaces are reserved for the number
    print("**{:^30}**".format(c))  # 30 spaces and centered

# commas
for i in range(20):
    c = random.randrange(10000000)
    print("${:8,}".format(c))

# precision and datatype (d dec/int, f float, b binary)
for i in range(20):
    c = random.random() * 1000
    print("{:14.3f}".format(c))  # 14 spaces to three decimals as a float

for i in range(20):
    c = random.randrange(1000)
    print("{:<10b}".format(c))


# scientific notation
for i in range(20):
    c = random.randrange(1000)
    print("{:.2e}".format(c))

x = 6.77e11
print(x)


