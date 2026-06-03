# Créé par r.ballaringlotain, le 12/01/2026 en Python 3.7
import tkinter as tk
from PIL import Image, ImageTk
from random import randint

#créer
fenetre = tk.Tk()
fenetre.title = ("Pac")
fenetre.geometry("2000x1000")

#Créer pacman
zone = tk.Canvas(fenetre, width = 1900 , height=950, bg='white')
zone.pack(padx =5, pady = 0)
imgpacman = ImageTk.PhotoImage(Image.open("pacman.png").resize((200,200)))
pos_pcx = 500
pos_pcy = 500
zone.create_image(pos_pcx,pos_pcy,image = imgpacman, tag="pac")

#Déplacer le pacman
def Gauche(event):
   print("Gauche")
   move_pacman()
   zone.move("pac", -100, 0)
   zone.update()
   move_ghost()
fenetre.bind("<Left>", Gauche)

def Haut(event):
    print ("Haut")
    move_pacman()
    zone.move("pac", 0, -100)
    zone.update()
    move_ghost()
fenetre.bind("<Up>", Haut)

def Bas(event):
    move_pacman()
    print ("Bas")
    zone.move("pac", 0, 100)
    zone.update()
    move_ghost()
fenetre.bind("<Down>", Bas)

def Droite(event):
    move_pacman()
    print ("Droite")
    zone.move("pac", 100, 0)
    zone.update()
    move_ghost()
fenetre.bind("<Right>", Droite)


#Ghost
ghost_blue = ImageTk.PhotoImage(Image.open("pacman-blue.png").resize((200,200)))
posx_gb = 200
posy_gb = 200
zone.create_image(posx_gb, posy_gb, image = ghost_blue, tag="ghostblue")
#def move_blue (event):
#    for i in range(10):
 #       zone.move(""ghostblue", 100, 0)
  #      zone.update()
   #     zone.after(1000)
#fenetre.bind("<space>","move_blue)"

def move_ghost():
    global posx_gb , posy_gb
    x = randint(1,4)

    while(posy_gb >= 950):
        x = randint(1,4)
    while(posx_gb >= 1900):
        x = randint(1,4)
    if (x == 1):
        zone.move("ghostblue", -100, 0)
        posx_gb -= 100
        zone.update()
        zone.after(1000)
    if (x == 2):
        zone.move("ghostblue", 0, -100)
        posy_gb -= 100
        zone.update()
    if (x == 3):
        zone.move("ghostblue", 0, 100)
        posy_gb += 100
        zone.update()
    if (x == 4):
        zone.move("ghostblue", 100, 0)
        posx_gb += 100
        zone.update()

def move_pacman():
    global pos_pcx , pos_pcy
    if (pos_pcy >= 950):
        zone.move("pac", 0, -100)
        zone.update()
    if (pos_pcy <= 0):
        zone.move("pac", 0, 100)
        zone.update()
    if (pos_pcx >= 1900):
        zone.move("pac", -100, 0)
        zone.update()
    if (pos_pcx <= 0):
        zone.move("pac", 100, 0)
        zone.update()


ghost_red = ImageTk.PhotoImage(Image.open("pacman-red.png").resize((200,200)))
zone.create_image(300,300,image = ghost_red, tag="ghostred")
#def move_red (event):
    #for i in range(10):
        #zone.move("ghostred", 0, 100)
        #zone.update()
        #zone.after(1000)
#fenetre.bind("<space>",move_red)
  # if (posy_gb >= 950):
       # zone.move("ghostblue", 0, -100)
        #zone.update()
    #if (posy_gb <= 0):
       # zone.move("ghostblue", 0, 100)
       # zone.update()
    #if (posx_gb >= 1900):
       # zone.move("ghostblue", -100, 0)
        #zone.update()
    #if (posx_gb <= 0):
        #zone.move("ghostblue", 100, 0)
       # zone.update()

move_ghost()
fenetre.mainloop()