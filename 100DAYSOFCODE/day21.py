if __name__ == '__main__':
    multiple_number = int(input('Enter a number: '))
    count = 0
    result = 0
    count2 = 0
    for count in range(1, 11):
        multiple = int(input(f'{multiple_number} * {count} = '))
        result = count * multiple_number
        if multiple == result:
            print('Great work')
            count2 += 1
        if multiple != result:
            print(f'Nope! The answer was {result}')
        count += 1
    print(f'You scored {count2} out of {count}')