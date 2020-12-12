from tkinter import *

largeurTexte = 100
hauteurTexte = 20

f = open("exemple.txt","r")
print(f.read())
print(f.read())
fen = Tk()
fen.title("Editeur de texte")
texte = Text(fen, width=largeurTexte, height=hauteurTexte,bg="yellow")
texte.insert(END,"ceci est un test")
texte.grid()



fen.mainloop()