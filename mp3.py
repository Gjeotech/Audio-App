from tkinter import * 
#pip install pygame
from tkinter import filedialog

import pygame 
root = Tk()
root.title("Sound App")
root.geometry("500x400")

#initialize pygame mixer
pygame.mixer.init()

#creat song function
def addSong():
	song = filedialog.askopenfilename(initialdir='C:/Users/brand/Desktop/Tkin_Aidio/audio/', title="choose a Song", filetypes=(("mp5 Files", "*mp3"), ))
	
	#strip out the directory infor extention from the song name
	song=  song.replace("C:/Users/brand/Desktop/Tkin_Aidio/audio/", "")
	song=  song.replace(".mp3", "")

	#add song to listbox
	sounsListBox.insert(END, song)


def play():
	song = sounsListBox.get(ACTIVE)
	song = f'C:/Users/brand/Desktop/Tkin_Aidio/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)


def stop():
	pygame.mixer.music.stop()
	sounsListBox.selection_clear(ACTIVE)

#create playlist box
sounsListBox = Listbox(root, bg="lightblue", fg="green", width=80, selectbackground="blue", selectforeground="white")
sounsListBox.pack(pady=20)


#define player control button images
backBtnImg =  PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/back.png')
forwardBtnImg =PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/forwd.png')
playBtnImg = PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/play.png')
stopBtnImg = PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/stop.png')
pauseBtnImg = PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/pause.png')

#create playe control frame

controls_frame = Frame(root)
controls_frame.pack()

#ctreate player control button 
backbtn = Button(controls_frame, image=backBtnImg, borderwidth=0)
forwardBtnImg = Button(controls_frame, image=forwardBtnImg, borderwidth=0)
playbtn = Button(controls_frame, image=playBtnImg, borderwidth=0, command=play)
stopbtn = Button(controls_frame, image=stopBtnImg, borderwidth=0, command=stop)
pausebtn = Button(controls_frame, image=pauseBtnImg, borderwidth=0)


backbtn.grid(row=0, column=0,padx=10)
forwardBtnImg.grid(row=0, column=2,padx=10)
playbtn.grid(row=0, column=2,padx=10)
stopbtn.grid(row=0, column=3,padx=10)
pausebtn.grid(row=0, column=4,padx=10)

#creat menue

my_menu = Menu(root)
root.config(menu=my_menu)

#add song to Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Song", menu=add_song_menu)
add_song_menu.add_command(label="Add one Song to Playlist", command=addSong)


root.mainloop()