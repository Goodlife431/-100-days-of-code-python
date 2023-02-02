if __name__ == '__main__':
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

        print('Character Builder')
        print()
        character_one_name = str(input('Name your Legend-> '))
        character_type = str(input('Character Type (Human, Elf, Wiard, Orc)-> '))
        print()
        player_one_health = health_status()
        player_one_strength = strength_status()
        print(f'{character_one_name}')
        print(f'HEALTH-> {health_status()}')
        print(f'STRENGTH-> {strength_status()}')

        print('Who are they battling? ')
        print()
        character_two_name = str(input('Name your Legend-> '))
        character_two_type = str(input('Character Type (Human, Elf, Wiard, Orc)-> '))
        print()
        player_two_health = health_status()
        player_two_strength = strength_status()
        print(f'{character_two_name}')
        print(f'{character_two_type}')
        print(f'HEALTH-> {health_status()}')
        print(f'STRENGTH-> {strength_status()}')
        print()
        winner = None
        count = 0
        count1 = 0
        count2 = 0
        while True:
            time.sleep(1)
            os.system('clear')
            print()
            print('⚔️ BATTLE TIME ⚔️')
            print()
            player_one = roll_dice(6)
            player_two = roll_dice(6)

            difference = abs(player_one_strength - player_two_strength) + 1
            if player_one > player_two:
                winner = player_one
                player_two_health -= difference
                count1 += 1
                print(f'{character_one_name} wins the {count1} round ')
            elif player_two > player_one:
                winner = player_two
                player_one_health -= difference
                count2 += 1
                print(f'{character_two_name} wins the {count2} round')
            else:
                count += 1
                print(f'Their sword clash and they draw {count} round')

            if player_one_health <= 0:
                print(f'Oh no {character_one_name} has die!')
                print(f'{character_two_name} destroyed {character_one_name} in {count2} rounds')
                break
            elif player_two_health <= 0:
                print(f'Oh no {character_two_name} has die!')
                print(f'{character_one_name} destroyed {character_two_name} in {count1} rounds')
                break








