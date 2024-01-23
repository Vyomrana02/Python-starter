# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))
# Hello, my name is Brad and I am 37

# String Formatting
# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))
# My name is Brad and I am 37


# F-Strings from python (3.6+)
print(f'Hello, my name is {name} and I am {age}')
# Hello, my name is Brad and I am 37

# String Methods

s = 'helloworld'

# Capitalize string
print(s.capitalize())
# Helloworld

# Make all uppercase
print(s.upper())
# HELLOWORLD

# Make all lower
print(s.lower())
# helloworld

# Swap case
print(s.swapcase())
# HELLOWORLD

# Get length
print(len(s))
# 10

# Replace
print(s.replace('world', 'everyone'))
# helloeveryone

# Count
sub = 'h'
print(s.count(sub))
# 1

# Starts with
print(s.startswith('hello'))
# True

# Ends with
print(s.endswith('d'))
# True

# Split into a list
print(s.split())
# ['helloworld']

# Find position
print(s.find('r'))
# 7

# Is all alphanumeric
print(s.isalnum())
# True

# Is all alphabetic
print(s.isalpha())
# True

# Is all numeric
print(s.isnumeric())
# False