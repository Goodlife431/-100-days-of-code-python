if __name__ == '__main__':
    Inventory = []

    try:
        f = open("Inventory.txt", "r")
        Inventory = eval(f.read())
        f.close()
    except Exception as err:
        print("Error loading file")
        print(err)


    def add_inventory():
        while True:
            add_item = input("Enter Inventory you want to add-> ").strip().capitalize()
            Inventory.append(add_item)
            print()
            fl = open("Inventory.txt", "w")
            fl.write(str(Inventory))
            fl.close()
            print()
            print(f"{add_item} has been added to your inventory")
            another = input("Do you want make another inventory y/n -> ")
            if another == 'y':
                continue
            else:
                break


    def remove_inventory():
        find = input("What inventory do you want to remove-> ").strip().capitalize()
        if find in Inventory:
            Inventory.remove(find)
        print(f"{find} has been removed from your inventory")


    def view_inventory():
        view_item = input("Input item you want to view-> ").capitalize()
        if view_item in Inventory:
            print(f"You have {Inventory.count(view_item)} {view_item} ")


    while True:
        menu = int(input("""
        1. Add
        2. View
        3. Remove
        4. Exit
        """))
        if menu == 1:
            add_inventory()
        elif menu == 2:
            view_inventory()
        elif menu == 3:
            remove_inventory()
        elif menu == 4:
            exit()
