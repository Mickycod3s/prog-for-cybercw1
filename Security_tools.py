 #Michael McClay
#B01886622
#CourseWork 1 Reusable Cyber Security Utilities

# Import required modules
import random
import string


# Function to validate the strength of a password based on length and characters
def validate_password(password):

    # Check if the password length is less than 8 characters
    if len(password) < 8:
        return False

    # Check if the password contains at least one letter, one digit and one symbol
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    # Return True if the password meets all criteria, otherwise return False
    return bool(has_letter and has_digit and has_symbol)


# Function to validate an IP address
def validate_ip(ip_address):

    # Remove unnecessary spaces
    ip = ip_address.strip()

    # Check if the IP address contains periods/dots
    if "." not in ip:
        return False

    # Check if it contains exactly three periods/dots
    if ip.count(".") != 3:
        return False

    # Split the IP address into four parts
    parts = ip.split(".")

    # Check if there are four numbers in the IP address
    if len(parts) != 4:
        return False

    # Check each part of the IP address
    for part in parts:

        # Check that each part contains only digits
        if not part.isdigit():
            return False

        # Convert the part to an integer
        number = int(part)

        # Check that the number is between 0 and 255
        if number < 0 or number > 255:
            return False

    # Return True if all checks pass
    return True


# Function to generate a strong random password
# Password length will be between 10 and 16 characters
def generate_password():

    # Randomly choose a password length between 10 and 16
    password_length = random.randint(10, 16)

    # Define the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Select at least one character from each character set
    password_characters = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + symbols

    # Add random characters until the desired password length is reached
    for i in range(password_length - 4):
        password_characters.append(random.choice(all_characters))

    # Shuffle the password characters into a random order
    random.shuffle(password_characters)

    # Join the characters into a single password
    strong_password = "".join(password_characters)

    return strong_password