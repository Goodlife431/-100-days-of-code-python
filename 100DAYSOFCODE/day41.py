import os, time
if __name__ == '__main__':
    information = {}
    print("🌟Website Rating🌟")
    website_name = str(input("Input the website name-> "))
    url = str(input("Input the URL-> "))
    description = str(input("Input your a description-> "))
    rating = str(input("Input the a star rating out of 5-> "))


    def print_information():
        information['name'] = website_name
        information['URL'] = url
        information['description'] = description
        information['rating'] = rating
        for key, values in information.items():
            time.sleep(1)
            os.system('clear')
            print(f"{key}: {values}")

    print_information()


