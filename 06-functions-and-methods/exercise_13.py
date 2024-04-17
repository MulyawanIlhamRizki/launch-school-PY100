# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# It will result in an error
# There is no argument for the "third" parameter in the function


# LS answer: 
# Once Python sees a positional parameter has a default value, all subsequent parameters
# must have default values