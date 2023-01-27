if __name__ == '__main__':
    print("\033[35m", "Fill-in the blank Lyrics!", "\033[0m")
    print("\033[35m", "type in the blank lyrics, see if you're as cool as me", "\033[0m")
    count = 0
    while True:
        lyrics = input("You are the handicap: _____________")
        if lyrics != "you must face":
            print("Nope try again")
            count += 1
        elif lyrics == "you must face":
            print("well done it only took you ", count, "attempts!")
            break
