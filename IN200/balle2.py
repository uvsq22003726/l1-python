import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
couleursZones = ["red","green","blue","yellow"]


###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    changementCouleur()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        if y1 >= 400:
            c.itemconfig(balle[0],)


def changementCouleur():
    global balle
    coordsXY = canvas.coords(balle[0])
    coordsCentre = [(coordsXY[0]+coordsXY[2])/2,(coordsXY[1]+coordsXY[3])/2]
    if coordsCentre[1] <= 50:
        indexRectangle = int(coordsCentre[0]/(LARGEUR/4))
        canvas.itemconfig(balle[0],fill=couleursZones[indexRectangle])


######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()

for i in range(4):
    canvas.create_rectangle(LARGEUR/4*i,0,LARGEUR/4*(i+1),50,fill=couleursZones[i])

balle = creer_balle()
mouvement()



racine.mainloop()
