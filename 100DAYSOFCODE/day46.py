if __name__ == '__main__':
    moke_beast = {}

    def pretty_print():
        print()
        for key, value in moke_beast.items():
            print(key, end= " : ")
            for subKey, subValue in value.items():
                print(subKey, subValue, end= " | ")
            print()
    while True:
        beast_name = input("Input the beast name > ")
        beast_element = input("Input the beast element > ")
        beast_move = input("Input the beast special move > ")
        hp = input("Input the beast starting HP > ")
        mp = input("Input the beast starting MP > ")

        moke_beast[beast_name] = {"element": beast_element, "move": beast_move, "HP": hp, "MP": mp}
        pretty_print()
        exit_game = input("Do you want to exit game yes or no-> ").strip().lower()
        if exit_game == "yes":
            exit()
        else:
            continue