from hospitalPerson import HospitalPerson
from utils import findBook, getConfig


# config = getConfig("Hospital_Management_System/config.json")


personell_menu = """
    Select option:
    ---------------
    1. Doctor
    2. Patient
    ---------------
    3. Exit
"""

doctor_menu = """
    Select Option:
    --------------
    1. Insert Doctor
    2. Display All Doctors
    3. Search Doctor
    4. Update Doctor
    5. Delete Doctor
    ---------------
    6. Exit
"""

patient_menu = """
    Select Option:
    --------------
    1. Insert Patient
    2. Display All DPatient
    3. Search Patient
    4. Update Patient
    5. Delete Patient
    ---------------
    6. Exit
"""

while True:
    print(personell_menu)
    personell_choice = int(input("Enter a choice: "))

    if personell_choice == 1:
        while True:
            print(doctor_menu)
            choice = int(input("Enter a choice"))
            if (choice == 6):
                break

    if personell_choice == 2:
        while True:
            print(patient_menu)
            choice = int(input("Enter a choice"))
            if (choice == 6):
                break
    if personell_choice == 3:
        break
