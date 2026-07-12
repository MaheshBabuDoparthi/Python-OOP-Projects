# Project 8: College Management System (OOP)
# Author: Mahesh Babu Doparthi

class College:

    def __init__(self, name, roll_number, branch, marks):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Branch:", self.branch)
        print("Marks:", self.marks)

    def update_marks(self, marks):
        self.marks = marks
        print("Marks Updated Successfully!")
        print("Updated Marks:", self.marks)

    def change_branch(self, branch):
        self.branch = branch
        print("Branch Changed Successfully!")
        print("New Branch:", self.branch)

    def result(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 75:
            print("Grade B")
        elif self.marks >= 50:
            print("Grade C")
        else:
            print("Fail")

    def search_student(self, roll_number):
        if self.roll_number == roll_number:
            print("Student Found!")
        else:
            print("Student Not Found!")


# Creating Object

student1 = College("Mahesh", 27, "CSE-AI", 95)

print("========== STUDENT DETAILS ==========")
student1.show_details()

print("\n========== UPDATE MARKS ==========")
student1.update_marks(98)

print("\n========== CHANGE BRANCH ==========")
student1.change_branch("AI & Machine Learning")

print("\n========== RESULT ==========")
student1.result()

print("\n========== SEARCH STUDENT ==========")
student1.search_student(27)

print("\n========== UPDATED DETAILS ==========")
student1.show_details()