import random
import string

def generate_password(length):
    if length < 1:
        return "Error! Password length must be at least 1."
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Combine all character sets
    all_chars = lower + upper + digits + special
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

# Run the password generator
if __name__ == "__main__":
    password_generator()
