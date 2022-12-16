class Person:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def username(self):
        return self.firstname
    def password(self):
        return self.lastname

p1 = Person("Jay","123")
user = p1.username()
passw = p1.password()

name = str(input("Enter Username: "))

pass1 = str(input("Enter Password: "))

if(name == user and passw == pass1):
    print("Successfully Login!")
else:
    print("Failed Login!")
