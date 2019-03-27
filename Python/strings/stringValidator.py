# https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=python

'''
Python has built-in string validation methods for basic data. It can  check if
a string is composed of alphabetical characters, alpha numeric chars, digits, etc.

Sample input:
qA2

Sample output:
True
True
True
True
True
'''


input_string = raw_input()


# Lines below check if any of the characters in the strong are of a particular type

print any(char.isalnum() for char in input_string)
print any(char.isalpha() for char in input_string)
print any(char.isdigit() for char in input_string)
print any(char.islower() for char in input_string)
print any(char.isupper() for char in input_string)

# Methods below check if every character is the string is of a particular type

# input_string.isalnum()
# input_string.isalpha()
# input_string.isdigit()
# input_string.islower()
# input_string.isupper()
