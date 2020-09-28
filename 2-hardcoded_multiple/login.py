valid_users = {
    'marcemeister' : 'marcelo123',
    'vortaq' : 'holaquetal',
    'soymarcelo' : 'soymarceloXD'
}

def is_valid_credentials(user, password):
    for valid_user, valid_password in valid_users.items():
        if user == valid_user and password == valid_password:
            return True

    return False

if __name__ == "__main__":
    username = input("What is your username?: ")
    password = input("What is your password?: ")

    if is_valid_credentials(username, password):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
