import time, os
if __name__ == '__main__':
    pizza = []

    try:
        f = open("pizza.txt", "r")
        pizza = eval(f.read())
        f.close()
    except Exception as err:
        print("Unable to load")
        print(err)

    def add_pizza():
        while True:
            print("🌟Dave's Dodgy Pizzas🌟")
            print()
            quantity = input("How many pizzas?-> ")
            try:
                value = int(quantity)
            except ValueError:
                print("Please Enter a valid Number")
                continue
            size = input("What size?-> ").lower()
            total = 0
            if size == 's':
                cost = 5.99
            elif size == 'm':
                cost = 9.99
            else:
                cost = 14.99
                total = cost * float(quantity)
                total = round(total, 2)
            name = input("Name please-> ")
            topping = input("Enter toppings-> ")
            row = [name, topping, size, quantity, total]
            pizza.append(row)
            print(f"Thanks {name} your pizza will cost {cost}")
            print()

            fl = open("pizza.txt", "a+")
            fl.write(str(pizza))
            fl.close()
            time.sleep(0.10)
            another = input("Do you want make another order y/n -> ")
            if another == 'y':
                continue
            else:
                break


    def pretty_print():
        os.system("clear")
        h1 = "Name"
        h2 = "Toppings"
        h3 = "Size"
        h4 = "Quantity"
        h5 = "Total"
        print(f"{h1:^10} {h2:^10} {h3:^10} {h4:^10} {h5:^10}")
        for row in pizza:
            print(f"{row[0]:^10} {row[1]:^10} {row[2]:^10} {row[3]:^10} {row[4]:^10}")
        time.sleep(1)
    while True:
        menu = int(input(f"""
        1. Add pizza
        2. View pizza
        3. exit
        """))
        if menu == 1:
            add_pizza()
        elif menu == 2:
            pretty_print()
        else:
            exit()


