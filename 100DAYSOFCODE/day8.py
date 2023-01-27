print("\033[32m", "MY PERSONAL AFFIRMATION", "\033[0m")
print()
name = input("Who are you: ")
print()
achieve = input("What do you want to achieve?: ")
print()
feelings = input("On a scale of 1 - 10 how do you feel today?: ")
print()
if name == "Seun" or name == "seun" and feelings <= "6":
    print("hey ", name, "I know you are not feeling too good today", "\n Just a quick  reminder",
          "\n Good things take time. Passion, hard work, and dedication will always pay off eventually. Do not give "
          "up on your dreams. In all things, work to be the best, and remember that only by constantly improving your "
          "skills can you truly be your best self. \n HAVE A GREAT DAY")
elif name == "Seun" or name == "seun" and feelings > "7":
    print("Hey ", name, "let's do this, I know you are feeling great today", "make sure you make your day productive..",
          "and remember is not how fast you did it, is how well....\n HAVE A GREAT DAY")
else:
    print(
        "Code, inspire and create. Don’t be afraid of the unknown; embrace it! Programming is like solving a puzzle. "
        "You think you’ve got it, and then you realize there are many more pieces to it. The code is the way: "
        "programming is a way of viewing reality.")
