# Types of loop --> for, while
# It should always have a stopping condition

# my_list = [1, 2, 3, 4, 5, 6]

# for item in my_list:
#     print(item)


# for <loop_variable> in <iterable_variable>:
# for item in range(100):  # List Traversal
#     print(item)

# range(*starting_value,ending_value,*skipping_value)
# sample_range = range(100, 2, -1)
# for i in sample_range:
#     print(i)


# Find the largest number on a list
# my_list = [34, 123, 543, 234, 6512, 654]

# create a temp_variable called largest and assign it to 0
# iterate through each item
# compare with the largest until now
# if larger then change the value

# largest = my_list[0]
# for item in my_list:
#     if (item > largest):
#         largest = item
# print(largest)


# my_dict = {
#     "name": "Adam",
#     "age": 23,
#     "faculty": "BIT"
# }

# for a, b in my_dict.items():
#     print(f"Key:{a} | Value:{b}")

# for number in range(51):
#     if (number % 3 == 0 or number % 5 == 0):
#         print(number)

# For each iteration of outer loop, the inner loop completes an entire cycle
for column in range(1, 6, 2):  # 1, 3, 5, 7
    for spaces in range((5 - column) // 2):
        print(" ", end="")
    for row in range(column):
        print("*", end=" ")

    print()


# my_list = [1, 2, 3, 4, 5, 6]

# for index, number in enumerate(my_list):
#     print(f"Index:{index} | Value:{number}")

# name = ["Adam", "Chloe"]
# marks = [89, 98]

# for name, marks in zip(name, marks):
#     print(f"Name:{name} | Marks:{marks}")


# Program to check if the input number is prime or composite
