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
        return dice


    def roll_dice2(dice1, dice2):
        import random
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 8)
        health_status = dice1 * dice2
        return health_status


    # roll_dice(dice=int(input('How many sides?: ')))
    while True:
        name = str(input('Name your warrior->'))
        print(f'your health is-> {roll_dice2(2,3)}hp')
        print()
        question = input('Do you want to generate health stats for another character->')
        if question == 'yes':
            continue
        elif question == 'no':
            break

