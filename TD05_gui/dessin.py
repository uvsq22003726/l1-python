from tkinter import *
import random

def afficherCercle():
    x = random.randint(0,largeurCanvas-diametreCercle)
    y = random.randint(0,hauteurCanvas-diametreCercle)
    tag = c.create_oval(x,y,x+diametreCercle,y+diametreCercle,outline=couleurCercle,fill=couleurCercle)
    objets.append(tag)

def afficherCarre():
    x = random.randint(0,largeurCanvas-tailleCarre)
    y = random.randint(0,hauteurCanvas-tailleCarre)
    tag = c.create_rectangle(x,y,x+tailleCarre,y+tailleCarre,outline=couleurCarre,fill=couleurCarre)
    objets.append(tag)

def afficherCroix():
    x = random.randint(0,largeurCanvas-tailleCroix)
    y = random.randint(0,hauteurCanvas-tailleCroix)
    tag1 = c.create_line(x,y+tailleCroix/2,x+tailleCroix,y+tailleCroix/2,fill=couleurCroix,width=20)
    tag2 = c.create_line(x+tailleCroix/2,y,x+tailleCroix/2,y+tailleCroix,fill=couleurCroix,width=20)
    objets.append(tag1)
    objets.append(tag2)

def choisirCouleur():
    global couleurCarre
    global couleurCercle
    global couleurCroix
    couleur = input("Couleur : ")
    couleurCercle = couleur
    couleurCarre = couleur
    couleurCroix = couleur

def undo():
    print(objets)
    if(len(objets)>0):
        if c.type(objets[len(objets)-1]) == "line":
            c.delete(objets[len(objets)-1])
            objets.remove(objets[len(objets)-1])
        c.delete(objets[len(objets)-1])
        objets.remove(objets[len(objets)-1])


largeurCanvas, hauteurCanvas = 500,500
fonte = "Cambria"
couleurCercle = "blue"
couleurCarre = "red"
couleurCroix = "yellow"
tailleCarre = 100
tailleCroix = 100
diametreCercle = 100
objets = []

fen = Tk()
fen.title("Mon dessin")
c = Canvas(fen, width = largeurCanvas, height = hauteurCanvas,bg="black",borderwidth=3, relief="raised")
bChoix = Button(text="Choisir une couleur",borderwidth=3, relief="raised",bg="green",font=fonte,command=choisirCouleur)
bUndo = Button(text="Annuler",borderwidth=3, relief="raised",font=fonte,command=undo)
bCercle = Button(text="Cercle",borderwidth=3, relief="raised",font=fonte,command=afficherCercle)
bCarre = Button(text="Carré",borderwidth=3, relief="raised",font=fonte,command=afficherCarre)
bCroix = Button(text="Croix",borderwidth=3, relief="raised",font=fonte,command=afficherCroix)
bChoix.grid(row=0,column=1)
bUndo.grid(row=0,column=2)
bCercle.grid(row=1,column=0)
bCarre.grid(row=2,column=0)
bCroix.grid(row=3,column=0)
c.grid(row=1,column=1,rowspan=3,columnspan=2)
fen.mainloop()


