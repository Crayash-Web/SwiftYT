#YouTube Video Downloader By YASH

#SwiftYT

import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from pytube import YouTube
from PIL import Image, ImageTk


root = tk.Tk()
root.title("SwiftYT - Youtube Video Downloader")
label = Label(root, text ="WELCOME..!!").pack()

# the label for url 
URL = Label(root, text = "Enter URL").place(x = 40, y = 60)

URL_input_area = Entry(root, width = 50).place(x=110, y=60)



                  
                                          

root.mainloop()