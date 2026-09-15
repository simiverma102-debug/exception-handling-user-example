def login_01():
    
    user_data = {
        "name": "Crow T. Robot",
        "id": 11067
    }
    try:                                            #try clause
        if user_data["is_logged_in"]:
            print(f"{user_data['name']}, "
                "you've successfully logged in!")
        else:
            print("You must log in to continue.")
    except KeyError as error:                        #except clause
        print("you have entered a key that " 
        f"doesn't exist in 'user_data: {error}")
login_01()