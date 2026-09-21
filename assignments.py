# Ask the user for two numbers and an operator (`+`, `-`, `*`, `/`).
# Print the result. Handle division by zero with a friendly message instead of crashing.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# operator = input("Enter the operator (+, -. *. /)")

# if (operator == "+"):
#     print(f"Sum is: {num1+num2}")
# elif (operator == "-"):
#     print(f"Difference is: {num1-num2}")
# elif (operator == "*"):
#     print(f"Product is: {num1*num2}")
# elif (operator == "/"):
#     if (num2 == 0):
#         print("Denominator cannot be 0 in division.")
#     else:
#         print(f"Division is: {num1/num2}")
# else:
#     print("Invalid operator")


# Ask for the bill amount and a tip percentage (default 10% if left blank).
# Print the tip amount and total, formatted to 2 decimal places.

# billed_amout = float(input("Enter total billed amount: "))
# tip = float(input("Enter tip amount: ") or 10)
# tip_amount = tip/100*billed_amout

# total_amount = billed_amout+tip_amount

# print(f"""
#     -----Restaurant Bill------
#     ------------------------
#     Total Billed Amount: {billed_amout}
#     Total Tip Amount: {tip_amount}
#     Total Amount: {total_amount}
# """)

# Ask for weight (kg) and height (m).
# Compute BMI (`weight / height ** 2`) and print it formatted to 1 decimal place,
# along with the category (Underweight / Normal / Overweight) using comparisons.
# <18 underweight 18-25-->Normal  25-30-->overweight >30 obese

# weight = float(input("Enter weight(in KG): "))
# height = float(input("Enter height (in Meters): "))
# bmi = weight/(height*height)
# print(f"BMI: {bmi:.2f}")

# if (bmi < 18.0 and bmi >= 0):
#     print("Underweight")
# elif (bmi >= 18 and bmi < 25):
#     print("Normal Weight")
# elif (bmi >= 25 and bmi < 30):
#     print("Overweight")
# elif (bmi > 30):
#     print("Obese")
# else:
#     print("Something went wrong")


# Ask for three side lengths. Determine if they form a valid triangle,
# and if so, whether it's equilateral, isosceles, or scalene.

# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     if a == b and b == c:
#         print("Equilateral Triangle")
#     elif a == b or a == c or b == c:
#         print("Isosceles Triangle")
#     else:
#         print("Scalene Triangle")
# else:
#     print("Invalid Triangle")

# Store a username and password. Ask the user to log in.
# Use nested conditions to give a specific message for "wrong username," "wrong password," and "success."
# Ask repeatedly until both the username and password are right.

# username = "admin"
# password = "12345"

# while (True):
#     input_username = input("Enter your username: ")
#     if (input_username != username):
#         print("Invalid username")
#         continue
#     input_password = input("Enter your password: ")
#     if (input_password != password):
#         print("Invalid Password")
#         continue
#     print("Login Sucessful")
#     break


# Check if the input number is prime or composite.

# number = int(input("Enter a number: "))
# count = 0
# if (number < 2):
#     print("Invalid Number")
# else:
#     for i in range(2, number):
#         if (number % i == 0):
#             count += 1

#     if (count == 0):
#         print("Prime")
#     else:
#         print("Composite")


# Given a list of tuples like `[("Sita", 88), ("Ram", 95), ("Maya", 91)]`,
# find and print the name and score of the student with the highest score —
# without using `sorted()` or `max()`.

# students = [("Sita", 88), ("Ram", 95), ("Maya", 91)]

# name = students[0][0]
# score = students[0][1]

# for student in students:
#     if student[1] > score:
#         name = student[0]
#         score = student[1]

# print(name, score)


# Number Guessing Game**
# The program picks a secret number (hardcode one). Loop, asking the user to guess:
# - Print "Too high" / "Too low" / "Correct!" using conditions
# - Count how many guesses it took
# - Use `break` to end the loop on a correct guess


# secret = 7
# count = 0

# while (True):
#     guess = int(input("Enter your guess: "))
#     count = count + 1

#     if guess > secret:
#         print("Too high")
#     elif guess < secret:
#         print("Too low")
#     else:
#         print("Correct!")
#         print("Guesses:", count)
#         break
