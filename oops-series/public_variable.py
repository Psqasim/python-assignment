# Define a class named Car
class Car:
    # Public variable
    brand = "Toyota"

    # Public method
    def start(self):
        print(self.brand, "is starting...")

# Create an object of Car class
my_car = Car()

# Accessing public variable from outside the class
print("Car Brand:", my_car.brand)

# Accessing public method from outside the class
my_car.start()
# This code defines a class named Car with a public variable 'brand' and a public method 'start'.
# An object of the Car class is created, and both the public variable and method are accessed from outside the class.
