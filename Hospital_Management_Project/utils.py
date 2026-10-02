import json


def getConfig(config_file_path):
    with open(config_file_path, 'r') as file:
        config: dict = json.load(file)
    return config


def doctorFilePath() -> str:
    config = getConfig("Hospital_Management_Project/config.json")
    return config.get("doctor_filepath")  # config["doctor_filepath"]


def patientFilePath():
    config = getConfig("Hospital_Management_Project/config.json")
    return config.get("patient_filepath")


def loadDoctors():
    # with open(filepath,"mode") as file_object_name:
    with open(doctorFilePath(), "r") as file:
        doctors = file.read()
    doctors_list = doctors.split("\n")
    doctors_list = [doctor_list_element for doctor_list_element in doctors_list if len(
        doctor_list_element) > 2]
    return doctors_list


def findDoctors(id):
    from doctor_class import Doctor
    doctors = loadDoctors()
    for doctor in doctors:
        doctor_details = doctor.split(",")
        if int(doctor_details[0]) == id:
            return True
    return False


def saveToDoctorFile(doctor_full_list):
    with open(doctorFilePath(), "w") as file:
        for doctor in doctor_full_list:
            file.write(f"{doctor}\n")
    print("Written to file sucessfully.")
