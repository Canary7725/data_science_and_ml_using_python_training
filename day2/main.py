# This program is used to demonstrate formatted output using a sample marksheet.

# name,roll,marks_in_eng,marks_in_sci,marks_in_maths --> Calculated total and percentage --> Display

name = input("Enter your name: ")
roll = int(input("Enter your Roll Number: "))

marks_in_eng = float(input("Enter your marks in English: "))
marks_in_sci = float(input("Enter your marks in Science: "))
marks_in_maths = float(input("Enter your marks in Maths: "))

obtained_marks = marks_in_eng + marks_in_maths + marks_in_sci
percentage = (obtained_marks/300) * 100

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
""")
