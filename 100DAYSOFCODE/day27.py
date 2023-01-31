import random, os, time

if __name__ == '__main__':
    def roll_dice(side):
        result = random.randint(1, side)
        return result


    def health_status():
        health = ((roll_dice(6) * roll_dice(12) / 2) + 10)
        return health


    def strength_status():
        strength = ((roll_dice(6) * roll_dice(12) / 2) + 12)
        return strength

    while True:
        print('Character Builder')
        print()
        character_name = str(input('Name your Legend-> '))
        print()
        character_type = str(input('Character Type (Human, Elf, Wiard, Orc)-> '))

        print(f'{character_name}')
        print(f'{character_type}')
        print(f'HEALTH-> {health_status()}')
        print(f'STRENGTH-> {strength_status()}')
        print()
        time.sleep(2)
        os.system('clear')
        print('May your name go down in Legend...')

        generate_new_character = str(input('Do you want to generate new character yes or no-> '))
        if generate_new_character == 'no' or generate_new_character == 'No':
            break
        elif generate_new_character == 'yes' or generate_new_character == 'Yes':
            continue
        else:
            print('Choose an option yes or no')




