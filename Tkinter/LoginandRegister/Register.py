from tkinter import *
from functools import partial

def login():
    print("Login session started")
    screen1 = Toplevel(screen)
    screen1.title("Login And Registration System")

def register_user(username, password):

    username_info = username.get()
    password_info = password.get()
    db = open("database.txt", "r")

def register():

    print("Register session started")
    screen1 = Toplevel(screen)
    screen1.title("Login And Registration System")
    screen1.geometry("400x350")
    #global username
    #global password
    username = StringVar()
    password = StringVar()
    password1 = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username").pack()
    Entry(screen1, textvariable=username).pack()
    Label(screen1, text = "Password").pack()
    Entry(screen1, textvariable=password).pack()
    Label(screen1, text="Retype-Password").pack()
    Entry(screen1, textvariable=password1).pack()
    Label(screen1, text="").pack()
    Button(screen1, text ="Register", height=1, width=10,command=register_user).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Login And Registration System")
    Label(text="Login And Registration System", bg= "grey", height= "2", width="300", font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()
main_screen()

