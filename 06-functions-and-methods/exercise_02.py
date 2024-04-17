# What does this program print? Why?

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# This program will print "bar"
# Because there is a global scope where foo = "bar"
# Although the is a function call on the main program, 
# foo = "qux" only exists inside the function set_foo()