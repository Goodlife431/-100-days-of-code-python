if __name__ == '__main__':
    f = open("high_score.txt", "r")
    scores = f.read().split("\n")
    f.close()

    high_score = 0
    name = None
    for row in scores:
        data = row.split()
        if data != []:
            if int(data[1]) > high_score:
                high_score = int(data[1])
                name = data[0]

    print(f"{name} wins with highest score of {high_score}")

