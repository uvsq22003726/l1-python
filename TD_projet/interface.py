import tkinter as tk

largeur = 500
hauteur = 500

fen = tk.Tk()
grille = tk.Frame(fen,bg="orange")
b = []
for i in range(0,9):
    b.append(tk.Button(grille,text=i))
    b[i].grid(row=int(i/3),column=int(i%3))
grille.grid_propagate(100)
grille.columnconfigure(0,weight=1)
grille.columnconfigure(1,weight=1)
grille.columnconfigure(2,weight=1)
grille.pack()
fen.mainloop()