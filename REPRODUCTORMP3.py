from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os


pygame.init() #niciamos modulo pygame


#Funcion bpton abrir canción
def openFilesong():
    cancion = filedialog.askopenfile() #Guardar el nombre o canción que queremos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)

def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()

def resumeSong():
    pygame.mixer.music.unpause()

def volumenDown():
    volumenlevel = pygame.mixer.music.get_volume() - 0.1
    print(volumenlevel)
    pygame.mixer.music.set_volume(volumenlevel)

def volumenUp():
    volumenlevel = pygame.mixer.music.get_volume() + 0.1
    print(volumenlevel)
    pygame.mixer.music.set_volume(volumenlevel)



raiz = Tk()
raiz.title("Reproductor MP3")
raiz.geometry("460x400")
raiz.resizable(0,0)


#crear Frame
framePrincipal = Frame(raiz, bg="#32CD32")
framePrincipal.pack(fill="both", expand=1)

#titulo reproductor
tituloreproductor = Label(framePrincipal, text="ESPOTYFY.MP3.FREE", font=("Roboto", 20, "bold"), bg="#32CD32", fg="white")
tituloreproductor.place(relx=0.05,rely=0.05)

#Boton open song
botonOpenSong = Button(framePrincipal, text="Open\nsong", bg="#a27611", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10,height=2, cursor="spraycan", command = openFilesong)
botonOpenSong.place(relx=0.05,rely=0.7)

#Boton play song
botonPlaySong = Button(framePrincipal, text="Play\nsong", bg="#e2504c", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10,height=2, cursor="spraycan", command = playSong)
botonPlaySong.place(relx=0.23,rely=0.7)

#Boton stop song
botonStopSong = Button(framePrincipal, text="Stop\nsong", bg="#550099", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10,height=2, cursor="spraycan", command = stopSong)
botonStopSong.place(relx=0.41,rely=0.7)

#Boton pause song
botonPauseSong = Button(framePrincipal, text="Pause\nsong", bg="#23BAC4", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10,height=2, cursor="spraycan", command = pauseSong)
botonPauseSong.place(relx=0.59,rely=0.7)

#Boton resume song
botonResumeSong = Button(framePrincipal, text="Resume\nsong", bg="#ffc400", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10,height=2, cursor="spraycan", command = resumeSong)
botonResumeSong.place(relx=0.77,rely=0.7)

#Boton volumen más
botonVolumeUpSong = Button(framePrincipal, text="Volumen\nmore", bg="#42ab49", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10,height=2, cursor="spraycan", command = volumenUp)
botonVolumeUpSong.place(relx=0.23,rely=0.85)

#Boton volumen menos
botonVolumeDownSong = Button(framePrincipal, text="Volumen\nless", bg="#42ab49", font=("Roboto", 8, "bold"), fg="#fbfbfb", width=10,height=2, cursor="spraycan", command = volumenDown)
botonVolumeDownSong.place(relx=0.59,rely=0.85)

imgSong = Image.open("Jigglypuff_Sing.webp")
imagen = imgSong.resize((200,200))
imag = ImageTk.PhotoImage(imagen)

miTitulo = Label(framePrincipal, image=imag)
miTitulo.place(relx=0.3,rely=0.15)

raiz.mainloop()