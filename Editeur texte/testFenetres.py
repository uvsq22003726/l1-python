from tkinter import *

def creerFen():
    nouvelleFen = Toplevel(fen)
    nouvelleFen.title("Deuxieme fenêtre")
    l = Label(nouvelleFen,text="Texte de la 2eme fenêtre")
    l.grid()

largeurTexte = 100
hauteurTexte = 20


fen.title("Premiière fenêtre")
texte = Text(fen, width=largeurTexte, height=hauteurTexte,bg="yellow")
texte.insert(END,"ceci est un test")
texte.grid()
b = Button(fen,text="nouvelle fenêtre",command=creerFen)
b.grid()


fen.mainloop()