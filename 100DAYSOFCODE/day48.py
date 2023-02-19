import time, os

for i in range(3):
    name = input("What is your name: ")
    score = input("Enter score out of 100,000: ")
    print()

    f = open("high_score.txt", "a+")
    f.write(f"{name}:  {score}\n")
    f.close()
    print("Added to high score table")

    time.sleep(1)
    os.system("clear")
