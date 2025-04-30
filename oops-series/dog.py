# Define a class named Dog
class Dog:
    def __init__(self, name, breed):
        self.name = name     # Instance variable for dog's name
        self.breed = breed   # Instance variable for dog's breed

    # Instance method that uses 'self' to access instance data
    def bark(self):
        print(f"{self.name} says: Woof woof!")

# Create an object of Dog class and call bark method
dog1 = Dog("Buddy", "Labrador")
dog1.bark()
# This will create a Dog object with name "Buddy" and breed "Labrador", and then call the bark method which prints the dog's bark.
# This code demonstrates the use of 'self' in a class to refer to instance variables and methods.