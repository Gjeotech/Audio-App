from tkinter import * 
#pip install pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk 


import pygame 
root = Tk()
root.title("Sound App")
root.geometry("750x550")

#initialize pygame mixer
pygame.mixer.init()

#Grabe song timer 
def play_time():
#grabe the current song time elapse
	current_time = pygame.mixer.music.get_pos() / 1000

	#throw uo temporary label to getdata

	slider_label.config(text=f'Slider: {int(myslider.get())} and Song Pos: {int(current_time)}')

	#convert to time format 
	convert_current_time = time.strftime('%M:%S', time.gmtime(current_time)) #'%H:%M:%S'

	
	#get the current song turple number 
	#current_song = songsListBox.curselection() #curselection is a function in pygame
		
	#grab song title from playlist
	song = songsListBox.get(ACTIVE)
	
	#add dir
	song = f'C:/Users/brand/Desktop/Tkin_Aidio/audio/{song}.mp3'

	#Get song length with Mutagen 

	#load song with Mutagen
	song_mut = MP3(song)

	global song_length  #so that wil can use it for slider progreess
	#Get song Length
	song_length = song_mut.info.length 
	#Convert to time format
	convert_Song_length = time.strftime('%M:%S', time.gmtime(song_length)) 

	#Set increase current time by 1 secon
	current_time+=1

	#TO BE CONTINUE ...
	if int(myslider.get()) == int(song_length):	
		status_bar.config(text=f'Durantion: {convert_Song_length} of  {convert_current_time} ')
	 

	if int(myslider.get()) ==int(current_time):
		#slider has not been move
		slider_position = int(song_length)
		myslider.config(to=slider_position, value=int(current_time))
	else:
		slider_position = int(song_length)
		myslider.config(to=slider_position, value=int(myslider.get()))

		#convert to time format 
		convert_current_time = time.strftime('%M:%S', time.gmtime(int(myslider.get()))) #'%H:%M:%S'
			
		#outputing the current play time with the slider status
		status_bar.config(text=f'Durantion: {convert_current_time} of  {convert_Song_length} ')
	
		#move this along by one seconds
		next_time = int(myslider.get()) +1 
		myslider.config(value=next_time)

	#status_bar.config(text=int(current_time)) #befor
	#status_bar.config(text=convert_current_time) #after befor
	#status_bar.config(text=f'Durantion: {convert_current_time} of  {convert_Song_length} ')
	
	#it was added last to get the current time as slider moves 
	#myslider.config(value=int(current_time)) 

	#Update and start up the timer in thousand micro seconds
	status_bar.after(1000, play_time)


#creat song function
def addSong():
	song = filedialog.askopenfilename(initialdir='C:/Users/brand/Desktop/Tkin_Aidio/audio/', title="choose a Song", filetypes=(("mp3 Files", "*mp3"), ))
	
	#strip out the directory infor extention from the song name
	song=  song.replace("C:/Users/brand/Desktop/Tkin_Aidio/audio/", "")
	song=  song.replace(".mp3", "")

	#add song to listbox
	songsListBox.insert(END, song)


#Add many songs to Playlist
def addManySongs():
	songs = filedialog.askopenfilenames(initialdir='C:/Users/brand/Desktop/Tkin_Aidio/audio/', title="choose a Song", filetypes=(("mp3 Files", "*mp3"), ))
	
	#loop through song list and replace directory info and mp3
	for song in songs:
		#strip out the directory infor extention from the song name
		song=  song.replace("C:/Users/brand/Desktop/Tkin_Aidio/audio/", "")
		song=  song.replace(".mp3", "")

		#insert into playlist
		songsListBox.insert(END, song)

	#play btn function
def play():
	song = songsListBox.get(ACTIVE)
	song = f'C:/Users/brand/Desktop/Tkin_Aidio/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	#Call play timer function 
	play_time()

	#Update slider to position of playing
	#slider_position = int(song_length)
	#myslider.config(to=slider_position, value=0) #setting value to 0 means whenever new music is selecte the slider should move to position 0

	#stop btn  function
