import socket
from threading import Thread

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from playsound import playsound
import pygame
from pygame import mixer
import os 
import time


IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
infoLabel = None
filePathLabel = None
song_selected = None
song_counter = 0

for file in os.listdir('shared_files'):
    file_name = os.fsdecode(file)
    listbox.insert(song_counter, filename)
    song_counter += 1

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)
    
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: "+song_selected)
    else:
        infoLabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_flies/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    selectLabel = Label(window, text="Select Song", bg='LightSkyBlue', font = ('Calibri',8))
    selectLabel.place(x=2, y=1)

    listbox = Listbox(window, height=10, width=39, activestyle='dotbox', bg='LightSkyBlue', borderwidth=2, font = ('Calibri',10))
    listbox.place(x=10, y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command = listbox.yview)

    PlayButton = Button(window, text="Play", width=10, bd=1, bg="SkyBlue", font = ('Calibri',10), command=play)
    PlayButton.place(x=30, y=200)

    Stop = Button(window, text="Stop", width=10, bd=1, bg="SkyBlue", font = ('Calibri',10), command=stop)
    Stop.place(x=200, y=200)

    Upload = Button(window, text="Upload", width=10, bd=1, bg="SkyBlue", font = ('Calibri',10))
    Upload.place(x=30, y=250)

    Download = Button(window, text="Download",  width=10, bd=1, bg="SkyBlue", font = ('Calibri',10))
    Download.place(x=200, y=250)

    infoLabel = Label(window, text="", fg="blue", font=("Calibri", 8))
    infoLabel.place(x=4, y=280)

    window.mainloop()

def setup():
    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    musicWindow()

setup()

