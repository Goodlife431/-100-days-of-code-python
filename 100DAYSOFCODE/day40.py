if __name__ == '__main__':
    contact_card = {}
    print("Here's your contact card")
    name = str(input("name: "))
    date_of_birth = input("Date of birth: ")
    Telephone_number = str(input("Telephone number: "))
    Email = str(input("Email: "))
    Address = str(input("Address: "))

    def print_contact_card():
        print("Here's your contact card")
        print()
        contact_name = contact_card['name'] = name
        contact_dob = contact_card['DOB'] = date_of_birth
        contact_tel = contact_card['Tel'] = Telephone_number
        contact_email = contact_card['Email'] = Email
        contact_address = contact_card['Address'] = Address
        print(f"""Hi {contact_name}. Our dictionary says that you were
born on {contact_dob} , we can call you on{contact_tel},
email {contact_email}, or write to{contact_address} """)
    print_contact_card()



