import hashlib

# Function to hash a password using SHA-256
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Dictionary storing email-password hashes (simulating stored login credentials)
stored_logins: dict[str, str] = {
    "user@example.com": hash_password("securepassword"),
    "test@domain.com": hash_password("mypassword123"),
    "admin@site.com": hash_password("adminpass")
}

# Function to check if the entered password matches the stored hash
def login(email: str, password_to_check: str) -> bool:
    """
    Checks if the provided email exists in stored_logins and 
    verifies if the hashed password matches the stored hash.
    """
    if email in stored_logins:  # Check if email exists in the dictionary
        return stored_logins[email] == hash_password(password_to_check)  # Compare hashed values
    return False  # Return False if email is not found

# Example usage
if __name__ == "__main__":
    # Taking user input
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")

    # Checking login credentials
    if login(user_email, user_password):
        print("Login successful!")
    else:
        print("Invalid email or password.")
