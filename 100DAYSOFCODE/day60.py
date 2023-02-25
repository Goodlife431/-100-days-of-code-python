import datetime

print("🌟Event Countdown Timer🌟")

today = datetime.date.today()

event = input("Input the event > ")

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

date = datetime.date(year, month, day)

if date < today:
    print("Coming soon")
elif date > today:
    print("Hope you enjoyed it")
else:
    print(f"{event} is today")
