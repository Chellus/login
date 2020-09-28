import hashlib

valid_users = {
    'marcemeister' : 'db1f87649d1e48643b90bf5baa00b40249ce856b6f0a7fceacc28f1b520ff56c',
    'vortaq' : 'd06b4d89ddffb4f8e71bb22c2206651fd9f0afe2dd3a7f6d3cc262c0e8c7ccd6',
    'soymarcelo' : 'a7c43586cf8714e15e6f3d68355af111e60b5e5287d1a4308077443effb53cfe'
}

def is_valid_credentials(user, password):

    password = hashlib.sha256(password.encode('utf-8')).hexdigest()

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
