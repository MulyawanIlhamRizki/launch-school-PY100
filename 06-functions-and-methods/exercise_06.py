# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# This code does not print anything to the terminal
# The return parameters is empty due to print(words) is 1 line below it
# The function does not recognize print(words) as it comes after return