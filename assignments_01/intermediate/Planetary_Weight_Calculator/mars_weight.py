def main():
    # Prompt user for their weight on Earth
    earth_weight = float(input("Enter your weight on Earth (kg): "))
    
    # Mars gravity factor
    mars_weight = earth_weight * 0.378

    # Print the weight on Mars rounded to two decimal places
    print(f"Your weight on Mars would be: {round(mars_weight, 2)} kg")

if __name__ == "__main__":
    main()
