# Assume argument is an integer

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# To test the function, should print even
print(even_or_odd(8))

# It should print odd
print(even_or_odd(3))


# Challenge! Refactor it by using ternary

def odd_or_even(number):
    print("even" if number % 2 == 0 else "odd")

odd_or_even(2)