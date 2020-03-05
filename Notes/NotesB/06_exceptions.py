# Exceptions (use me sparingly please)

# Exception - a condition that results in abnormal program flow
# Exception handling - what we actively do to accommodate exceptions
# Throw/Raise - Exception condition occurs
# Catch - Code handles thrown exception
# Unhandled exception - Thrown not caught.  Program killer.

x = 2
y = 0

# Divide by Zero (ZeroDivisionError)
try:
    print(x / y)
except:
    print("Infinity")


# Conversion Error (ValueError)
try:
    int("T")
except:
    print("Number was not valid")


# handle with a loop
done = False

while not done:
    try:
        user_input = int(input("Enter an integer: "))
        done = True
    except:
        print("Number is not valid")


# File Opening (IOError, FileNotFoundError)
try:
    file = open("AliceInWonderland.txt")
except:
    print("Could not open file")


# Use built in error types for python to check what error occurred.
try:
    # my_file = open("myfile.txt")
    # int("Hello")
    print(1 / 0)
except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print("Invalid conversion")
    print(e)
except ZeroDivisionError as e:
    print("Error:", e)
