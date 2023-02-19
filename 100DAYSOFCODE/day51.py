import os
import time

if __name__ == '__main__':
    to_do_list = []

    try:
        f = open("to_do_list.txt", "r")
        to_do_list = eval(f.read())
        f.close()
    except Exception as err:
        print("Unable to load")
        print(err)


    def pretty_print():
        os.system('clear')
        print("ToDoList")
        for index in range(1, len(to_do_list)):
            print(f'{index}: {to_do_list[index]}')
            time.sleep(0.6)


    while True:
        menu = int(input("""
        1. view 
        2. add
        3. remove
        4. edit
        5. Erase
        6. exit\n
        """))

        if menu == 1:
            pretty_print()
        elif menu == 2:
            my_list = input('What do you want to add: ')
            if my_list not in to_do_list:
                to_do_list.append(my_list)
        elif menu == 3:
            my_list = input("remove item from list-> ")
            check = input("Are you sure you want to remove item from list(yes or no)-> ")
            if check == 'yes':
                to_do_list.remove(my_list)
            else:
                continue
        elif menu == 4:
            text = input('What do you want to edit-> ')
            edit_text = input("What do you want to change->")
            for i in range(0, len(to_do_list)):
                if to_do_list[i] == text:
                    to_do_list[i] = edit_text

        elif menu == 5:
            to_do_list.clear()

        elif menu == 6:
            exit()

        f = open("to_do_list.txt", "w")
        f.write(str(to_do_list))
        f.close()
