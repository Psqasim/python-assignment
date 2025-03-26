def main():
    # Dictionary containing gravity conversion factors for each planet
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Prompt user for their weight on Earth
    earth_weight = float(input("Enter your weight on Earth (kg): "))

    # Prompt user for the planet name
    planet = input("Enter the name of a planet: ")

    # Calculate weight on the selected planet
    new_weight = earth_weight * planet_gravity[planet]

    # Print the equivalent weight rounded to 2 decimal places
    print(f"Your weight on {planet} would be: {round(new_weight, 2)} kg")

if __name__ == "__main__":
    main()
