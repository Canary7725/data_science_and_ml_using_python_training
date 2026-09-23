

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter second number: "))
    print(num1/num2)

except ValueError as e:
    print(f"Value should be number: {e}")

except ZeroDivisionError as e:  # ZeroDivisionError's error message is stored in variable e using 'as' operator
    print(f"Division by zero is not allowed: {e}")

except:
    print("Something went wrong")


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter second number: "))
# print(num1/num2)
