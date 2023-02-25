
def palindrome(s_word):
    flag = bool
    if s_word == s_word[::-1]:
        flag = True
        print(flag)
    else:
        flag = False
        print(flag)
    return flag


if __name__ == '__main__':
    word = input("Enter word-> ")
    palindrome(word)
