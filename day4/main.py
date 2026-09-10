
student_record = {}

student_record["roll"] = int(input("Enter roll number: "))
student_record["name"] = input("Enter your name: ")

student_record["science"] = float(input("Enter marks in science: "))
student_record["maths"] = float(input("Enter marks in maths: "))
student_record["english"] = float(input("Enter marks in english: "))

student_record["obtained_marks"] = student_record["english"] + \
    student_record["maths"]+student_record["science"]

student_record["percentage"] = (student_record["obtained_marks"]/300)*100

print(student_record)
