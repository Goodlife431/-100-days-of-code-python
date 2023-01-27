if __name__ == '__main__':
    def pin_picker(number):
        import random
        pin = ''
        for i in range(number):
            pin += str(random.randint(1, 9))
        return pin


    my_pin = pin_picker(4)
    print(my_pin)
