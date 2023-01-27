import random
if __name__ == '__main__':
    count = 0
    guessing_number = random.randint(1, 1000000)
    number = 0
    while True:
        if 0 <= number <= 1000000:
            number = int(input('Enter your guess: '))
        if number > guessing_number:
            print('Too high')
        elif number < guessing_number:
            print('Too low')
        elif number == guessing_number:
            print('Correct!')
            break
        if number == '-':
            exit()
        count += 1
    print(f'it took {count} guess to get it correct')

