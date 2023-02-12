if __name__ == '__main__':
    moke_beast = {}
    print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
    name = str(input("Input your beast's name-> "))
    beast_type = str(input("Input your beast's type-> ")).title()
    move = str(input("Input your beast's special move-> "))
    HP = int(input("Input your beast's staring HP->"))
    MP = int(input("Input your beast's staring MP->"))

    def check_beast_type():
        moke_beast['name'] = name
        moke_beast['type'] = beast_type
        moke_beast['move'] = move
        moke_beast['HP'] = HP
        moke_beast['MP'] = MP

        for key, values in moke_beast.items():
            if beast_type == 'Water':
                print('\033[31m', end=" ")
            elif beast_type == 'Earth':
                print('\033[30m', end=" ")
            elif beast_type == 'Fire':
                print('\033[34m', end=" ")
            elif beast_type == 'Air':
                print('\033[33m', end=" ")
            print(f"{key}:      {values:^20}")


    check_beast_type()


