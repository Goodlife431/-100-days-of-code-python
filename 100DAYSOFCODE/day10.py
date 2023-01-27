print("\034[031m","TIP CALCULATOR", "\033[0m")
bill = float(input("How much did you spend: "))
percentage = int(input("What percentage do you want to tip: "))
people = int(input("How many people in your group: "))
tip_percentage = (percentage / 100 * bill + bill)  / people
tip_percentage = round(tip_percentage, 2)
print("You each owe: ",tip_percentage)