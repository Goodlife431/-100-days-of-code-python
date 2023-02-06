import time, os
if __name__ == '__main__':
    list_of_email = []

    def pretty_print():
        os.system('clear')
        print('ListOfEmail')
        print()
        for index in range(len(list_of_email)):
            print(f'{index}: {list_of_email[index]}')
            time.sleep(1)

    def email_spammer():
        for i in range(len(list_of_email)):
            print(f"'email {i}\n Dear{list_of_email[i]}\n It has come to our attention that you're missing out on the "
                  f"amazing"
                  f"Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email "
                  f"address to every spammer we've ever encountered and also sign you up to the My Little Pony "
                  f"newsletter, because that's neat. We might just do that anyway.\nLove and hugs,\nIan Spammington III")
            time.sleep(0.5)
            os.system('clear')
            if i == 10:
                break

    while True:
        print('SPAMMERS Inc.')
        menu = int(input('1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n5. exit\n ->'))
        if menu == 1:
            email = input('Email -> ')
            list_of_email.append(email)
        elif menu == 2:
            email = input('Email -> ')
            if email in list_of_email:
                list_of_email.remove(email)
            pretty_print()
            time.sleep(1)
            os.system('clear')
        elif menu == 3:
            pretty_print()
            time.sleep(1)
            os.system('clear')
        elif menu == 4:
            email_spammer()
        else:
            if menu == 5:
                exit()
