import hashlib
import sqlite3
from getpass import getpass

DATABASE_NAME = "ppab6.db"

def is_username_available(username):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    res = c.execute("""
        SELECT *
        FROM users
        WHERE username = ?
    """, (username,)).fetchone()

    return res is None

def add_user(username, password):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO users
        VALUES (?, ?)
    """, (username, password))
    conn.commit()

if __name__ == "__main__":
    while True:
        username = input("What's going to be your username?: ")
        if is_username_available(username):
            print("Username is available!\n")
            break
        else:
            print("Username is taken, please choose another one.")


    password = getpass("What's going to be your password?: ")

    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    add_user(username, password)

    print("Added %s to the database!" % username)
