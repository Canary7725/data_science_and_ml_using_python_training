# This program is used to demonstrate formatted output using a sample marksheet.

# name,roll,marks_in_eng,marks_in_sci,marks_in_maths --> Calculated total and percentage --> Display


def calculateTotal(*args):
    return (sum(args))


def calculatePercentage(obtained_marks):
    return (obtained_marks/300)*100


def calculateDivision(percentage):
    if (percentage >= 80 and percentage < 100):
        return "Distinction"
    elif (percentage >= 70 and percentage < 80):
        return "First Division"
    elif (percentage >= 60 and percentage < 70):
        return "Second Division"
    elif (percentage >= 40 and percentage < 60):
        return "Third Division"
    elif (percentage < 40 and percentage >= 0):
        return "Not Graded"
    else:
        return "Invalid"


def isPass(marks):
    if (marks > 40):
        return True
    else:
        return False


name = input("Enter your name: ")
roll = int(input("Enter your Roll Number: "))

marks_in_eng = float(input("Enter your marks in English: "))
marks_in_sci = float(input("Enter your marks in Science: "))
marks_in_maths = float(input("Enter your marks in Maths: "))

obtained_marks = calculateTotal(marks_in_eng, marks_in_maths, marks_in_sci)

percentage = calculatePercentage(obtained_marks=obtained_marks)

division = calculateDivision(percentage=percentage)

if (isPass(marks_in_sci) and isPass(marks_in_maths) and isPass(marks_in_eng)):
    result = "Pass"
else:
    result = "Fail"

print(f"""
    -----------------Marksheet-------------
    Your name: {name}
    Your Roll: {roll}
    ---------------------------------------
    Marks in English: {marks_in_eng}
    Marks in Science: {marks_in_sci}
    Marks in Maths: {marks_in_maths}
    ---------------------------------------
    Obtained Marks: {obtained_marks}
    Percentage: {percentage:.2f}
    Grade: {division}
    Result:{result}
""")
