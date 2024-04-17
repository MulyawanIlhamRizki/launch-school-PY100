# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# It will cause an error, NameError to be exact
# This is because foo only exist in the function scope of set_foo()