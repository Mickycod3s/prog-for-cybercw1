#Michael McClay
#B01886622
#CourseWork 1 Security tool


#stores initial login credentials
correct_username = "admin"
correct_password = "password123"

#stores credentials for the login authentication feature
login_username = "student"
login_password = "student123"

#predefined password for the brute-force simulation
brute_force_password = "securepass"

#max number of attempts
max_brute_force_attempts = 5
max_login_attempts = 3



#function to handle initial authentication
def initial_authentication():

    print("Welcome to the Security Tool")

#ask the user for their username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

#check if the entered credentials match the correct ones
    if username == correct_username and password == correct_password:
        print("Login successful!")
        return True

#if the credentials are incorrect, inform the user and return False
    else:
        print("Incorrect username or password.")
        return False







#function to count correct and incorrect password entries
def security_event_counter():

#define the correct password and initialise counters for correct and incorrect entries
    correct_password = "password123"
    correct_count = 0
    incorrect_count = 0

#ask the user to enter the password 10 times and count the correct and incorrect entries
    for i in range(10):
        user_input = input("Enter the password: ")
        if user_input == correct_password:
            correct_count += 1
            print("Correct password entered.")
        else:
            incorrect_count += 1
            print("Incorrect password entered.")

#calculate the total attempts and the percentage of incorrect entries, then display the results
    total_attempts = correct_count + incorrect_count
    incorrect_percentage = (incorrect_count / total_attempts) * 100

#display the results of the password entry attempts
    print(f"Correct passwords entered: {correct_count}")
    print(f"Incorrect passwords entered: {incorrect_count}")
    print(f"Percentage of incorrect passwords: {incorrect_percentage:.2f}%")

#if more than 50% of the passwords entered were incorrect, display an alert message
    if incorrect_percentage > 50:
        print("ALERT: More than 50% of the passwords entered were incorrect!")







#function to simulate a brute-force attack by allowing the user to guess a predefined password
def brute_force_simulation():
    attempts = 0

#allow the user to guess the password up to a maximum number of attempts
    while attempts < max_brute_force_attempts:
        user_input = input("Enter the password guess: ")
        attempts += 1

#check if the guessed password matches the predefined password and provide feedback to the user
        if user_input == brute_force_password:
            print("Correct password entered!")
            break
        else:
            print(f"Incorrect password. Attempts left: {max_brute_force_attempts - attempts}")

#if the user reaches the maximum number of attempts without guessing the correct password, inform them that access is denied
    if attempts == max_brute_force_attempts:
        print("Maximum attempts reached. Access denied.")









#function to handle login authentication with a maximum number of attempts
def login_authentication():
    attempts = 0

#allow the user to enter their username and password up to a maximum number of attempts
    while attempts < max_login_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")
        attempts += 1

#check if the entered credentials match the predefined login credentials and provide feedback to the user
        if username == login_username and password == login_password:
            print("Authentication succeeded!")
            break
        else:
            print(f"Authentication failed. Attempts left: {max_login_attempts - attempts}")

#if the user reaches the maximum number of attempts without successfully authenticating, inform them that their account is frozen for 24 hours
    if attempts == max_login_attempts:
        print("Maximum failed logins reached. Account is frozen for 24 hours.")





#main function to run the security tool, providing a menu for the user to choose from different security features
def main():

    # Check the user's login credentials first
    if initial_authentication():

#while loop to display the security menu and handle user choices until they choose to exit
        while True:

            print("\nSECURITY MENU")
            print("1. Security Event Counter")
            print("2. Brute-Force Simulation")
            print("3. Login Authentication")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                security_event_counter()

            elif choice == "2":
                brute_force_simulation()

            elif choice == "3":
                login_authentication()

            elif choice == "4":
                print("Thank you for using the security tool")
                break

            else:
                print("Invalid choice. Please try again.")

    else:
        print("Access denied.")

##run the main function to start the security tool
main()