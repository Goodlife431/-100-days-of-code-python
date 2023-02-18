import time, os, random
if __name__ == '__main__':
    top_trumps = {}
    top_trumps["Kendrick Lamar"] = {'Intelligence': 178, 'Speed': 87, 'Guile': 32, 'Baldness level': 0}
    top_trumps["Don Toliver"] = {'Intelligence': 100, 'Speed': 50, 'Guile': 100, 'Baldness level': 0}
    top_trumps["Rema"] = {'Intelligence': 100, 'Speed': 100, 'Guile': 100, 'Baldness level': 0}
    top_trumps["Davido"] = {'Intelligence': 90, 'Speed': 87, 'Guile': 200, 'Baldness level': 50}

    while True:
        for key in top_trumps:
            print(key)
        character = input("Pick a character-> ").strip().title()
        computer = random.choice(list(top_trumps.keys()))
        print(f"Computer has picked {computer}")
        print()
        print("Choose your stat: Intelligence, Speed, Guile & Baldness level")
        stats = input("-> ").strip().title()
        print(f"{character}: {top_trumps[character][stats]}")
        print(f"{computer}: {top_trumps[computer][stats]}")

        if top_trumps[character][stats] > top_trumps[computer][stats]:
            print(f"{character} wins")
        elif top_trumps[character][stats] < top_trumps[computer][stats]:
            print(f"{computer} wins")
        else:
            print("DRAW")
