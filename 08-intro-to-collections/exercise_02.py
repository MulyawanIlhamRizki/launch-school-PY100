# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# Since tuples are immutable, what we can do is to change the data type to mutable: List
# And then change it back to tuple

new_stuff = list(stuff)
new_stuff[2] = "goodbye"
stuff = tuple(new_stuff)

print(stuff)