import os
import sqlite3

DATABASE_NAME = "ppab6.db"

if __name__ == "__main__":
    if os.path.isfile(DATABASE_NAME):
        while True:
            ans = input("Database file %s already exists. Shall I overwrite it? [y/n]" % DATABASE_NAME)

            if ans == "y":
                print("OK. Deleting database and recreating it")
                os.remove(DATABASE_NAME)
                break
            elif ans == "n":
                print("OK. Exiting")
                exit(0)
            else:
                print("I didn't understand you")

    conn = sqlite3.connect('ppab6.db')
    c = conn.cursor()

    c.execute("""
        CREATE TABLE users (
            username VARCHAR,
            password_hash VARCHAR
        )
    """)
    conn.commit()

    print("Database created!")
