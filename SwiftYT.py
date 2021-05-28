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

URL_input_area = Entry(root, width = 50).place(x=130, y=400)

#Video Quality

Quality = Label(root, text = "Choose Quality").place(x = 40, y = 450)

Quality_input_area = Entry(root, width = 50).place(x=130, y=450)




#placing character

canvas = Canvas(root, width=1000, height=1000)      
canvas.pack()      
img = PhotoImage(file="charachter.png")      
canvas.create_image(20, 20, anchor=NW, image=img)    
canvas.place(x=850, y=50)

#Placing TITLE
c = Canvas(root, width=640, height=300)      
c.pack()         
img2 = PhotoImage(file="title.png")      
c.create_image(20, 20, anchor=NW, image=img2)    
c.place(x=50, y=50)


root.mainloop()