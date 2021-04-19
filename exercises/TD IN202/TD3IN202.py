import tkinter as tk


fen = tk.Tk()
fen.title("Mon Petit Photoshop")
canvas = tk.Canvas(fen, width=500, height=500, bg="grey")
btCharger = tk.Button(fen, text="Charger")
btQuitter = tk.Button(fen, text="Quitter")
btFiltreVert = tk.Button(fen, text="Filtre vert")
btNegatif = tk.Button(fen, text="Négatif")
btSymetrique = tk.Button(fen, text="Symétrique")
btGris = tk.Button(fen, text="Gris")
label = tk.Label(text="MAOUCHE Clément 22003726",fg="green")

canvas.grid(row=0, column=1, rowspan=4, columnspan=2)
btCharger.grid(row=4, column=0)
btQuitter.grid(row=4, column=2)
btFiltreVert.grid(row=0, column=0)
btNegatif.grid(row=1, column=0)
btSymetrique.grid(row=2, column=0)
btGris.grid(row=3, column=0)
label.grid(row=4,column=1)

fen.mainloop()