import tkinter as tk


def clic(event):
    global couleur
    global rectangleFige
    x = event.x
    y = event.y
    if x > 200 and x < 300 and y > 200 and y < 300 and not rectangleFige:
        if couleur == "red":
            couleur = "blue"
            canevas.itemconfigure(1, fill=couleur)
        else:
            couleur = "red"
            canevas.itemconfigure(1, fill=couleur)
    else:
        rectangleFige = True


def reset():
    global couleur
    global rectangleFige
    couleur = "red"
    canevas.itemconfigure(1, fill=couleur)
    rectangleFige = False


fenetre = tk.Tk()
canevas = tk.Canvas(fenetre, bg="black", width=500, height=500)
bouton = tk.Button(text="Recommencer", command=reset)
couleur = "red"
rectangleFige = False

canevas.grid(row=0, column=0)
bouton.grid(row=1, column=0)
canevas.create_rectangle(200, 200, 300, 300, fill=couleur)
canevas.bind("<Button-1>", clic)

fenetre.mainloop()
