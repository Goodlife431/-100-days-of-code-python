print("\033[31m", "Oduwole's movie character creator \n ---", "\033[0m")
print()
complexion = input("Are you very fair in complexion: ")
if complexion == "yes":
    print("Then you are my sister")
else:
    print("Aww, then you are not kemi")
behaviour = input("Are you loving and caring: ")
if behaviour == "yes":
    print("Then you are mummy")
else:
    print("Aww, then you are not mummy")
snore = input("Do you snore at night?: ")
if snore == "yes":
    print("you are daddy")
else:
    print("Aww, Then you are not daddy")
stubborn = input("Are u very stubborn: ")
if stubborn == "yes":
    print("yes you are my brother")
else:
    print("Aww, you are not my brother")
if (complexion and behaviour and snore and stubborn) == "no":
    print("You are not a member of Oduwole's family")
