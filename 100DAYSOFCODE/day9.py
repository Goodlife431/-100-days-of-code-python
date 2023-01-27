if __name__ == '__main__':
    print("\033[032m", "GENERATION IDENTIFIER", "\033[0m")
    print()
    age = int(input("Which year were you born: "))
    if 1883 <= age <= 1900:
        print("Hah! Lost Generation")
    elif 1901 <= age <= 1927:
        print("Wow! Greatest Generation")
    elif 1928 <= age <= 1945:
        print("Silent Generation")
    elif 1944 <= age <= 1964:
        print("Baby Boomers")
    elif 1965 <= age <= 1980:
        print("Generation X")
    elif 1981 <= age <= 1996:
        print("Hah! Millennial's")
    elif 1997 <= age <= 2012:
        print("Generation Z")
    elif 2012 <= age <= 2023:
        print("Generation Alpha")
    else:
        print("I don't know your generation")
