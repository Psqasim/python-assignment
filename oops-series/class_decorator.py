# Define a class decorator that adds a greet() method
def add_greeting(cls):
    # Define a new method inside the decorator
    def greet(self):
        return "Hello from Decorator!"
    
    # Attach the new method to the class
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an object of Person and call greet()
p = Person("Qasim")
print(p.greet())  # Output: Hello from Decorator!
