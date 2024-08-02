# src/gui.py
import tkinter as tk
from tkinter import simpledialog, messagebox
from src.auth import hash_password, verify_password
from src.encryption import generate_key, encrypt_password, decrypt_password
from src.db import connect_db, add_password, get_password

class PasswordManagerApp:
    def __init__(self, db_path, key):
        self.db_path = db_path
        self.key = key
        self.encryption_key = None
        self.conn, self.cursor = connect_db(db_path, key)
        self.root = tk.Tk()
        self.root.title("Password Manager")
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.root, text="Add Password", command=self.add_password).pack(pady=10)
        tk.Button(self.root, text="Retrieve Password", command=self.retrieve_password).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def add_password(self):
        username = simpledialog.askstring("Input", "Enter username:")
        service = simpledialog.askstring("Input", "Enter service:")
        service_password = simpledialog.askstring("Input", "Enter password:")

        if username and service and service_password:
            self.encryption_key = generate_key()
            encrypted_service_password = encrypt_password(self.encryption_key, service_password)
            add_password(self.cursor, username, service, encrypted_service_password)
            self.conn.commit()
            messagebox.showinfo("Success", f"Password for {service} added successfully.\nEncryption key: {self.encryption_key.decode()}")

    def retrieve_password(self):
        service = simpledialog.askstring("Input", "Enter the service name:")
        encryption_key = simpledialog.askstring("Input", "Enter the encryption key:")

        if service and encryption_key:
            encrypted_password = get_password(self.cursor, service)
            if encrypted_password:
                decrypted_password = decrypt_password(encryption_key.encode(), encrypted_password[0])
                messagebox.showinfo("Password Retrieved", f"The password for {service} is: {decrypted_password}")
            else:
                messagebox.showerror("Error", f"No password found for {service}.")

    def run(self):
        self.root.mainloop()

    def __del__(self):
        self.conn.close()

