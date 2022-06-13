# Importing Required Modules & libraries
from ast import Raise
from textwrap import fill
from tkinter import *
import pygame
import os
from tkinter import filedialog
# Defining MusicPlayer Class
class MusicPlayer:
  # Defining Constructor
  def __init__(self,root):
    self.root = root
    self.root.title("MP3 Player".upper())
    self.root.geometry("440x360")
    # adding Open Button to MP3 Folder
    def songTrack():
      song_folder = filedialog.askdirectory(initialdir='/')
      os.chdir(song_folder)
      songtracks = os.listdir()
      for track in songtracks:
        self.playlist.insert(END, track)
    menu = Menu()
    self.root.config(menu=menu)
    fileMenu = Menu(menu)
    menu.add_cascade(label="Open Folder", command=songTrack)
    pygame.init()
    pygame.mixer.init()
    # Declaring track Variable
    self.track = StringVar()
    self.status = StringVar()
    # Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root,text="Now Playing".upper(),font=("Arial Black",10,"bold"),bg="Green",fg="black",relief=FLAT)
    trackframe.place(x=0,y=0,width=440,height=80)
    # Inserting Song Track Label
    songtrack = Label(trackframe,textvariable=self.track,width=20,font=("Arial Black",15),bg="Green",fg="black").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Status Label
    trackstatus = Label(trackframe,textvariable=self.status,font=("Arial Black",15,"bold"),fg="black").grid(row=0,column=1,padx=10,pady=5)

    # Creating Button Frame
    buttonframe = LabelFrame(self.root,text="Control Panel".upper(),font=("Arial Black",13,"bold"),bg="white",fg="black",relief=FLAT)
    buttonframe.place(x=0,y=280,width=440,height=80)
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("Arial Black",10,"bold"),fg="navyblue",bg="green").grid(row=0,column=0,padx=10,pady=5)
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("Arial Black",10,"bold"),fg="navyblue",bg="Orange").grid(row=0,column=1,padx=10,pady=5)
    playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("Arial Black",10,"bold"),fg="navyblue",bg="DarkOrange").grid(row=0,column=2,padx=10,pady=5)
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("Arial Black",10,"bold"),fg="navyblue",bg="Red").grid(row=0,column=3,padx=10,pady=5)

    # Creating Playlist Frame
    songsframe = LabelFrame(self.root,text="Playlist".upper(),font=("Arial Black",15),bg="white",fg="Black",relief=FLAT)
    songsframe.place(x=0,y=80,width=440,height=200)
    # Inserting scrollbar
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="green",selectmode=SINGLE,font=("Arial Black",10,"bold"),bg="white",fg="black",relief=FLAT)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill=Y)
    #scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)

    
  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set(self.playlist.get(ACTIVE))
    # Displaying Status
    self.status.set("Playing".upper())
    # Loading Selected Song
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()
    

  def stopsong(self):
    # Displaying Status
    self.status.set("Stopped".upper())
    # Stopped Song
    pygame.mixer.music.stop()

  def pausesong(self):
    # Displaying Status
    self.status.set("Paused".upper())
    # Paused Song
    pygame.mixer.music.pause()
    

  def unpausesong(self):
    # Displaying Status
    self.status.set("Playing".upper())
    # Playing back Song
    pygame.mixer.music.unpause()

# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()