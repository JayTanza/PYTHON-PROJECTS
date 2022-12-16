from tkinter import *
from tkinter import messagebox
from functools import partial

class FrontEnd:

    def registerUser(username, password, password1):

        Ausername = username
        Apassword = password
        Apassword1 = password1

        print("Username entered :", username.get())
        print("Password entered :", password.get())
        print("Retype-password entered :", password1.get())

        db = open('Database.txt', 'w')

        if Apassword.get() != Apassword1.get():
            print("Passwords don't match, restart")
            messagebox.showinfo("Register", "Passwords don't match, restart")
        else:
            if len(Apassword.get()) <= 6:
                print("Password is too short, restart")
                messagebox.showinfo("Register", "Password is too short, restart")
                screen.mainloop()
            # elif len(Ausername.get()) <= 0:
            #     print("Textbox is Empty")
            #     messagebox.showinfo("Register", "Textbox is Empty, restart")
            #     screen.mainloop()
            # elif Ausername in db:
            #     print("Username exists")
            #     messagebox.showinfo("Register", "Username exists")
            #     screen.mainloop()
            else:
                db = open("Database.txt", "a")
                db.write(Ausername.get() + ", " + Apassword.get()+ "\n")
                print("Success!")
                print("Hi", Ausername.get())
                messagebox.showinfo("Register", "Successfully Register!")

    global screen
    screen = Tk()
    screen.geometry("400x350")
    Label(text="Login And Registration System", bg="grey", height="2", width="300", font=("Calibri", 13)).pack()
    Label(text="").pack()

    username = StringVar()
    password = StringVar()
    password1 = StringVar()

    Label(screen, text = "Please enter details below").pack()
    Label(screen, text = "").pack()

    Label(screen, text = "Username").pack()
    Entry(screen, textvariable=username).pack()

    Label(screen, text = "Password").pack()
    Entry(screen, textvariable=password).pack()

    Label(screen, text="Retype-Password").pack()
    Entry(screen, textvariable=password1).pack()

    registerUser = partial(registerUser, username, password, password1)

    Label(screen, text="").pack()
    Button(screen, text="Register", height=1, width=10, command=registerUser).pack()

    screen.mainloop()
