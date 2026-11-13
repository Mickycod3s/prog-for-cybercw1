#Michael McClay
#B01886622
#CourseWork 1 Reusable Cyber Security Utilities
#main program

# Import the Security_tools module
import Security_tools


#main function to run the Cyber Security Utilities program
def main():
    print("Welcome to Cyber Security Utilities")

# Prompt the user for a password and an IP address, and validate them using the Security_tools module
    try:
        password = input("Enter your password: ")

        ip_address = input("Enter an IP address: ")

        print("\npassword Validation:")

# Validate the password using the validate_password function from the Security_tools module
        if Security_tools.validate_password(password):
            print("Password is strong.")
        else:
            print("Password is weak. ")
            suggested_password = Security_tools.generate_password()

            print(f"Suggested strong password: {suggested_password}")

        print("\nIP Address Validation:")

# Validate the IP address using the validate_ip function from the Security_tools module
        if Security_tools.validate_ip(ip_address):
            print("IP address is valid.")
        else:
            print("IP address is invalid.")

#except block to handle EOFError and KeyboardInterrupt exceptions, allowing the user to stop the program gracefully
    except (EOFError, KeyboardInterrupt):
        print("\nProgram stopped by user.")

#main function to call the Cyber Security Utilities program
if __name__ == "__main__":
    main()