# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# It will result in an error
# Not enough arguments being passed into the function
# Missing positional argument for the "first" parameter