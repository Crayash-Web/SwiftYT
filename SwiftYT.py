#YouTube Video Downloader By YASH

#SwiftYT

import tkinter as tk
from pytube import YouTube

def swiftdownlod():
    if(getURL.get() == ""):
        messagebox.showinfo("ERROR", "No URL is Entered")
        return
    elif (getLoc.get() == ""):
        messagebox.showinfo("ERROR", "Specify Location Correctly")
        return

    select = listbox.curselection()
    quality = videos[select[0]]
    location = getLoc.get()
    quality.download(location)
    messagebox.showinfo("Downloaded Successfully....!!!!")


def swiftURL():

    url = getURL.get()
    print(url)

    global yt
    yt = YouTube(url)
    print(yt.title)

    global videos
    videos = yt.streams.filter(mime_type='video/mp4').all()

    count = 1
    for i in videos:
        listbox.insert(END, str(count)+". "+str(i)+"\n\n")
        count += 1

def swiftBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)

def swiftReset():
    getURL.set("")
    getLoc.set("")
    listbox.delete(0,END)

root = tk.Tk()

root.mainloop()