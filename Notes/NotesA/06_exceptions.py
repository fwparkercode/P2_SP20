# Exceptions (use me sparingly please)

# Exception - condition that results in abnormal program flow
# Exception handling - what we actively do for an exception
# Throw/Raise - abnormal conditions throw or raise an exception
# Catch - Code that handles the abnormal condition
# Unhandled exceptions - program killers.  Thrown... but not caught.


# Divide by zero error (ZeroDivisionError)
x = 0
y = 2

try:
    print(y / x)
except:
    print("Invalid operation, divide by zero.")

# Conversion error (ValueError)
done = False

while not done:
    try:
        user_input = int(input("Enter a valid integer: "))
        done = True
    except:
        print("Number not valid, enter an integer")


# File opening (IOError, FileNotFoundError)

try:
    file = open("AliceInWonderland.txt")
except:
    print("File not found.")


# Use the built in error types for Python

try:
    #my_file = open("myfile.txt")
    #print(1 / 0)
    int("Hello")
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Fool! You can't divide by zero")
except ValueError:
    print("Invalid int conversion")
except:
    print("Unknown Error")



# Make an MPG calculator

try:
    miles = float(input("Miles traveled: "))
    gallons = float(input("Gallons used: "))
except ValueError:
    print("You entered an invalid number.")


try:
    print("MPG is", miles / gallons)
except:
    print("Your MPG is infinite!!!")
finally:
    print("Finally will always run regardless of exception or no exception")


