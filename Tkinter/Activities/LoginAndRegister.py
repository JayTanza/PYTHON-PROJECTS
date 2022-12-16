from functools import partial
from tkinter import *
from tkinter import messagebox
import Common
import sqlite3

class User:
    def validateLogin(username, password):
        db=sqlite3.connect('login.sqlite')
        db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')
        db.execute("INSERT INTRO login(username,password) VALUES('admin','admin')")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM login where username=? AND password=?",())
        print("username entered :", username.get())
        print("password entered :", password.get())
        z = Common.initAll
        Ausername = z.z.getAcustomer()
        Apassword = z.z.getAlimit()
        if(username.get() == Ausername and password.get() == Apassword):
            print("Successfully Login!")
            messagebox.showinfo("Login", "Successfully Login!")
        else:
            print("Incorrect Username or Password!")
            messagebox.showinfo("Login", "Incorrect Username or Password!")
        return
        # window
    tkWindow = Tk()
    tkWindow.geometry('1980x1080')
    tkWindow.title('LOGIN AND REGISTER FORM')
    # username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)
    validateLogin = partial(validateLogin, username, password)
    # login button
    loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)
    tkWindow.mainloop()