# What happens when you run the following code? Why?

This program greets Victor 3 times and then greets Nina 3 times.

    NAME = 'Victor'
    print('Good Morning, ' + NAME)
    print('Good Afternoon, ' + NAME)
    print('Good Evening, ' + NAME)

    NAME = 'Nina'
    print('Good Morning, ' + NAME)
    print('Good Afternoon, ' + NAME)
    print('Good Evening, ' + NAME)

On the first line the variable NAME is assign as value "Victor". So the following greeting lines will be using "Victor" as an output.

However, there is a variable reassignment for the line,

    Name = "Nina"

Therefore the following line will be using the value "Nina" as the output. Do note that python do note have absolute constant variable even though we use only CAPS to declare the variable. Best case is to change the variable NAME to name, to use lowercase to follow non-constant variable naming convention.