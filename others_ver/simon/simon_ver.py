# Créé par s.ballaringlotain, le 20/04/2026 en Python 3.7
#importer tkinter+randint
import tkinter as tk
from PIL import Image, ImageTk
from random import randint

#créer la fenêtre
fenetre = tk.Tk()
fenetre.title = ("Pac")
fenetre.geometry("2000x1000")

#insérer les images
zone = tk.Canvas(fenetre, width = 1900 , height=950, bg='white')
zone.pack(padx =5, pady = 0)

#pacman
imgpacman = ImageTk.PhotoImage(Image.open("pacman.png").resize((200,200)))
zone.create_image(500,500,image = imgpacman, tag="pac")


#Déplacer le pacman

#Vers la gauche
def Gauche(event):
   print("Gauche")
   zone.move("pac", -100, 0)
   zone.update()
fenetre.bind("<Left>", Gauche)

#Vers le haut
def Haut(event):
    print ("Haut")
    zone.move("pac", 0, -100)
    zone.update()
fenetre.bind("<Up>", Haut)

#Vers le bas
def Bas(event):
    print ("Bas")
    zone.move("pac", 0, 100)
    zone.update()
fenetre.bind("<Down>", Bas)

#Vers la droite
def Droite(event):
    print ("Droite")
    zone.move("pac", 100, 0)
    zone.update()
fenetre.bind("<Right>", Droite)

#Bouger les fantomes
class ghost :
    def __init__ ():
        self.stack = None
    def __str__ (self) :
        #yellow
        imgyellowghost = ImageTk.PhotoImage(Image.open("yellow_ghost.png").resize((200,200)))
        zone.create_image(500,500,image = imgyellowghost, tag="yellowghost")
        #blue
        imgblueghost = ImageTk.PhotoImage(Image.open("blue_ghost.png").resize((200,200)))
        zone.create_image(500,500,image = imgyellowghost, tag="blueghost")
        #red
        imgredghost = ImageTk.PhotoImage(Image.open("red_ghost.png").resize((200,200)))
        zone.create_image(500,500,image = imgyellowghost, tag="redghost")
        #pink
        imgpinkghost = ImageTk.PhotoImage(Image.open("pink_ghost.png").resize((200,200)))
        zone.create_image(500,500,image = imgyellowghost, tag="pinkghost")
    def se_diriger ():
        dir = randint(1,4)



lst = Stack()
lst = lst.add([15, 52, 645489, 564865643])
print(lst)