# Grouped Data Types --> List, Tuple, Set, Dictionary


# Lists    0        1           2
fruits = ['apple', 'pear', 'watermelon',
          'kiwi', 'banana', 'apple', 'mango']  # Initilize

# nested_list_example = [[1, 2], [2, 3], [4, 5], [3, 4]]  # Nested List
# print(nested_list_example[0][0])
# print(fruits)

# print(fruits[-1])  # Indexing --> -1 means the last element of the list

# print(fruits[1:3])  # Slicing
# print(fruits[::-1])  # Reversing a list

# fruits[0] = 'papaya'  # Changing item of list using index
# print(fruits)

# Adding item(s) into the list
# fruits.append('papaya')
# fruits.insert(3, 'papaya')
# fruits.extend(['papaya', 'coconut'])
# print(fruits)

# Removing item(s) from the list
# fruits.remove('apple')  # Remove by value
# fruits.pop(3)  # Remove by index
# fruits.clear()
# print(fruits)

# Methods / Functions

# print(len(fruits))
# print(fruits.count('apple'))
# print(fruits.index('apple'))


# Membership
if 'banana' in fruits:
    print(True)
else:
    print(False)
