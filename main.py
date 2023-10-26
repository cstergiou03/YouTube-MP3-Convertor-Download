import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import *
from pytube import * 
import re
import os

download_path = None

def convert():
    url = entry_widget1.get()
    download(url)

def download(url):

    try:
        global download_path
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        title = re.sub(r'[\/:*?"<>|]', '', video.title)
        if not download_path:
            title = re.sub(r'[\/:*?"<>|]', '', video.title)
            download_path = os.path.expanduser("~/Downloads") 
            statusbar.config(text=download_path)
        stream.download(output_path= download_path , filename=f"{title}.mp3")
        canvas.delete("message")
        canvas.create_text(300, 300, text="Download completed", font=("Helvetica", 20), fill="green", tags="message")
        entry_widget1.delete(0, tk.END) 
    except:
        canvas.delete("message")
        canvas.create_text(300, 300, text="Error with the download", font=("Helvetica", 20), fill="red", tags="message")
        

def path_select():
    global download_path  
    download_path = askdirectory(title="Folder")
    statusbar.config(text=download_path)

 

window = tk.Tk()
window.title("MP3 Convertor")
window.geometry("600x600") 
window.maxsize(600, 600) 

canvas = tk.Canvas(window, width=570, height=570)
canvas.pack()

canvas.create_text(285, 125, text="YouTube Link", font=("Helvetica", 24))

entry_widget1 = tk.Entry(window) 
canvas.create_window(285, 160, window=entry_widget1, width=400, height=25) 

button = Button(window, text="Convert & Download", command=convert)
button.pack()
button.place(x=235, y=180)

button2 = Button(window, text="...", command=path_select)
button2.pack()
button2.place(x=510, y=148)

statusbar = tk.Label(window, text="Default: /Download", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

window.mainloop()