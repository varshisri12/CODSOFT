import random
import string

def generate_password(length):
    # Define the character sets to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password using random choices from the character sets
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate the password
    password = generate_password(length)
    # Display the password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
