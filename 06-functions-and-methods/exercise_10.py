# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# It will print:
# 42
# 3.141592
# 2

# There are only 2 arguments being passed however, there is a default value for the third parameters.
# Thus print(third) will print the default value