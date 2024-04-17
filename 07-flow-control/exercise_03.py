def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# Without running the following code, what does it print? Why?

# Answer: 
# It will output:
# Product2
# Product not found!

# Product2 is because there is a case that matches with the line 12 argument
# Product not found! is because the argument is an integer whereas
# the cases are a string type, therefore it will match with the default case