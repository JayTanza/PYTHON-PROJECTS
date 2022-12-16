from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
#from tkinter.ttk import *
from tkinter.ttk import Progressbar
import sys
import Main_Screen

root = Tk()

image_bg = Image.open('D:\\UDEMY\\PythonGame\\Loadingpic.jpg')
imagebg = ImageTk.PhotoImage(image_bg)

lbl = Label(root,image=imagebg)
lbl.place(x=0,y=0)
lbl.pack(fill=BOTH, expand = YES)

w = 1080  # Width
h = 720  # Height

screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)
i = 0

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Helmet Heroes')
root.iconbitmap(r'favicon.ico')
root.overrideredirect(1)

progress_label = Label(root, text="Loading Please Wait...", font=("yu gothic ui",15, 'bold'),bg='white')
progress_label.place(x=390,y=480)

#canvas = Canvas(relief = FLAT, background = "#D2D2D2",width = 400, height = 5)
progress = Progressbar(root,style="white.Horizontal.TProgressbar",orient=HORIZONTAL,length=920, mode='determinate')
progress.place(x=100,y=520)

def top():
    win = Toplevel()
    Main_Screen.MainScreen(win)
    root.withdraw()
    win.deiconify()

def loadingscreen():
    global i
    if(i <= 10):
        txt = ('Please wait for a moment... '+(str(10*i))+'%')
        progress_label.config(text=txt)
        progress_label.after(300, loadingscreen)
        progress['value'] = 10*i
        i += 1
    else:
        top()

loadingscreen()

root.mainloop()