# Create a new list from an existing iterable

mylist = [8, 7, 6, 5, 4, 3, 2, 1]

# Create a loop (Option-1 )
# square = []
# for number in mylist:
#     square.append(number ** 2)

# Use map function (Option- 2)

# square = map(lambda x: x**2, mylist)

# Use list comprehension (Option-3; Recommended)
# square = [item**2 for item in mylist]  # replaces map function

# odd = [item for item in mylist if item % 2 == 1]  # replaces filter function
# variable=[<expression> <loop> <conditional_statement>]


# Dictionary Comprehension
# Create  a new dictionary where key is the number and value is the square of the number
# square = {1: 1, 2: 4, 3: 9}
square = {item: item**2 for item in mylist}
odd_square = {item: item ** 2 for item in mylist if item % 2 == 1}


odd_square = {}  # Traditional
for item in mylist:
    if (item % 2 == 1):
        odd_square[item] = item**2
