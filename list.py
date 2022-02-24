

from ast import Delete
from unicodedata import name


names=['Vasiliy', 'Peter', 'Alex', 'Mark']


print(names)
print(names[3].upper())

# Append in list
print("---------------Append in list--------------------")
names.append('Tolja')
print(names)


# Insert in list
print("---------------Insert in list--------------------")
names.insert((5), 'Mark')
print(names)


# Delete in list
print("---------------Delete in list--------------------")
del names[3]
print(names)

names.remove('Mark')
print(names)