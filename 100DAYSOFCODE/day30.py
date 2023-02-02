if __name__ == '__main__':
    print('30 Days down what do you think')
    for i in range(1, 31):
        thought = input(f'Day {i}-> \n')
        text = f'You thought Day {i} was-> {thought}'
        print(f'{text:^47}')
    print('Thank you for joining us')
