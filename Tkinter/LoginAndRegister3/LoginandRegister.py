from functools import partial
from tkinter import *
from tkinter import messagebox
import Common

class User:

	def validateLogin(username, password):
		print("username entered :", username.get())
		print("password entered :", password.get())
		Ausername = username
		Apassword = password
		db = open('database.txt', 'r')

		z = Common.initAll
		Ausername = z.z.getAcustomer()
		Apassword = z.z.getAlimit()

		if not len(Ausername or Apassword)<1:
			d = []
			f = []
			for i in db:
				a,b = i.split(", ")
				b = b.strip()
				d.append(a)
				f.append(b)
			data = dict(zip(d,f))
		#database text file
			try:
				if(data[Ausername.get()]):
					try:
						if(Apassword.get() != data[Ausername.get()]):
							print(data)
							print("Password or Username is incorrect")
							messagebox.showinfo("Login", "Incorrect Username or Password!")
						else:
							print("Login Success!")
							print("Hi", Ausername.get())
							messagebox.showinfo("Login", "Successfully Login!", Ausername.get())
					except:
						print("Password or Username is incorrect")
						messagebox.showinfo("Login", "Incorrect Username or Password!")
				else:
					print("Password or Username doesn't exist")
					messagebox.showinfo("Login", "Password or Username doesn't exist")
			except:
				print("Password or Username doesn't exist")
				messagebox.showinfo("Login", "Password or Username doesn't exist")
		else:
			print("Please enter a value!")
			messagebox.showinfo("Login", "Please enter a value!")

#window
	tkWindow = Tk()
	tkWindow.geometry('1980x1080')
	tkWindow.title('LOGIN AND REGISTER FORM')

#username label and text entry box
	usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
	username = StringVar()
	usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

#password label and password entry box
	passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
	password = StringVar()
	passwordEntry = Entry(tkWindow, textvariable=password, show='').grid(row=1, column=1)

	validateLogin = partial(validateLogin, username, password)

#login button
	loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)


	tkWindow.mainloop()