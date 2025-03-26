import random

def main():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(10):
        print(random.randint(1, 100), end=" ")
    print()  # Move to the next line after printing numbers

if __name__ == '__main__':
    main()
