# Project 2: Student Management System (OOP)
# Author: Mahesh Babu Doparthi

class Student:

    def __init__(self, name, roll, branch, marks):
        self.name = name
        self.roll = roll
        self.branch = branch
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Branch:", self.branch)
        print("Marks:", self.marks)

    def update_marks(self, marks):
        self.marks = marks
        print("Updated Marks:", self.marks)

    def update_branch(self, branch):
        self.branch = branch
        print("Branch Updated:", self.branch)

    def percentage(self):
        print(f"Percentage: {self.marks}%")

    def result(self):
        if self.marks >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

    def is_topper(self):
        if self.marks >= 90:
            print("Topper")
        else:
            print("Keep Working")

    def greet(self):
        print(f"Hello {self.name}! Welcome to {self.branch}")


# Creating Objects

student1 = Student("Mahesh", 27, "CSE-AI", 95)
student2 = Student("Rahul", 15, "CSE", 65)

print("========== Student 1 ==========")
student1.greet()
student1.show_details()
student1.result()
student1.is_topper()
student1.percentage()

print("\n========== Student 2 ==========")
student2.greet()
student2.show_details()
student2.result()
student2.is_topper()
student2.percentage()

print("\n========== Updating Student 2 ==========")
student2.update_marks(90)
student2.update_branch("CSE-DS")
student2.show_details()
student2.result()
student2.is_topper()
student2.percentage()