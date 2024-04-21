# How would you print all the numbers in the following range?

range(3, 17, 4)

# At first I did not understand the question.
# What I though was to print all the numbers from 3 - 17

# Since range() is a lazy sequence, what we can do is to convert it into an ordered collection
# And the print it out

print(list(range(3,17,4)))