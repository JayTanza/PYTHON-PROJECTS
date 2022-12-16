from tkinter import * #Access all the module of tkinter
from PIL import ImageTk
import sys
import pygame
from tkinter import messagebox
import pymysql
import sqlite3

#functionality
def login_page():
    root.destroy()
    import Signin

def connect_database():
    if(emailEntry.get()=='' or userEntry.get()=='' or passEntry.get()=='' or repassEntry.get()==''):
        messagebox.showerror('Error','All Fields are Required!')
    elif(passEntry.get() != repassEntry.get()):
        messagebox.showerror('Error','Password Mismatch!')
    elif(check.get() == 0):
        messagebox.showerror('Error', 'Please Accept Terms and Conditions!')
    else:
        messagebox.showinfo('Success','Successfully Register!')
        try:
            con = sqlite3.connect('Database/Users.db')
            mycursor = con.cursor()
            query = (
                'create table Usersinfo(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))')
            mycursor.execute(query)
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        query = ('INSERT INTO Usersinfo(email,username,password) VALUES(?,?,?)',
                 (email_input.get(), user_input.get(), pass_input()))
        mycursor.execute(query)
        con.commit()
        con.close()
        # query='create database users'
        # mycursor.execute(query)
        # query='main.db'
        # mycursor.execute(query)
root = Tk()
root.resizable(0,0)
root.iconbitmap("favicon.ico")
# in order to add image in window
bgImage = ImageTk.PhotoImage(file='createaccbg.jpg')
# pass the image through label to view
bgLabel = Label(root,image=bgImage)
bgLabel.place(x=0,y=0)
bgLabel.pack(fill=BOTH, expand=YES)

# add background music
pygame.mixer.init()
pygame.mixer.music.load("Helmet Heroes Soundtrack - 01 - Helmet Heroes.mp3")
pygame.mixer.music.play(loops=0)

# Calculate Starting X and Y coordinates for Window
w = 1080  # Width
h = 720  # Height
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight()  # Height of the screen
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)

exit_btn = Button(root, text='X',command=lambda: exit_window(), font=("Comic Sans MS",13, 'bold'),fg='white',bg='limegreen',height='1', width='3')
exit_btn.place(x=1038,y=2)

back_btn = Button(root, text='<',command=lambda: login_page(), font=("Comic Sans MS",13, 'bold'),fg='white',bg='limegreen',height='1', width='3')
back_btn.place(x=2,y=2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Helmet Heroes')
root.overrideredirect(1)

email_input=StringVar()
user_input=StringVar()
pass_input=StringVar()

heading = Label(root, text='CREATE AN ACCOUNT', font=("Comic Sans MS", 25, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='20')
heading.place(x=330,y=50)

emaillbl = Label(root, text='Email Address', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
emaillbl.place(x=345,y=150)

emailEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", justify='center',textvariable=email_input)
emailEntry.place(x=345,y=190)

userlbl = Label(root, text='Username', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
userlbl.place(x=345,y=250)

userEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", show='', justify='center',textvariable=user_input)
userEntry.place(x=345,y=290)

passlbl = Label(root, text='Password', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
passlbl.place(x=345,y=350)

passEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", show='', justify='center',textvariable=pass_input)
passEntry.place(x=345,y=390)

repasslbl = Label(root, text='Confirm Password', font=("Comic Sans MS", 18, "bold"),bg='limegreen',fg='white',borderwidth=3, relief="solid",height='1', width='25')
repasslbl.place(x=345,y=450)

repassEntry = Entry(root, width=25, font=("Comic Sans MS", 18, "bold"),borderwidth=3, relief="solid", show='', justify='center')
repassEntry.place(x=345,y=490)

check=IntVar()

termandconditions = Checkbutton(root,text='I agree to the Terms & Conditions',font=("Comic Sans MS", 13, "bold"),width='35',variable=check)
termandconditions.place(x=345,y=540)

signup_btn = Button(root, text='SIGN UP', font=("Comic Sans MS", 18, "bold"),fg='white',bg='limegreen',height='1', width='25',activebackground='white',command=connect_database)
signup_btn.place(x=345,y=585)

developby = Label(root, text='Developed by: Jay Tanza', font=("Comic Sans MS", 10, "bold"),bg='limegreen',fg='white',borderwidth=1, relief="solid",width='22')
developby.place(x=10,y=685)

def exit_window():
    sys.exit(root.destroy())

root.mainloop()