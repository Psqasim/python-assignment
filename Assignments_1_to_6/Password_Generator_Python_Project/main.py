import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        num_passwords = int(input("🔢 Enter the number of passwords to generate: "))
        password_length = int(input("🔐 Enter the password length: "))

        print("\n🛡️ Here are your secure passwords:\n")
        for i in range(num_passwords):
            print(f"🔑 Password {i+1}: {generate_password(password_length)}")

    except ValueError:
        print("⚠️ Please enter valid numbers!")

if __name__ == "__main__":
    main()
