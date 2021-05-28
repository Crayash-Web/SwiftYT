#YouTube Video Downloader By YASH

#SwiftYT

import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from pytube import YouTube
from PIL import ImageTk, Image



root = tk.Tk()
root.title("SwiftYT - Youtube Video Downloader")
label = Label(root, text ="NOTE: YOU MUST HAVE AN INTERNET CONNECTION").pack()

# the label for url 
URL = Label(root, text = "Enter URL").place(x = 40, y = 400)

URL_input_area = Entry(root, width = 50).place(x=110, y=400)

#placing character

canvas = Canvas(root, width=1000, height=1000)      
canvas.pack()      
img = PhotoImage(file="charachter.png")      
canvas.create_image(20, 20, anchor=NW, image=img)    
canvas.place(x=850, y=50)

                                                            

root.mainloop()