import random
if __name__ == '__main__':
    bingo = []
    numbers = []
    def pretty_print():
        for value in bingo:
            print(
                f"""|--------------------|
        | {value} |
        |____________________|""")

    for i in range(8):
        numbers.append(random.randint(1, 90))
    numbers.sort()

    bingo = [[numbers[0], numbers[1], numbers[2]],
             [numbers[3], "BINGO", numbers[4]],
             [numbers[5], numbers[6], numbers[7]]
             ]

    pretty_print()




    
