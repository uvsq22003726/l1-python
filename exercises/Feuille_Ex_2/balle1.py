from tkinter import *

largeur = 600
hauteur = 400

def creerBalle():
    c.create_oval()

def dbClic(event):
    print("Double clic")

fen = Tk()
fen.title("Balle")
c = Canvas(fen,width=largeur,height=hauteur,bg="black")
c.bind("<Double-1>",dbClic)
c.grid(row=0,column=0)
b = Button(text="Démarrer")
b.grid(row=1,column=0)

fen.mainloop()