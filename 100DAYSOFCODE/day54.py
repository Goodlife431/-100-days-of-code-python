if __name__ == '__main__':
    print("🌟Shop $$ Tracker🌟")
    with open("Day54Totals.csv") as file:
        reader = csv.DictReader(file)
        line = 0

        total = 0.0
        for row in reader:
            total = + float(row["Cost"]) * float(row["Quantity"])
        print(f"Your shop took pounds today. {total}")

