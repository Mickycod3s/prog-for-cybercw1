#Michael McClay
#B01886622
#CourseWork 1 Security Incident Manager

security_incident = {
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event_type": "unsuccesful login",
    "risk_level": "low"
}   


def security_incident_manager():

    print("Welcome to the Security Incident Manager")

    print("\n--Security Incident Details--:")
    print(f"Username: {security_incident['username']}")
    print(f"IP Address: {security_incident['ip_address']}")

    security_incident["status"] = "under investigation"

    print("\nStatus field added unsuccessfully.")

    security_incident["risk_level"] = "Critical"

    print("\nRisk level updated successfully.")

    security_incident.pop("event_type")

    print("\nEvent type field removed successfully.")

    print("\nupdated Security Incident Details:")

    for key, value in security_incident.items():
        print(f"{key}: {value}")

    total_fields = len(security_incident)
    print(f"\nTotal number of key-value pairs: {total_fields}")

    print("\nSecurity Incident Manager completed.")

try:
    security_incident_manager()

except (KeyError, TypeError) as error:
    print(f"An error occurred:, error")
