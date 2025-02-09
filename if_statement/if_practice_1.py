db_username = "admin"
db_password = "123456"

username = input ("Please enter your username:")
password = input ("please enter your password: ")

if username == db_username and password == db_password:
    print ("You have logged in Successfully!")
else:
    print ("wrong credentials used! please try agian")
