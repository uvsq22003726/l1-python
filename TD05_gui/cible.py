from tkinter import *

largeur, hauteur = 800,800
couleurs = ["blue", "green", "black", "yellow", "magenta", "red"]
nbCercles = 24
pas = 0.02

fen = Tk()
fen.title("Cible")
c = Canvas(fen,width=largeur,height=hauteur,bg="black",)
c.grid()
for i in range(nbCercles):
    print(i*pas*largeur,i*pas*hauteur,largeur-largeur*pas*i,hauteur-hauteur*pas*i)
    indiceCouleur = i%6
    c.create_oval(i*pas*largeur,i*pas*hauteur,largeur-largeur*pas*i,hauteur-hauteur*pas*i,outline=couleurs[indiceCouleur],fill=couleurs[indiceCouleur])
fen.mainloop()