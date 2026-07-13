# Project 9: Student Record Management System
# Author: Mahesh Babu Doparthi

class Student:

    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch


students = []

while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Name: ")
        roll_number = int(input("Enter Roll Number: "))
        branch = input("Enter Branch: ")

        student = Student(name, roll_number, branch)
        students.append(student)

        print("Student Added Successfully!")

    elif choice == 2:

        if len(students) == 0:
            print("No Students Found!")
        else:
            print("\n------ Student List ------")
            for student in students:
                print("Name:", student.name)
                print("Roll Number:", student.roll_number)
                print("Branch:", student.branch)
                print("--------------------------")

    elif choice == 3:

        roll_number = int(input("Enter Roll Number: "))
        found = False

        for student in students:
            if student.roll_number == roll_number:
                print("\nStudent Found!")
                print("Name:", student.name)
                print("Roll Number:", student.roll_number)
                print("Branch:", student.branch)
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == 4:

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")