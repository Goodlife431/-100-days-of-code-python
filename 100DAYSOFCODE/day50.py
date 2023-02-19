import os
import time
import random


def add_item():
    idea = input("Enter your idea-> ")
    f = open("idea.txt", "a+")
    f.write(f"{idea}\n")
    f.close()
    print()
    print("Nice! Your idea has been stored.")
    time.sleep(1)
    os.system("clear")


def load_idea():
    f = open("idea.txt", "r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    picked = random.choice(ideas)
    print(picked)
    time.sleep(0.30)
    os.system("clear")


while True:
    menu = int(input(f"""
    1. add an idea 
    2. load a random idea
    3. exit \n
                """))
    if menu == 1:
        add_item()
    elif menu == 2:
        load_idea()
    elif menu == 3:
        exit()
    else:
        continue
