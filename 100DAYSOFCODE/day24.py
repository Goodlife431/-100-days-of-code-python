import random
if __name__ == '__main__':
    def roll_dice(dice):
        while True:
            dice = random.randint(1, 1000)
            print(f'You rolled {dice}')
            roll = str(input('Roll again? '))
            if roll == 'yes':
                roll_dice(dice)
                print(f'You rolled {dice}')
            elif roll == 'no':
                break


    roll_dice(dice=int(input('How many sides?: ')))