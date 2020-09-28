import hashlib
import yaml

with open("credentials.yaml") as file:
    credentials = yaml.safe_load(file)

def is_valid_credentials(user, password):
    user_stored_creds = None

    for cred in credentials:
        if cred["username"] == user:
            user_stored_creds = cred
            break

    if user_stored_creds is None:
        return False

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return user_stored_creds["password_hash"] == password

if __name__ == "__main__":
    username = input("What is your username?: ")
    password = input("What is your password?: ")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
