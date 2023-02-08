if __name__ == '__main__':
    print("Star Wars Name Generator")
    print()
    first_name = str(input("Input your first name-> "))
    slice_first_name = first_name[:3]
    last_name = str(input("Input your last name-> "))
    slice_last_name = last_name[:3]
    maiden_name = str(input("Input your mother's maiden name-> "))
    slice_maiden_name = maiden_name[:2]
    city_name = str(input("Input the city where you were born-> "))
    slice_city_name = city_name[-3:]
    print(f"Your star Wars name is {str(slice_first_name).title()+ str(slice_last_name).title()+str(slice_maiden_name).title()+str(slice_city_name).title()}")



