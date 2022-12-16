from tkinter import *
from tkinter import messagebox
from functools import partial
import os

def register_user():
    username_info = username.get()
    password_info = password.get()
    password1_info = password1.get()
    db = open("Database.txt", "r")
    # db.write(username_info+ ", " + password_info+ "\n")
    # db.close()
    # # username_entry.delete(0, END)
    # # password_entry.delete(0, END)
    # print("Success!") 
    # print("Hi", username_info)
    # messagebox.showinfo("Register", "Successfully Register!")
    # Label(screen1, text="Successfully Register!", fg="green", font=("Calibri", 13)).pack()

    print("Username entered :", username_info)
    print("Password entered :", password_info)

    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d,f))
    print(data)

    if password_info!= password1_info:
        print("Passwords don't match, restart")
        messagebox.showinfo("Register", "Passwords don't match, restart")
    else:
        if len(password_info) <= 6 and len(password_info) != 0:
            print("Password is too short, restart")
            messagebox.showinfo("Register", "Password is too short, restart")
            screen1.mainloop()
        elif username_info in d:
            print("Username exists")
            messagebox.showinfo("Register", "Username exists")
            screen1.mainloop()
        elif len(username_info) == 0 and len(password_info) == 0 and len(password1_info) == 0:
            print("Textbox is Empty!")
            messagebox.showinfo("Register", "Textbox is Empty!")
            screen1.mainloop()
        else:
            db = open("Database.txt", "a")
            db.write(username_info + ", " + password_info + "\n")
            print("Success!")
            print("Hi", username_info)
            messagebox.showinfo("Register", "Successfully Register!")

def register():
    global screen1
    global username
    global password
    global password1
    global username_entry
    global password_entry
    global password1_entry

    screen1 = Toplevel(screen)
    screen1.title("Register Screen")
    screen1.geometry("450x350")
    Label(screen1, text="Registration System", bg="grey", height="2", width="300", font=("Calibri", 13)).pack()
    Label(screen1, text="").pack()

    username = StringVar()
    password = StringVar()
    password1 = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()

    Label(screen1, text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()

    Label(screen1, text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()

    Label(screen1, text="Retype-Password").pack()
    password1_entry = Entry(screen1, textvariable=password1)
    password1_entry.pack()

    Label(screen1, text="").pack()
    Button(screen1, text="Register", height=1, width=17, command=register_user).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    db = open("Database.txt", "r")
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    print(data)
    #list_of_files = os.listdir()

    if username1 in d:
        # db = open("Database.txt", "r")
        # verify = db.read().splitlines()
        if password1 in f:
            print("Login Success!")
            messagebox.showinfo("Login", "Successfully Login!")
        else:
            print("Password has not been recognised!")
            messagebox.showinfo("Login", "Password has not been recognised!")
    else:
        print("User not found!")
        messagebox.showinfo("Login", "User not found!")

def login():
    global screen2
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    screen2 = Toplevel(screen)
    screen2.title("Login Screen")
    screen2.geometry("450x350")
    Label(screen2,text="LOGIN AND REGISTER SYSTEM", bg="grey", width="400", height="2", font=("Calibri", 13)).pack()
    Label(screen2,text="", height="4").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text="Username").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()

    Label(screen2, text="Password").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()

    Label(screen2, text="").pack()
    Button(screen2, text="Login", height=1, width=17, command=login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("450x350")
    screen.title("Login and Register")
    Label(text = "LOGIN AND REGISTER SYSTEM", bg="grey",width="400",height="2", font=("Calibri", 13)).pack()
    Label(text = "",height="4").pack()
    Button(text = "Login",width="20", height="3", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register",width="20", height="3", command = register).pack()

    screen.mainloop()
main_screen()