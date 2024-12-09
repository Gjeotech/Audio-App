from tkinter import * 
#pip install pygame
import pygame 
root = Tk()
root.title("Sound App")
root.geometry("500x400")

pygame.mixer.init()


def sound():
	pygame.mixer.music.load("C:/Users/brand/Desktop/Tkin_Aidio/audio/sound3.mp3")
	pygame.mixer.music.play()


def stop():
	pygame.mixer.music.stop()
	


myBtn = Button(root, text="Play Sound",font=("Helvitical", 22), command=sound)
myBtn.pack(pady=20)


stopBtn = Button(root, text='Stop', command=stop)
stopBtn.pack(pady=20,ipadx=40)

root.mainloop()