import random

if __name__ == '__main__':
    list_of_colors = ["White", "Yellow", "Blue", "Red", "Green", "Black", "Brown", "Silver", "Gray", "plum"]
    picked_letter = []
    lives = 6
    choice = random.choice(list_of_colors)
    while True:
        letter = str(input("Choose a letter-> ")).title()
        if letter in picked_letter:
            picked_letter.append(letter)
            print("You have have tried this letter before")
            continue
        if letter in choice:
            print("You found a word correctly")
        else:
            print("Nope, not in there!")
            lives -= 1

        all_letters = True
        for i in choice:
            if i in picked_letter:
                print(i, end='')
            else:
                print("_", end='')
                all_letters = False

        if lives <= 0:
            print(f"You have run out of lives. The right word is {choice}")
        if all_letters:
            print(f"You have won{lives} left")
        else:
            print(f"You have {lives} left")
