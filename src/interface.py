# src/interface.py

def display_menu():
    print("Password Manager")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Exit")

def get_user_choice():
    return input("Enter your choice: ")

def get_password_details():
    username = input("Enter username: ")
    service = input("Enter service: ")
    password = input("Enter password: ")
    return username, service, password

def get_service_name():
    return input("Enter the service name: ")

def display_password(service, password):
    print(f"The password for {service} is: {password}")
