import pytesseract
import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from functools import partial
from PIL import Image

class OCR:

    win = Tk()
    height = 540
    width = 800
    menubar = Menu(win)
    Label(win, text="Paste Image Path Below").grid()
    URLip = Text(win)
    output = Label(win)

    def __init__(self, **kwargs):
        try:
            self.height = kwargs[height]
        except:
            pass

        try:
            self.width = kwargs[width]
        except:
            pass

        self.win.title("OCR - Convertor")

        self.win.config(menu=self.menubar)

        # Center the window
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.width / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.height / 2)

        # For top and bottom
        self.win.geometry('%dx%d+%d+%d' % (self.width,self.height,left, top))

        self.win.grid_rowconfigure(0, weight=1)
        self.win.grid_columnconfigure(0, weight=1)

        self.URLip.configure(height=4)
        self.URLip.grid(padx="20", pady="10")
        self.Search = Button(self.win, text="  SEARCH  ", bg="#00a803", bd="6", fg="#ffffff", activeforeground="#ffffff",
                        activebackground="#007a02", underline=0, command=self.convert).grid()
        self.output.configure(height=15)
        self.output.grid(padx="20", pady="10")
        self.Save = Button(self.win, text=" SAVE AS TEXT ", bg="#00a803", bd="3", fg="#ffffff", activeforeground="#ffffff",
                      activebackground="#007a02", underline=0, command=self.save).grid()
        self.footer = Label(self.win, text="Made by HAPYY CHANDRU RAJU", fg="black")


        self.footer.grid(sticky=N + E + S + W)
        self.menubar.add_cascade(label="OPTICAL CHARACTER RECOGNITION")
        self.win.minsize(800, 540)

    def convert(self):
        Path = self.URLip.get(1.0,END)
        Path = Path.rstrip()

        if os.path.exists(Path):
            img = Image.open(Path)
            text = pytesseract.image_to_string(img)
        else:
            text = "Invalid / Corrupted Image Path"


        self.output.configure(text="{}".format(text))

    def save(self):
        save_file =  asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

        if save_file == "":
            text_file = open("output.txt", "wt")
        else:
            text_file = open(save_file, "w")
            text_file.write(self.output.cget("text"))
            text_file.close()


    def run(self):
        # Run main application OCR - img to txt/ocr.py:103
        self.win.mainloop()

ocr = OCR()
ocr.run()

