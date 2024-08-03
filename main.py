# main.py
import os
from src.auth import hash_password, verify_password
from src.encryption import generate_key, encrypt_password, decrypt_password
from src.db import connect_db, add_password, get_password
from src.interface import display_menu, get_user_choice, get_password_details, get_service_name, display_password

def main():
    db_path = 'db/passwords.db'
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    key = 'your_secure_key'  # This should be securely managed

    # Connect to the database
    conn, cursor = connect_db(db_path, key)

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            # Add a password
            username, service, service_password = get_password_details()
            encryption_key = generate_key()
            encrypted_service_password = encrypt_password(encryption_key, service_password)
            add_password(cursor, username, service, encrypted_service_password)
            conn.commit()
            print(f"Password for {service} added successfully.")
            print(f"Encryption key: {encryption_key.decode()}")  # Display the encryption key for the user

        elif choice == '2':
            # Retrieve a password
            service = get_service_name()
            encryption_key = input("Enter the encryption key: ").encode()  # Get the encryption key from the user
            encrypted_password = get_password(cursor, service)
            if encrypted_password:
                decrypted_password = decrypt_password(encryption_key, encrypted_password[0])
                display_password(service, decrypted_password)
            else:
                print(f"No password found for {service}.")

        elif choice == '3':
            # Exit the program
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

from src.gui import PasswordManagerApp

def main():
    db_path = 'db/passwords.db'
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    key = 'your_secure_key'  # This should be securely managed

    app = PasswordManagerApp(db_path, key)
    app.run()


if __name__ == '__main__':
    main()

