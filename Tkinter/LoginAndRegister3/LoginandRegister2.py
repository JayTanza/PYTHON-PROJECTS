def register():
    db = open("database.txt", "r")
    Username = input("Create username:")
    Password = input("Create password:")
    Password1 = input("Confirm password:")

    if Password != Password1:
        print("Passwords don't match, restart")
    else:
        if len(Password) <= 6:
            print("Password is too short, restart")
            register()
        elif Username in db:
            print("Username exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(Username+", "+Password+"\n")
            print("Success!")


def login():
    db = open("database.txt", "r")
    Username = input("Enter username:")
    Password = input("Enter password:")

    if Username and Password in db:
        print("Successfully Login!")
    else:
        print("Unsuccessfully Login!")
login()