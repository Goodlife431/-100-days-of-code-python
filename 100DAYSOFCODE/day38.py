if __name__ == '__main__':
    def color_subroutine(word):
        if word == 'r':
            print('\033[31m', end="")
        elif word == 'b':
            print('\033[30m', end="")
        elif word == 'g':
            print('\033[33m', end="")
        elif color == 'y':
            print('\033[33m', end="")
        elif word == 'b':
            print('\033[34m', end="")
        elif word == '':
            print('\033[35m', end="")
        elif word == 'c':
            print('\033[36m', end="")
        elif word == 'w':
            print('\033[37m', end="")


    text = str(input("What sentence do you want to rainbow-ising?-> "))
    for color in text:
        color_subroutine(text.strip().lower())
        print(color, end="")

