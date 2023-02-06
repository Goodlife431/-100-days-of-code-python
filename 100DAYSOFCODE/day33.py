import os, time
if __name__ == '__main__':
    print('ToDo List Manager')
    myPartyList = []


    def printList():
        print()
        for i in myPartyList:
            print(i)
            time.sleep(1)
            os.system('clear')
        print()


    while True:
        menu = input("Do you want to view, add, edit or exit?: ")
        if menu == 'view':
            printList()
        if menu == "add":
            item = input("Who should I add to the ToDo List Manger?: ")
            myPartyList.append(item)
            time.sleep(1)
            os.system('clear')
        elif menu == 'exit':
            exit()
        elif menu == "edit":
            item = input("Who should I remove from the ToDo List Manger?: ")
            if item in myPartyList:
                myPartyList.remove(item)
            else:
                print(f"{item} was not in the list")
        printList()

