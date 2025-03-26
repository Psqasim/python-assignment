def is_leap_year(year: int) -> bool:
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4
    - It is not divisible by 100 unless it is also divisible by 400

    Returns:
        bool: True if it is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Get user input
year = int(input("Enter a year: "))

# Check and print result
if is_leap_year(year):
    print("That's a leap year!")
else:
    print("That's not a leap year.")
