import time, os

if __name__ == '__main__':
    to_do_list = []


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
            added_list = to_do_list.append(my_list)
            if added_list == to_do_list:
                print('This item has already been added')
                to_do_list.remove(my_list)
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
