# Use the REPL and the arithmetic operators to extract the individual digits of 4936

num = 4936

# Extract One place
one = num % 10

# Remove one place from initial number
num = (num - one) / 10

# Extract Tens place
tens = num % 10

# Remove Tens place from initial number
num = (num - tens) / 10


# Extract Hundreds place
hundreds = num % 10

# Remove Hundreds place from initial number
num = (num - hundreds) / 10

# Extract Thousands place
thousands = num % 10

# Remove Thousands place from initial number
num = (num - thousands) / 10