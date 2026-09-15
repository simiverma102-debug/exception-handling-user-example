def login_02():
    
    user_data = {
        "name": "Crow T. Robot",
        "id": 11067
    }
    if user_data.get("is_logged_in"):
        if user_data["is_logged_in"]:
            print(f"{user_data['name']}, "
                "you've successfully logged in!")
        else:
            print("You must log in to continue.")
            
    else:
        print("error")

login_02()