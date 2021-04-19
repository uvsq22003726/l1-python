from tkinter import *
import random
import time


def creerBalle():
    return [c.create_oval(300-rayonBalle,200-rayonBalle,300+rayonBalle,200+rayonBalle,fill="blue"), random.randint(1,7), random.randint(1,7)]


def demarrerMouvement():
    global simulation
    simulation = not simulation
    if simulation:
        boutonDemarrer.config(text="Arrêter")
    else:
        boutonDemarrer.config(text="Démarrer")
    
    mouvement(balle1)

def mouvement(balle):
    global simulation, directionBalleX, directionBalleY
    if simulation:
        c.move(balle[0],directionBalleX,directionBalleY)
        rebond2(balle)
        fen.after(10,lambda:mouvement(balle))


def rebond1(balle):
    global directionBalleX, directionBalleY
    coords = c.coords(balle[0])
    if coords[0] <= 0:
        directionBalleX *= -1
    if coords[2] >= largeurCanvas:
        directionBalleX *= -1
    if coords[1] <= 0:
        directionBalleY *= -1
    if coords[3] >= hauteurCanvas:
        directionBalleY *= -1


def rebond2(balle):
    coords = c.coords(balle[0])
    if coords[0] <= 0:
        c.move(balle[0],largeurCanvas-2*rayonBalle,0)
    if coords[2] >= largeurCanvas:
        c.move(balle[0],-largeurCanvas+2*rayonBalle,0)
    if coords[1] <= 0:
        c.move(balle[0],0,hauteurCanvas-2*rayonBalle)
    if coords[3] >= hauteurCanvas:
        c.move(balle[0],0,-hauteurCanvas+2*rayonBalle)

global simulation
simulation = False
rayonBalle = 20
global directionBalleX
directionBalleX = 1
global directionBalleY
directionBalleY = 2
largeurCanvas = 600
hauteurCanvas = 400
nbCasesX = 20
nbCasesY = 20
largeurCase = largeurCanvas/nbCasesX
hauteurCase = hauteurCanvas/nbCasesY

fen = Tk()
fen.title("Feuille d'exercices 2")
c = Canvas(fen,width=largeurCanvas,height=hauteurCanvas,bg="black")
balle1 = creerBalle()
boutonDemarrer = Button(fen,text="Démarrer",command=demarrerMouvement,bg="yellow")
c.grid(row=0)
boutonDemarrer.grid(row=1)

for i in range(nbCasesX):
    for j in range(nbCasesY):
        c.create_rectangle(largeurCase*j,hauteurCase*i,largeurCase*(j+1),hauteurCase*(i+1),outline="yellow")

fen.mainloop()