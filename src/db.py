# src/db.py
from pysqlcipher3 import dbapi2 as sqlcipher

def connect_db(db_path, key):
    conn = sqlcipher.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA key = '{key}';")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            service TEXT NOT NULL,
            encrypted_password TEXT NOT NULL
        )
    ''')
    return conn, cursor

def add_password(cursor, username, service, encrypted_password):
    cursor.execute('''
        INSERT INTO passwords (username, service, encrypted_password)
        VALUES (?, ?, ?)
    ''', (username, service, encrypted_password))

def get_password(cursor, service):
    cursor.execute('''
        SELECT encrypted_password FROM passwords WHERE service = ?
    ''', (service,))
    return cursor.fetchone()
