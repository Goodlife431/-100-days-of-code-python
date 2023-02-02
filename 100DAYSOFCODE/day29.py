if __name__ == '__main__':
    def suber_subroutine(word, color):
        if color == 'red':
            print('\033[31m', word, end=" ")
        elif color == 'black':
            print('\033[30m', word, end=" ")
        elif color == 'green':
            print('\033[33m', word, end=" ")
        elif color == 'yellow':
            print('\033[33m', word, end=" ")
        elif color == 'blue':
            print('\033[34m', word, end=" ")
        elif color == 'purple':
            print('\033[35m', word, end=" ")
        elif color == 'cyan':
            print('\033[36m', word, end=" ")
        elif color == 'white':
            print('\033[31m', word, end=" ")


    print("Super Subroutine")
    suber_subroutine('with my new program', 'purple')
    print()
    suber_subroutine('i can just call red ("and")', 'red')
    print()
    suber_subroutine('with no weird gaps', 'cyan')
    print()
    suber_subroutine('Epic', 'yellow')


