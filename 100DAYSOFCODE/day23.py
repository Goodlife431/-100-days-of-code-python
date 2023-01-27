if __name__ == '__main__':
    def validate():
        username = str(input('Enter username-> '))
        password = int(input('Enter password-> '))
        print('username and password has been saved')

        while True:
            username_validate = str(input('Enter your username to login-> '))
            password_validate = int(input('Enter your password to login-> '))
            if password == password_validate and username == username_validate:
                print('WELCOME TO REPLIT')
                break
            if password != password_validate or username != username_validate:
                print('Opps! I dont recognise the username or password, Try again')
                continue

    validate()