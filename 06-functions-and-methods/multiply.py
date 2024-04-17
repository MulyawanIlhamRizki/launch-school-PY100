# Write a program that uses a multiply function to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def multiply(num_1, num_2):
    return(num_1 * num_2)


def get_number(prompt):
    entry = input(prompt)
    # Need to use coercion to change from input, str -> float
    return float(entry)


input_1 = get_number("Enter the first number: ")
input_2 = get_number("Enter the second number: ")


result = multiply(input_1, input_2)
print(f"{input_1} * {input_2} = {result}")