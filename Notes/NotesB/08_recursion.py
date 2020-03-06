# Recursion - function calling itself

def f():
    print("f")

def g():
    print("g")
    f()
    # g()  # RecursionError recursion depth exceeded
    print("END")

g()  # error commented out


# Control recursion with depth
def controlled(depth):
    print("recursion depth", depth)
    if depth > 0:
        controlled(depth - 1)
    print("recursion depth", depth, "has closed.")


controlled(10)


