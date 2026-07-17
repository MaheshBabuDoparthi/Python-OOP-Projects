class Employee:

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

    def update_salary(self, salary):
        self.salary = salary
        print("Salary Updated Successfully!")
        print("Updated Salary:", self.salary)

    def annual_salary(self):
        annual_salary = self.salary * 12
        print("Annual Salary:", annual_salary)

    def remove_employee(self):
        print("Employee Removed Successfully!")


employees = []

while True:

    print("\n===== Employee Payroll Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Salary")
    print("4. Calculate Annual Salary")
    print("5. Remove Employee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        name = input("Enter Employee Name: ")
        employee_id = int(input("Enter Employee ID: "))
        salary = float(input("Enter Monthly Salary: "))

        employee = Employee(name, employee_id, salary)
        employees.append(employee)

        print("Employee Added Successfully!")

    elif choice == 2:

        if len(employees) == 0:
            print("No Employees Found!")
        else:
            for employee in employees:
                employee.show_details()
                print("----------------------")

    elif choice == 3:

        emp_id = int(input("Enter Employee ID: "))

        for employee in employees:
            if employee.employee_id == emp_id:
                salary = float(input("Enter New Salary: "))
                employee.update_salary(salary)
                break
        else:
            print("Employee Not Found!")

    elif choice == 4:

        emp_id = int(input("Enter Employee ID: "))

        for employee in employees:
            if employee.employee_id == emp_id:
                employee.annual_salary()
                break
        else:
            print("Employee Not Found!")

    elif choice == 5:

        emp_id = int(input("Enter Employee ID: "))

        for employee in employees:
            if employee.employee_id == emp_id:
                employee.remove_employee()
                employees.remove(employee)
                break
        else:
            print("Employee Not Found!")

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")