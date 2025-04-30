# Define a class named MathUtils
class MathUtils:
    # Static method that adds two numbers
    @staticmethod
    def add(a, b):
        return a + b

# Call the static method without creating an object
result = MathUtils.add(5, 7)
print("Sum is:", result)
# This code defines a class named MathUtils with a static method 'add' that adds two numbers.
# The static method is called without creating an object of the class, demonstrating how to use static methods in Python.
