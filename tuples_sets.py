# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])
# Oranges

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))
# 3

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)
# True 

# Add to set
fruits_set.add('Grape')
# {'Apples', 'Oranges', 'Mango','Grape'}

# Remove from set
fruits_set.remove('Grape')
# {'Apples', 'Oranges', 'Mango'}

# Add duplicate
fruits_set.add('Apples')
# {'Apples', 'Oranges', 'Mango'}

# Clear set
fruits_set.clear()

# Delete
del fruits_set

# print(fruits_set)
