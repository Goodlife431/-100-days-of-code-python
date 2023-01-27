if __name__ == '__main__':
    print("\033[32m", "EXAM GRADE CALCULATOR", "\033[0m")
    name = input("Name of exam: ")
    max_score  = int(input("Max. Possible Score: "))
    score = int(input("Your score: "))
    if 90 <= score <= 100:
        print(f"You got {score}.00% which is a A+")
    elif 80 <= score <= 89:
        print(f"You got {score}.00% which is a A-")
    elif 70 <= score <= 79:
        print(f"You got {score}.00% which is a B")
    elif 60 <= score <= 69:
        print(f"You got {score}.00% which is a C")
    elif 50 <= score <= 59:
        print(f"You got {score}.00% which is a D")
    elif score < 50:
        print(f"You got {score}.00% which is a U")
