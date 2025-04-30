# Define a base class named Person
class Person:
    def __init__(self, name):
        self.name = name  # Store person's name

# Define a child class named Teacher that inherits from Person
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)     # Call the constructor of Person using super()
        self.subject = subject     # Store the subject taught by the teacher

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

# Create an object of Teacher class
t1 = Teacher("Ms. Sara", "Math")
t1.display()
