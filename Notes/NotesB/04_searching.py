# Searching and read/write files

# forward slash goes into a directory.  ".." goes "up" a directory.
# by default, open() opens a file to read ('r')
file = open('../resources/super_villains.txt', 'r')
print(file)
file.close()  # ends your access to the file

# Open a file to write with 'w'
# Overwrites entire file

# Opeen a file to append with 'a'
file = open('../resources/super_villains.txt', 'a')
file.write("Mia the Horrible\n")
file.close()

# Go through the info in the file line by line
file = open('../resources/super_villains.txt', 'r')
for line in file:
    print(line.strip().upper())

file.close()  # ends your access to the file

# .strip() method strips out spaces, tabs, returns (/t, /n etc.)
print("Hi\n".strip())
print("     Hello".strip())

#  Better way to open files (syntactic sugar)
with open('../resources/super_villains.txt') as f:
    for line in f:
        print("Hello", line)

# Read data into a list (array)
with open('../resources/super_villains.txt') as f:
    villains = [x.strip().upper() for x in f]

print(villains)


# Linear Search

# Python way
print("VARVARA TEMPEST" in villains)  # in keyword

# Brute force way
i = 0
key = "VARVARA TEMPEST"

while i < (len(villains) - 1) and key != villains[i]:
    i += 1

if i < len(villains) - 1:
    print("Found", key, "at position", i)
else:
    print(key, "not found.")

# Make a function out of it!
def linear_search(key, my_list):
    """
    Searches for key inside of list and returns True if you find it.
    :param key: item to find
    :param my_list: list to find key in
    :return: bool found
    """
    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:
        i += 1

    if i < len(villains) - 1:
        print("Found", key, "at position", i)
        return True
    else:
        print(key, "not found.")
        return False

print(linear_search("Lavinia Nyx", villains))


# Binary Search