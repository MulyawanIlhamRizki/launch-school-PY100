# To what value does the following expression evaluate?

'foo' == 'Foo'

# The expression above will return False. 
# Python will only compare the character "f" to "F"
# Character comparison starts from left to right, in reference to the ASCII table
# Capital character does not equal to lower case character based on the ASCII table

# To check my answer

# Will return False
print("foo" == "Foo")
print("f" == "F")

# Will return True
print("oo" == "oo")