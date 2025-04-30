# This code demonstrates the use of 'self' in a class to refer to instance variables and methods.
# 'self' is a reference to the current instance of the class and is used to access variables that belong to the class.
# Define a class named Student
class Student:
    # Constructor method to initialize name and marks using 'self'
    def __init__(self, name, marks):
        self.name = name      # 'self.name' stores the student's name
        self.marks = marks    # 'self.marks' stores the student's marks

    # Method to display student details
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Create an object of Student class and call display method
student1 = Student("Ali", 85)
student1.display()
# This will create a Student object with name "Ali" and marks 85, and then display the information.