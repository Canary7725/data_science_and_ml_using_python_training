# is_raining = True

# is_snowy = False
a, b = 5, 6
if (not a == b):
    print("Not equals")

    # if (is_raining):  # Nested If
    #     if (have_an_umbrella):
    #         print("Bring it.")
    #     print("Buy it.")

    # if (is_raining):  # If-Else
    #     print("Bring an umbrella.")
    # else:
    #     print("Leave it")

    # if (is_raining):  # If-Elif-Else
    #     print("Bring an umbrella.")
    # elif (is_snowy):
    #     print("Wear a jacket")
    # else:
    #     print("Leave it")

    # percentage: >80, Distinction, >70 --> First Division,
    #  >60 --> Second Division, >40 --> Third Division
    # <40 Not Graded

percentage = -67

if (percentage >= 80 and percentage < 100):
    division = "Distinction"
elif (percentage >= 70 and percentage < 80):
    division = "First Division"
elif (percentage >= 60 and percentage < 70):
    division = "Second Division"
elif (percentage >= 40 and percentage < 60):
    division = "Third Division"
elif (percentage < 40 and percentage >= 0):
    division = "Not Graded"
else:
    division = "Invalid"

print(division)


age = 19
if (age > 18):
    status = "Adult"
else:
    status = "Minor"

status = "Adult" if age > 18 else "Minor"
