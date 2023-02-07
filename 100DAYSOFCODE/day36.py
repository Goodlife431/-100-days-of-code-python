if __name__ == '__main__':
    full_name = []


    def surname_name(first_name, last_name):
        surname = f"{first_name} {last_name}"
        if surname not in full_name:
            full_name.append(surname)
        for name in full_name:
            print(f"{name}")


    while True:
        first = str(input("Enter your first name-> ")).strip().capitalize()
        last = str(input("Enter your last name-> ")).strip().capitalize()
        surname_name(first, last)
        exit_function = int(input("press 5 to exit"))
        if exit_function == 5:
            exit()
        else:
            continue