def stop():
	pygame.mixer.music.stop()
	songsListBox.selection_clear(ACTIVE)

	#Clear status Bar 
	status_bar.config(text='')

#Play next next song in the play list

def next_song():
	#get the current song turple number 
	next_one = songsListBox.curselection() #curselection is a function in pygame
	#Add one to the current number (incrementing)
	#print(next_one)
	#print(next_one[0])
	
	next_one = next_one[0]+1

	#grab song title from playlist
	song = songsListBox.get(next_one)
	
	#add dir
	song = f'C:/Users/brand/Desktop/Tkin_Aidio/audio/{song}.mp3'

	#Load and play song
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	#Clear active bar color in play list box
	songsListBox.selection_clear(0, END) 

	#Activate next song bar color 
	songsListBox.activate(next_one)

	#set Active bar color to next song
	songsListBox.selection_set(next_one, last=None)
	

#create previous song btn function

def previous_song():
	#get the current song turple number 
	next_one = songsListBox.curselection() #curselection is a function in pygame
	#Add one to the current number (incrementing)
	#print(next_one)
	#print(next_one[0])
	#if next_one:
	next_one = next_one[0]-1
	
	#grab song title from playlist
	song = songsListBox.get(next_one)
	
	#add dir
	song = f'C:/Users/brand/Desktop/Tkin_Aidio/audio/{song}.mp3'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	#Clear active bar color in play list box
	songsListBox.selection_clear(0, END) 

	#Activate next song bar color 
	songsListBox.activate(next_one)

	#set Active bar color to next song
	songsListBox.selection_set(next_one, last=None)
	

def delete_song():
	#Delete and stop music if it is playing
	songsListBox.delete(ANCHOR)
	pygame.mixer.music.stop()

def delete_all_songs():
	#Delete all song and stop music if it is playing
	songsListBox.delete(0, END)
	pygame.mixer.music.stop()


#create global pause varaible		
global paused
paused = False

#pause btn function
def pause(is_paused):
	global paused 
	paused = is_paused 

	if paused:
		#Unpaused
		pygame.mixer.music.unpause()
		paused = False
	else:
		#pause
		pygame.mixer.music.pause()
		paused = True


#Create Slider Function 

def slide(x):
	#slider_label.config(text=f'{int(myslider.get())} of {int(song_length)}' )
	song = songsListBox.get(ACTIVE)
	song = f'C:/Users/brand/Desktop/Tkin_Aidio/audio/{song}.mp3'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0,start=int(myslider.get()))


#create playlist box
songsListBox = Listbox(root, bg="lightblue", fg="green", width=80, selectbackground="blue", selectforeground="white")
songsListBox.pack(pady=20)


#define player control button images
backBtnImg =  PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/back.png')
forwardImg = PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/forwd.png')
playBtnImg = PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/play.png')
stopBtnImg = PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/stop.png')
pauseBtnImg = PhotoImage(file='C:/Users/brand/Desktop/Tkin_Aidio/pause.png')

#create playe control frame

controls_frame = Frame(root)
controls_frame.pack()

#ctreate player control button 
backbtn = Button(controls_frame, image=backBtnImg, borderwidth=0, command=previous_song)
forwardbtn = Button(controls_frame, image=forwardImg, borderwidth=0, command=next_song)
playbtn = Button(controls_frame, image=playBtnImg, borderwidth=0, command=play)
stopbtn = Button(controls_frame, image=stopBtnImg, borderwidth=0, command=stop)
pausebtn = Button(controls_frame, image=pauseBtnImg, borderwidth=0,command=lambda:pause(paused))


backbtn.grid(row=0, column=0,padx=10)
forwardbtn.grid(row=0,column=1,padx=10)
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

#add manay song toplaylist
add_song_menu.add_command(label="Add many Song to Playlist", command=addManySongs)

#create delete song menu 
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Song", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

#create a status bar
status_bar = Label(root, text='Loading', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)


#Create Music Position Slider 
myslider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL,value=0,length=360, command=slide)
myslider.pack(pady=30)

#create Temporary slider label 
slider_label = Label(root, text="0")
slider_label.pack(pady=10)



root.mainloop()