# src/encryption.py
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()
