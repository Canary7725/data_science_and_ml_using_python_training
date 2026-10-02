from hospitalPerson import HospitalPerson
from utils import doctorFilePath, loadDoctors, saveToDoctorFile


class Doctor(HospitalPerson):
    def __init__(self, id, name, age, gender, phone, specialization, type):
        super().__init__(id, name, age, gender, phone)
        self.specialization = specialization
        self.type = type

    def insertDoctor(self):
        try:
            with open(doctorFilePath(), "a") as file:
                file.write(
                    f"{self.id},{self.name},{self.age},{self.gender},{self.phone},{self.specialization},{self.type}\n")
            print(f"Doctor saved successfully at file {doctorFilePath()}")
        except Exception as e:
            print(f"Something went wrong {e}")

    def updateDoctor(self, id):
        doctors = loadDoctors()
        try:
            for i in range(len(doctors)):
                if id == int(doctors[i].split(",")[0]):
                    doctors[i] = f"{self.id},{self.name},{self.age},{self.gender},{self.phone},{self.specialization},{self.type}\n"
                    break
            saveToDoctorFile(doctors)
        except Exception as e:
            print(f"Something went wrong: {e}")


def displayAllDoctors():
    doctors = loadDoctors()
    print("---------------------------------Doctors-------------------------------------------------")
    for doctor in doctors:
        doctor_details = doctor.split(",")
        print(f"""
    id\tname\tage\tgender\tphone\t\tspecialization\ttype
    {doctor_details[0]}\t{doctor_details[1]}\t{doctor_details[2]}\t{doctor_details[3]}\t{doctor_details[4]}\t{doctor_details[5]}\t\t{doctor_details[6]}
    """)
    print(
        "----------------------------------------------------------------------------------------------")


def displayOneDoctor(id):
    doctors = loadDoctors()
    for doctor in doctors:
        doctor_details = doctor.split(",")
        if int(doctor_details[0]) == id:
            print(f"""
        id\tname\t\tage\tgender\tphone\t\tspecialization\ttype
        {doctor_details[0]}\t{doctor_details[1]}\t{doctor_details[2]}\t{doctor_details[3]}\t{doctor_details[4]}\t{doctor_details[5]}\t\t{doctor_details[6]}
        """)


def deleteDoctor(id):
    doctors = loadDoctors()
    updated_doctors = []
    for doctor in doctors:
        if (id == int(doctor.split(",")[0])):
            continue
        updated_doctors.append(doctor)
    print(updated_doctors)
    saveToDoctorFile(updated_doctors)
