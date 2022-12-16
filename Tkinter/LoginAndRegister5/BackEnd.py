from tkinter import *
from tkinter import messagebox

class Backend:

    def registerUser(obj,username, password):
        obj.Ausername = username.get()
        obj.Apassword = password.get()
        obj.Apassword1 = password1.get()

        print("Username entered :", username.get())
        print("Password entered :", password.get())
        print("Retype-password entered :", password1.get())

        db = open('Database.txt', 'w')

        if obj.Apassword.get() != obj.Apassword1.get():
            print("Passwords don't match, restart")
            messagebox.showinfo("Register", "Passwords don't match, restart")
        else:
            if len(obj.Apassword.get()) <= 6:
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
                db.write(Ausername.get() + ", " + Apassword.get() + "\n")
                print("Success!")
                print("Hi", Ausername.get())
                messagebox.showinfo("Register", "Successfully Register!")