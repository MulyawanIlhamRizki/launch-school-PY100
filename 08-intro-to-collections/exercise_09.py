
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# 1. Are the lists assigned to my_list and another_list equal?
# Yes they are equal. We can check it using:

print(my_list == another_list) # True

# 2. Are the lists assigned to my_list and another_list the same object?
# No, list(my_list) created a new object. Therefore it is a pass by object assignment

print(my_list is another_list) # False

# 3. Are the nested lists at index 3 of my_list and another_list equal?
# It is equal. We can check is using:

print(my_list[3] == another_list[3]) # True

# 4. Are the nested lists at index 3 of my_list and another_list the same object?
# They are the same object. This is because the a list inside a list create a shallow copy.
# Shallow copies do not create a new nested lists. Only a reference to the nested list gets copied.

print(my_list[3] is another_list[3]) # True