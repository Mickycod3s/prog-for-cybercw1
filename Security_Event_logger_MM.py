#Michael McClay
#B01886622
#CourseWork 1 Security tool

#importing the datetime module to get the current date and time for logging events
from datetime import datetime

#predefined correct username and password for authentication
correct_username = "admin"
correct_password = "password123"

#predefined IP address for logging purposes
ip_address = "192.168.1.25"

#initial event ID for logging events
event_id = 3971

#function to log security events based on user authentication attempts
def security_event_logger():

#global variable to keep track of the event ID across function calls
    global event_id

    print("Welcome to the Security Event Logger")

#while loop to continuously prompt the user for username and password until successful login or exit
    while True:
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

#getting the current timestamp for logging purposes
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#checking if the entered username and password match the predefined correct credentials
            if username == correct_username and password == correct_password:
                event = "Successful login"
                print("Login successful!")

#if the credentials do not match, log a failed login event
            else:
                event = "Failed login"
                print("\n Login failed. invalid username or password.")
               

#printing the event log details including event ID, username, IP address, event type, and timestamp
            print("\n--EVENT LOG--:")
            print(f"Event ID: {event_id}")
            print(f"Username: {username}")
            print(f"IP Address: {ip_address}")
            print(f"Event: {event}")
            print(f"Timestamp: {timestamp}")

#incrementing the event ID for the next event log entry
            event_id += 1

#checking if the event was a successful login to break the loop, otherwise prompting the user to try again
            if event == "Successful login":
                print("You have successfully logged in.")
                break
#else statement to handle failed login attempts and prompt the user to try again
            else:
                print("Please try again.\n")

#handling exceptions for keyboard interrupt or end-of-file error to exit the program
        except (KeyboardInterrupt, EOFError):
            print("\nExiting the Security Event Logger.")
            break

#calling the security_event_logger function to start the program
security_event_logger()