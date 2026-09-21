# def <function_name> ():
#   function logic goes here(indented)
#   return

# def add_two_numbers(num1=0, num2=0):  # Parameters
#     return num1+num2


# print("Hello")


# sum = add_two_numbers(5, 6)
# print(sum)


# def greet(name="Adam", age=43):  # Parameters --> Placeholders for value to be passed onto a function
#     print(f"{name} is {age}")


# # Arguments --> Actual value that is to be passed onto the function
# greet("Sita", 21)  # Positional Argument
# greet(age=21, name="Sita")  # Keyword Argument

# greet()


# def min_max(numbers):
#     return min(numbers), max(numbers)


# minimum, maximum = min_max([1, 2, 3, 4, 5, 6, 7, 8])  # (1,8)

# print(f"{maximum},{minimum}")


# Variable score --> local or global
# Local variable can only be used on the functions they are defined at..
# num5 = 9  # 00010


# def swap(num1, num2):
#     temp = num1
#     num1 = num2
#     num2 = temp
#     return num1, num2


# print(swap(4, 5))


def total(*args):
    return sum(args)


print(total(5, 6))
print(total(1, 2, 3, 4, 5, 6))
print(total())


def students(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():  # Dictionary Iterations
        print(key, value)


students(name="Adam", grade=9, division="A+")
{
    'name': 'Adam',
    'grade': 9,
    'division': 'A+'
}
