# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])
# Oranges

# Get the last value
print(fruits[-1])
# Pears

# Get length
print(len(fruits))
# 4

# Append to list
fruits.append('Mangos')
#['Apples', 'Oranges', 'Grapes', 'Pears','Mangos']

# Remove from list
fruits.remove('Grapes')
#['Apples', 'Oranges', 'Pears','Mangos']

# Insert into position
fruits.insert(2, 'Strawberries')
# ['Apple','Oranges','Strawberries','Pears','Mangos']

# Change value
fruits[0] = 'Blueberries'
# ['Blueberries','Oranges','Strawberries','Pears','Mangos']

# Remove with pop
fruits.pop(2)
# ['Blueberries','Oranges','Pears','Mangos']

# Reverse list
fruits.reverse()
# ['Pears','Oranges','Mangos','Blueberries']

# Sort list
fruits.sort()
# ['Blueberries', 'Mangos', 'Oranges', 'Pears']

# Reverse sort
fruits.sort(reverse=True)
# ['Pears', 'Oranges', 'Mangos', 'Blueberries']
print(fruits)

