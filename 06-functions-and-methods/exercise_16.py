def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# In the code shown below, identify all of the function names and parameters present in the code. 
# Include the line numbers for each item identified.

# 1: function name = multiply | parameters = left, right
# 3: function name = get_num | parameters = prompt
# 4: function name = float, input
# 7: function name = get_num
# 8: function name = get_num
# 9: function name = multiply
# 10: function name = print