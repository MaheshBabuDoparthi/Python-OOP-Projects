# Project 6: Hospital Management System (OOP)
# Author: Mahesh Babu Doparthi

class Hospital:

    def __init__(self, patient_name, patient_id, disease, doctor):
        self.patient_name = patient_name
        self.patient_id = patient_id
        self.disease = disease
        self.doctor = doctor

    def show_details(self):
        print("Patient Name:", self.patient_name)
        print("Patient ID:", self.patient_id)
        print("Disease:", self.disease)
        print("Doctor:", self.doctor)

    def change_doctor(self, doctor):
        self.doctor = doctor
        print("Doctor Changed Successfully!")
        print("New Doctor:", self.doctor)

    def update_disease(self, disease):
        self.disease = disease
        print("Disease Updated Successfully!")
        print("New Disease:", self.disease)

    def check_patient(self, patient_id):
        if self.patient_id == patient_id:
            print("Patient Found!")
        else:
            print("Patient Not Found!")


# Creating Object

patient1 = Hospital("Mahesh", 101, "Fever", "Dr. Ramesh")

print("========== PATIENT DETAILS ==========")
patient1.show_details()

print("\n========== CHANGE DOCTOR ==========")
patient1.change_doctor("Dr. Suresh")

print("\n========== UPDATE DISEASE ==========")
patient1.update_disease("Viral Fever")

print("\n========== CHECK PATIENT ==========")
patient1.check_patient(101)

print("\n========== UPDATED DETAILS ==========")
patient1.show_details()