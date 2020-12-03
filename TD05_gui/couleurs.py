from tkinter import *
import random


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def drawPixel(i,j,couleur):
    c.create_rectangle(i,j,i,j,outline=couleur)

def ecran_aleatoire():
    for i in range(0,tailleCanvas):
        for j in range(0,tailleCanvas):
            couleurPixel = get_color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            drawPixel(i,j,couleurPixel)

def degrade_gris():
    for i in range(0,tailleCanvas):
        couleurPixel = get_color(i,i,i)
        for j in range(0,tailleCanvas):
            drawPixel(i,j,couleurPixel)


def degrade_2D():
    for i in range(0,tailleCanvas):
        for j in range(0,tailleCanvas):
            couleurPixel = get_color(i,0,j)
            drawPixel(i,j,couleurPixel)


tailleCanvas = 256
fonte = "Cambria"
couleurTexte = "blue"

fen = Tk()
fen.title("Couleurs")
c = Canvas(fen,width=tailleCanvas,height=tailleCanvas,bg="black")
bAleat = Button(text="Aléatoire",fg=couleurTexte,command=ecran_aleatoire)
bDegrade = Button(text="Dégradé gris",fg=couleurTexte,command=degrade_gris)
bDegrade2d = Button(text="Dégradé 2D",fg=couleurTexte,command=degrade_2D)
c.grid(row=0,column=1,rowspan=3)
bAleat.grid(row=0,column=0)
bDegrade.grid(row=1,column=0)
bDegrade2d.grid(row=2,column=0)

fen.mainloop()