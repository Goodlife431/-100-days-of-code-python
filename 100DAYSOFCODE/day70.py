import os

admin_username = os.environ['admin_user']
normal_username = os.environ['normal_user']
admin_password = os.environ['admin']
normal_password = os.environ['normal']

username = input("Enter admin username: ")
password = input("Enter admin password: ")

if username == admin_username and password == admin_password:
    print("welcome Amin")
else:
    print("Better luck next time")

norm_username = input("Enter normal username: ")
norm_password = input("Enter normal password: ")

if norm_username == normal_username and norm_password == normal_password:
    print("Welcome normal ")
else:
    print("Better luck next time")
