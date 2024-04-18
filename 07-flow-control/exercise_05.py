def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# What does this code output, and why?


# it will output "Empty"
# Because the arguments that is being passed into the function is an
# empty list. Empty list is considered to be falsely
# Thus it will go into the else output.