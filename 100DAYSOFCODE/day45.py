import os
import time

if __name__ == '__main__':
    to_do_list = []
    def add():
        my_task = input('What is the task-> ')
        my_date = input("When is it due by-> ")
        my_priority = input("What is the priority-> ").strip().lower()
        row = [my_task, my_date,my_priority]
        to_do_list.append(row)
        print("Thanks, this task has been added.")

    def view():
        os.system('clear')
        print("View")
        my_view = int(input(f"""
        1: View All
        2: View priority
        """))
        if my_view == 1:
            for row in to_do_list:
                for item in to_do_list:
                    print(item, end= " | ")
        elif my_view == 2:
            priority = input("What priority-> ")
            for row in to_do_list:
                if priority in row:
                    for item in row:
                        print(item, end=" | ")
                        print()
                    print()
                    time.sleep(1)

    def edit():
        time.sleep(1)
        os.system("clear")
        find = input("Name of todo to edit > ")
        found = False
        for row in todo:
            if find in row:
                found = True
        if not found:
            print("Couldn't find that")
            return
        for row in todo:
            if find in row:
                to_do_list.remove(row)
        name = input("Name > ")
        date = input("Due Date > ")
        priority = input("Priority > ").capitalize()
        row = [name, date, priority]
        to_do_list.append(row)
        print("Added")


    def remove():
        time.sleep(1)
        os.system("clear")
        find = input("What todo do you want to remove")
        for row in to_do_list:
            if find in row:
                to_do_list.remove(row)


    while True:
        menu = int(input("""
        1. add 
        2. view
        3. remove
        4. edit
        5. Erase
        6. exit\n
        """))

        if menu == 1:
            add()
        elif menu == 2:
            view()
        elif menu == 3:
            remove()
        elif menu == 4:
            edit()
        elif menu == 5:
            to_do_list.clear()
        elif menu == 6:
            exit()

