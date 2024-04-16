
age = input("How old are you? ")

print(f"You are {age} years old.")

# input() returns string, we need to use coercion for age variable to operate successfully
print(f"In 10 years, you will be {int(age) + 10} years old.")
print(f"In 20 years, you will be {int(age) + 20} years old.")
print(f"In 30 years, you will be {int(age) + 30} years old.")
print(f"In 40 years, you will be {int(age) + 40} years old.")

# This exercise is similar to 04-variables/age.py
# The main difference is the use of input() function