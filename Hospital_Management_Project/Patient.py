from hospitalPerson import HospitalPerson


class Patient(HospitalPerson):
    def __init__(self, id, name, age, gender, phone, illness, visit_date):
        super().__init__(id, name, age, gender, phone)
        self.illness = illness
        self.visit_date = visit_date
