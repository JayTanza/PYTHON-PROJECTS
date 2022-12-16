from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
#from tkinter.ttk import *
from tkinter.ttk import Progressbar
import sys
import pygame

class MainScreen:
    def __init__(self,root):
        self.root = root
        # image_bg = Image.open('D://UDEMY//PythonGame//LoadingBackground.jpg')
        # imagebg = ImageTk.PhotoImage(image_bg)
        # lbl = Label(root, image=imagebg)
        # lbl.place(x=0, y=0)
        # lbl.pack(fill=BOTH, expand=YES)
        pygame.mixer.init()
        pygame.mixer.music.load("Helmet Heroes Soundtrack - 01 - Helmet Heroes.mp3")
        pygame.mixer.music.play(loops=0)
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

        exit_btn = Button(root, text='X',command=lambda: exi_window(), font=("yu gothic ui",13, 'bold'),fg='white',bg='limegreen',height='1', width='3')
        exit_btn.place(x=1038,y=2)

        # playmusic_btn = Button(root, text='P',command=lambda: playmusic(), font=("yu gothic ui",13, 'bold'),fg='white',bg='limegreen',height='1', width='3')
        # playmusic_btn.place(x=995,y=2)

        start_btn = Button(root, text='PLAY',command=lambda: exi_window(), font=("yu gothic ui",13, 'bold'),fg='white',bg='limegreen',height='2', width='15')
        start_btn.place(x=450,y=460)

        option_btn = Button(root, text='OPTION',command=lambda: exi_window(), font=("yu gothic ui",13, 'bold'),fg='white',bg='limegreen',height='2', width='15')
        option_btn.place(x=450,y=540)

        exit_btn = Button(root, text='EXIT',command=lambda: exi_window(), font=("yu gothic ui",13, 'bold'),fg='white',bg='limegreen',height='2', width='15')
        exit_btn.place(x=450,y=620)

        # progress_label = Label(root, text="Loading Please Wait...", font=("yu gothic ui",13, 'bold'),bg='white')
        # progress_label.place(x=400,y=350)
        #
        # #canvas = Canvas(relief = FLAT, background = "#D2D2D2",width = 400, height = 5)
        # progress = Progressbar(root,style="white.Horizontal.TProgressbar",orient=HORIZONTAL,length=1000, mode='determinate')
        # progress.place(x=40,y=400)

        def exi_window():
            sys.exit(root.destroy())

        # def playmusic():
        #     pygame.mixer.music.load("Helmet Heroes Soundtrack - 01 - Helmet Heroes.mp3")
        #     pygame.mixer.music.play(loops=0)
        #root.mainloop()

def page():
    root = Tk()

    image_bg = Image.open('D:/UDEMY/PythonGame/LoadingBackground.jpg')
    imagebg = ImageTk.PhotoImage(image_bg)
    lbl = Label(root, image=imagebg)
    lbl.place(x=0, y=0)
    lbl.pack(fill=BOTH, expand=YES)

    MainScreen(root)
    root.mainloop()

if __name__ == '__main__':
    page()

