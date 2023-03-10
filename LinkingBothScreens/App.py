import tkinter as tk
from tkinter import *
from tkinter import filedialog
from Classes.FileManagement import FileManager
from Game import GameFrame
from PIL import Image, ImageTk
import tkinter.messagebox as tkM
from DataSets.DetectObjects import extract_objects
import sys
from PIL import ImageTk

class App:

    # dynamic variable
    def __init__(self,title, w, h):
        self.w = w
        self.h = h
        self.window = tk.Tk()
        # self.window.geometry(f"{w}x{h}")
        # self.window.title(title)
        # self.window.resizable(False, False)
        w = 1080  # Width
        h = 720  # Height
        screen_width = self.window.winfo_screenwidth()  # Width of the screen
        screen_height = self.window.winfo_screenheight()  # Height of the screen
        x = (screen_width / 2) - (w / 2)
        y = (screen_height / 2) - (h / 2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.title('Shapes Categorization')
        self.window.resizable(0, 0)
        # in order to add image in window

        self.img_input = None
        self.dir_file_name = None
        #load
        self.__load_app()

        exit_btn = Button(self.window, text='X', command=lambda: exit(), font=("Comic Sans MS", 13, 'bold'), fg='white',
                          bg='limegreen', height='1', width='3')
        exit_btn.place(x=1038, y=2)

        bgImage = ImageTk.PhotoImage(file='LoadingBackground.jpg')
        # pass the image through label to view
        bgLabel = Label(self.window, image=bgImage)
        bgLabel.place(x=0, y=0)
        bgLabel.pack(fill=BOTH, expand=YES)

    def select_file(self, canvas):
        valid_file_formats  = [("Valid img formats", ("*.jpg", "*.png"))]
        def get_dir_file():
            self.dir_file_name = filedialog.askopenfilename(title="Select a image", filetypes=valid_file_formats)
            #set image
            img = Image.open(self.dir_file_name)
            #resizing the image
            approx_h = 350
            approx_w = (350*img.width)//img.height
            canvas.config(width = approx_w)
            img_resized = img.resize((approx_w, approx_h))
            #place the img on input
            self.tk_img_input = ImageTk.PhotoImage(img_resized)
            canvas.create_image(0, 0, image=self.tk_img_input, anchor=tk.NW)

        #move to the game sequence
        return get_dir_file

    def start_game(self):
        # must select a file first
        if(self.dir_file_name is None or self.dir_file_name.strip()==""):
            tkM.showinfo("Interruption!", "Select a picture first")
            return
        elif not FileManager.check_file_ifexists(self.dir_file_name):
            tkM.showinfo("Interruption!", "Select existing picture")
            return

        #remove data temp
        FileManager.remove_allfiles("DataSets/DataTemp")
        # process image processing
        print("Extracting objects from image..")
        extract_objects(self.dir_file_name)
        print("Done extracting")
        # go to game
        print("Starting Game")
        self.go_to_game()
        
    def go_to_game(self):
        # Going to the game frame segment
        self.frame_app.destroy()
        self.frame_app = None
        self.frame_game = GameFrame(self.window, self)

        #reseting dynamic var
        self.img_input = None
        self.dir_file_name = None
        

    def __load_app(self):
        #frame
        self.frame_app = tk.Frame(self.window)
        self.frame_app.pack()

        #labels and title
        tk.Label(self.frame_app, text="Shape Categorization Game based on Images", font=("Arial", 25)).pack(pady=10)
        tk.Label(self.frame_app, text="Developed by Team Padayon", font=("Arial", 10)).pack()
        #Image
        canvas = tk.Canvas(self.frame_app, width= 400, height= 350, bg="gray")
        canvas.pack(pady=20)

        #file
        file_btn = tk.Button(self.frame_app, text="Select an Image", height= 2, width=15, bg="orange", foreground="black", command=self.select_file(canvas))
        file_btn.pack()

        # run a game
        start_btn = tk.Button(self.frame_app, text="Start Game", height=3, width=23, bg="green", foreground="white", command=self.start_game)
        start_btn.pack(pady=30)

        

    def reload_app(self):
        self.img_input = None
        self.dir_file_name = None
        self.__load_app()
        

    def run(self):
        self.window.mainloop()

app = App("Shapes Categorization", 775, 625)
app.run()