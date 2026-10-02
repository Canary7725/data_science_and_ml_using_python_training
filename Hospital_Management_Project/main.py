from hospitalPerson import HospitalPerson
from utils import getConfig, findDoctors

from doctor_class import Doctor, displayAllDoctors, displayOneDoctor, deleteDoctor


config = getConfig("Hospital_Management_Project/config.json")
patient_file_path = config.get("patient_filepath")
doctor_file_path = config.get("doctor_filepath")

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
    2. Display All Patient
    3. Search Patient
    4. Update Patient
    5. Delete Patient
    ---------------
    6. Exit
"""

while True:
    print(personell_menu)
    personell_choice = int(input("Enter a choice: "))

    if personell_choice == 1:  # Exit from doctor menu
        while True:
            print(doctor_menu)
            choice = int(input("Enter a choice: "))
            if (choice == 6):
                break
            elif choice == 1:  # Insert Doctor
                # id, name, age, gender, phone, specialization, type
                try:
                    id = int(input("Enter Doctor ID: "))
                    name = input("Enter Doctor Name: ")
                    age = int(input("Enter Doctor Age: "))
                    gender = input("Enter Doctor Gender: ")
                    phone = input("Enter Doctor Phone Number: ")
                    specialization = input("Enter Doctor specialization: ")
                    type = input("Enter type (Full-Time or Part-Time): ")

                    doctor_obj = Doctor(id=id, name=name, age=age, gender=gender,
                                        phone=phone, specialization=specialization, type=type)
                    doctor_obj.insertDoctor()
                except Exception as e:
                    print(f"Something went wrong. {e}")

            elif choice == 2:  # Display All Doctor Records
                displayAllDoctors()

            elif choice == 3:  # Search for Doctor
                id_to_search = int(input("Enter ID to search for doctor: "))
                displayOneDoctor(id=id_to_search)

            elif choice == 4:  # Update Doctor Info
                id_to_update = int(
                    input("Enter the id whose details is to be updated: "))
                if findDoctors(id=id_to_update):
                    id = int(input("Enter Doctor ID: "))
                    name = input("Enter Doctor Name: ")
                    age = int(input("Enter Doctor Age: "))
                    gender = input("Enter Doctor Gender: ")
                    phone = input("Enter Doctor Phone Number: ")
                    specialization = input("Enter Doctor specialization: ")
                    type = input("Enter type (Full-Time or Part-Time): ")

                    doctor_obj = Doctor(id=id, name=name, age=age, gender=gender,
                                        phone=phone, specialization=specialization, type=type)

                    doctor_obj.updateDoctor(id=id_to_update)
                else:
                    print("Doctor with that ID not found in the system.")
            elif choice == 5:  # Delete Doctor by Id
                id_to_delete = int(
                    input("Enter ID of doctor whose record is to be deleted: "))
                if (findDoctors(id_to_delete)):
                    deleteDoctor(id_to_delete)
                else:
                    print("Doctor with that ID not found in the system.")

    if personell_choice == 2:
        while True:
            print(patient_menu)
            choice = int(input("Enter a choice: "))
            if (choice == 6):
                break
    if personell_choice == 3:
        break
