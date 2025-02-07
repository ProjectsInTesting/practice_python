def login():
    db_username = "Admin"
    db_password = "Password"

    username = input ("Please, enter your username:  ")
    password = input ("Please, enter your password:  ")

    if username == db_username and password == db_password:
        print ("You logged in successfully.")
    else:
        print (" oops, wrong passwrod or username: * please try again")
     login()

