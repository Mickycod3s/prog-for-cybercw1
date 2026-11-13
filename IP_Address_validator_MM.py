#Michael McClay
#B01886622
#CourseWork 1 IP Address Validator





def validate_ip(ip):
    ip = ip.strip()  # Remove unnecessary spaces
    
    if "." not in ip:  # Check if the IP address contains periods/dots
        return False
    
    if ip.count(".") != 3:  # Check if it contains exactly three periods/dots
        return False
    
    parts = ip.split(".")  # Split the IP address into four parts
    
    if len(parts) != 4:  # Check that there are four parts
        return False

#for each part of the IP address, check if it is a valid number between 0 and 255
    for part in parts:

        if not part.isdigit():  # Check that the part contains only digits
            return False
        
        number = int(part)  # Convert the part to an integer
                              
        
        if number < 0 or number > 255:  # Check that the number is between 0 and 255
            return False

        
#return True  # If all checks pass, the IP address is valid
    return True






#main function to prompt the user for an IP address and validate it
def main():
    ip_address = input("Enter an IP address: ")

#validate the entered IP address and print whether it is valid or invalid
    if validate_ip(ip_address):
        print("Valid IP address")
    else:
        print("Invalid IP address")

#check if the script is being run directly and call the main function 
if __name__ == "__main__":
    main()
    
