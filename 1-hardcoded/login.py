valid_user = 'Marcemeister'
valid_password = 'marcelo123'

def is_valid_credentials(user, password):
    return (user == valid_user and password == valid_password)

if __name__ == "__main__":
    username = input("What is your username?: ")
    password = input("What is your password?: ")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
