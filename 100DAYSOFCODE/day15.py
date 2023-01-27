if __name__ == '__main__':
    while True:
        animal = input("What animal do you want: ")
        if animal == "cow":
            print("Cow goes moo")
        elif animal == "tiger":
            print("A tiger rows")
        elif animal == "cat":
            print("A cat purrs")
        elif animal == "snake":
            print("A snake hisses")
        elif animal == "dog":
            print("Dog barks ")
        else:
            print("I dont know this animal sound")

        exit_button = input("Do you want to exit? (yes or no): ")
        if exit_button == "yes":
            break
