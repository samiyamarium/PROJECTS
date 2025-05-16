class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee: {self.name}, ID: {self.emp_id}"

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Department: {self.dept_name}")
        for emp in self.employees:
            print(emp.get_details())


e1 = Employee("sam", 90)
e2 = Employee("mary", 98)

dept = Department("Marketing")
dept.add_employee(e1)
dept.add_employee(e2)

dept.show_employees()
