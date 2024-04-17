def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


# Using the code below, classify the identifiers as global, local, or built-in

# 1: multiply = global, left = local, right = local
# 2: left = local, right = local
# 4: get_num = global, prompt = local
# 5: float = built-in, input = built-in, prompt = local
# 7: first_number = global, get_num = global
# 8: second_number = global, get_num = global
# 9: product = global, multiply = global, first_number = global, second_number = global
# 10: print = built-in, first_number = global, second_number = global, product = global