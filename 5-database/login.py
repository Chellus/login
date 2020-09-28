import hashlib
import sqlite3
from getpass import getpass

DATABASE_NAME = "ppab6.db"

def is_valid_credentials(user, password):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    res = c.execute("""
        SELECT *
        FROM users
        WHERE username = ? AND password_hash = ?
    """, (user, password)).fetchone()

    return res is None

if __name__ == "__main__":
    username = input("What is your username?: ")
    password = getpass("What's going to be your password?: ")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
