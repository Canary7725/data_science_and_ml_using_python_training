# Give the users options to create and display contacts.
# Create contancts--> asks the user for name,email,phone and then store it in a file which is comma separated.
# Display contacts--> read from the file and display all the contacts

import json


def insertContact(name, email, phone, filepath):
    try:
        with open(filepath, "a") as file:
            # Add comma-separated one-liner data onto the file
            file.write(f"{name},{email},{phone}\n")
        print("Contacts saved sucessfully")

    except Exception as e:  # Use Exception if you don't know which particular exception to catch
        print(e)


def getContacts(filepath):
    try:
        final_list = []  # empty list to be appended and returned to main program
        file_content = ""
        with open(filepath, "r") as file:
            # Read entire content of the file and put it into a string variable
            file_content = file.read()
        for item in file_content.split("\n"):
            if len(item) < 2:  # Remove any empty lists or one with single item(malformed)
                continue
            final_list.append(item.split(","))
        return final_list
# split()--> it is used when we need to create a list where we give the separator.

    except Exception as e:
        print(e)


def displayContacts(filepath):
    contacts_list = getContacts(filepath=filepath)
    print(contacts_list)
    for item in contacts_list:
        print(f"Name={item[0]}")
        print(f"Email={item[1]}")
        print(f"Phone={item[2]}")
        print("\n---------------")


with open("day10/config.json", "r") as file:
    # json is a built-in package which allows the use of load() funciton
    config = json.load(file)  # it converts json file data into a dictionary
filepath = config.get("filepath")


menu = """
    -------Contact Saver-------
    ---------------------------
    1. Insert Contacts
    2. Display Contacts
    ---------------------------
    3. Exit
    ---------------------------
    """

choice = 0
while (choice != 3):
    print(menu)
    choice = int(input("Enter your choice: "))

    if (choice == 1):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone: ")
        insertContact(name=name, email=email, phone=phone, filepath=filepath)
    elif (choice == 2):
        displayContacts(filepath=filepath)
