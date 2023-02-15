import random
if __name__ == '__main__':
    bingo = []
    numbers = []
    def pretty_print():
        print()
        for row in bingo:
            print(f"-----------------------------------------")
            for item in row:
                print(f"{item:^10}", end=" | ")
            print()

    for i in range(8):
        numbers.append(random.randint(1, 90))
    numbers.sort()

    bingo = [[numbers[0], numbers[1], numbers[2]],
             [numbers[3], "BINGO", numbers[4]],
             [numbers[5], numbers[6], numbers[7]]
             ]

    def create_card():
        while True:
            pretty_print()
            user = int(input("Enter next number-> "))
            for row in range(3):
                for item in range(3):
                    if bingo[row][item] == user:
                        bingo[row][item] = "X"

            X = 0
            for row in bingo:
                for item in row:
                    if item == "X":
                        X += 1

            if X == 8:
                print("You have won the game")
    create_card()







