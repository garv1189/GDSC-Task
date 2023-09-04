import random
import string

def generate_password(length=12, include_special_chars=True):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation if include_special_chars else ""

    if length < 6:
        print("Password length is too short for any complexity level.")
        return None
    elif length < 8:
        charset = lowercase_letters + uppercase_letters + digits
    elif length < 12:
        charset = lowercase_letters + uppercase_letters + digits + special_characters
    else:
        charset = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate the password by randomly selecting characters from the charset
    password = ''.join(random.choice(charset) for _ in range(length))

    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        include_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

        password = generate_password(length, include_special_chars)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid password length as a number.")

