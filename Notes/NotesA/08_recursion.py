#  Recursion - function calling itself

def f():
    print("f")
    #  f()  # similar to an infinte loop, but different.  RecursionDepthError
    print("END")

f()  # function calling itself (we had to comment it out)


def g():
    print("g")
    f()

g()


# Controlling recursion with depth
def controlled(depth, max_depth):
    print("Recursion depth:", depth)
    if depth < max_depth:
        controlled(depth + 1, max_depth)
    print("Recursion depth", depth, "has closed.")

controlled(0, 10)


# Fibonacci Sequence  0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# def fibonacci_recursion(n):
#     print("Calculating Fibonacci", n)
#
#     # base case
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     # recursive case
#     else:
#         return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
#
# fibonacci_recursion(10)



