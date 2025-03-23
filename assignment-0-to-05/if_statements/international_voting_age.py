def check_voting_eligibility(age: int) -> None:
    """
    Checks and prints whether the user can vote in the fictional countries
    based on their age.
    """
    # Define voting ages for each country
    voting_ages = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }

    # Check voting eligibility for each country
    for country, voting_age in voting_ages.items():
        if age >= voting_age:
            print(f"You can vote in {country} where the voting age is {voting_age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {voting_age}.")

# Get user input
user_age = int(input("How old are you? "))
check_voting_eligibility(user_age)
