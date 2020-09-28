import hashlib
import yaml

with open("credentials.yaml") as file:
    credentials = yaml.safe_load(file)

def is_valid_credentials(user, password):
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for cred in credentials:
        if cred["username"] == user and cred["password_hash"] == password:
            return True

    return False

if __name__ == "__main__":
    username = input("What is your username?: ")
    password = input("What is your password?: ")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
