import os, time, random
from replit import db


def createUser():
    time.sleep(1)
    os.system("clear")
    username = input("Username: ")
    password = input("password: ")
    keys = db.keys()
    if username in keys:
        print("ERROR: Username exists")
        return

    salt = random.randint(1000, 9999)
    newPassword = f"{password} {salt}"
    newPassword = hash(newPassword)

    db[username] = {"password": newPassword, "salt": salt}
    print("User added")


def login():
    time.sleep(1)
    os.system("clear")
    username = input("Username: ")
    password = input("Password: ")
    key_s = db.keys()
    if username not in key_s:
        print('ERROR: User does not exist')
        return

    salt = db[username]["salt"]
    newPassword = f"{password} {salt}"
    newPassword = hash(newPassword)

    if db[username]["password"] == newPassword:
        print("LOgged in")
    else:
        print("Username or password incorrect ")


while True:
    menu = int(input(f"""1: New User
    2: Login: """))
    if menu == 1:
        createUser()
    elif menu == 2:
        login()
    else:
        key_s = db.keys()
        for key in key_s:
            print(db[key])

