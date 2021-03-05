import tkinter as tk

largeurTexte = 50
hauteurTexte = 10

def afficher(texteBouton):
    l.config(text=texte.get())

fen = tk.Tk()
fen.title("Exercice bonus")
texte = tk.Entry(fen,bg="yellow")
b1 = tk.Button(text="Bouton 1",command=lambda : l.config(text="Appui bouton 1"))
b2 = tk.Button(text="Bouton 2",command=lambda : l.config(text="Appui bouton 2"))
b3 = tk.Button(text="Afficher le texte",command=lambda : afficher(texte.cget("text")))
l = tk.Label(text="Label")
texte.grid(row=1,column=0,columnspan=2)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=2,column=0,columnspan=2)
l.grid(row=3,column=0,columnspan=2)
fen.mainloop()