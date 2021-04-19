import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400


###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = 1+150 // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    if compteur < 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.move(mur1,1,0)
        canvas.move(mur2,1,0)
        canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    global compteur
    coordsMur1 = canvas.coords(mur1)
    coordsMur2 = canvas.coords(mur2)
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= coordsMur1[0] and balle[1] < 0:
        balle[1] = -balle[1]
        compteur += 1
    elif x1 >= coordsMur2[0]:
        balle[1] = -balle[1]
        compteur += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        compteur += 1


######################
# programme principal

global compteur
compteur = 0

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
mur1 = canvas.create_line(1,0,1,HAUTEUR,fill="white")
mur2 = canvas.create_line(150,0,150,HAUTEUR,fill="white")
balle = creer_balle()
mouvement()
racine.mainloop()
