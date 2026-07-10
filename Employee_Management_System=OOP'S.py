# Project 5: Employee Management System (OOP)
# Author: Mahesh Babu Doparthi

class Employee:

    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def show_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Salary:", self.salary)

    def update_salary(self, salary):
        self.salary = salary
        print("Salary Updated Successfully!")
        print("New Salary:", self.salary)

    def bonus(self, amount):
        self.salary += amount
        print("Bonus Added Successfully!")
        print("Updated Salary:", self.salary)

    def change_department(self, department):
        self.department = department
        print("Department Changed Successfully!")
        print("New Department:", self.department)


# Creating Object

employee1 = Employee("Mahesh", 101, "CSE-AI", 40000)

print("========== EMPLOYEE DETAILS ==========")
employee1.show_details()

print("\n========== UPDATE SALARY ==========")
employee1.update_salary(50000)

print("\n========== BONUS ==========")
employee1.bonus(5000)

print("\n========== CHANGE DEPARTMENT ==========")
employee1.change_department("AI & Data Science")

print("\n========== UPDATED DETAILS ==========")
employee1.show_details()