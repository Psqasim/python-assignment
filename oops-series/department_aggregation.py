# Define the Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

# Define the Department class that uses aggregation
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Store reference to an independent Employee object

    def show_details(self):
        print(f"Department: {self.department_name}")
        self.employee.show()  # Access Employee's method

# Create an Employee object
emp = Employee("Qasim")

# Pass the Employee object to the Department
dept = Department("HR", emp)

# Show department and employee info
dept.show_details()
