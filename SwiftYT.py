#YouTube Video Downloader By YASH

#SwiftYT

import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from PIL import ImageTk, Image



root = Tk()
root.geometry("1280x720")
root.title("SwiftYT - Youtube Video Downloader")
label = Label(root, text ="NOTE: YOU MUST HAVE AN INTERNET CONNECTION").pack()

# the label for url - TKINTER
URL = Label(root, text = "Enter URL").place(x = 40, y = 350)

URL_input_area = Entry(root, width = 50).place(x=130, y=350)



#Video Quality

Quality = Label(root, text = "Choose Quality").place(x = 40, y = 400)

Quality_input_area = Entry(root, width = 50).place(x=130, y=400)




#placing character

canvas = Canvas(root, width=1000, height=1000)      
canvas.pack()      
img = PhotoImage(file="charachter.png")      
canvas.create_image(20, 20, anchor=NW, image=img)    
canvas.place(x=850, y=50)

#Placing TITLE
c = Canvas(root, width=640, height=120)      
c.pack()         
img2 = PhotoImage(file="title.png")      
c.create_image(20, 20, anchor=NW, image=img2)    
c.place(x=50, y=50)


root.mainloop()

#Processing URL - PYHTON

str_url = str(URL)

yt = YouTube(str_url)
print(yt.title)