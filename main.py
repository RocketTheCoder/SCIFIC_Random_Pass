import random

def generate_password(length):
    """Generates a random password of the given length"""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def save_password(account, password):
    """Saves the account name and password to a file"""
    with open("passwords.txt", "a") as f:
        f.write(f"{account}: {password}\n")

def main():
    # Ask the user for the account name and password length
    account = input("Enter the account name: ")
    length = int(input("Enter the password length: "))

    # Generate a random password and save it to a file
    password = generate_password(length)
    save_password(account, password)

    # Display the password to the user
    print(f"Password for {account}: {password}")

if __name__ == "__main__":
    main()
