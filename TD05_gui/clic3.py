from tkinter import *

def clic(event):
    x = event.x
    y = event.y
    points.append([x,y])
    print(points)
    if len(points) == 2:
        if (points[0][0] < largeur/2 and points[1][0] < largeur/2) or (points[0][0] >= largeur/2 and points[1][0] >= largeur/2):
            couleur = "blue"
        else:
            couleur = "red"
        c.create_line(points[0][0],points[0][1],x,y,fill=couleur)
        points.clear()

largeur = 500
hauteur = 500
points = []

fen = Tk()
fen.title("Clic 2")
c = Canvas(fen,width=largeur,height=hauteur,bg="black")
c.grid()
c.create_line(largeur/2,0,largeur/2,hauteur,fill="white")
c.bind("<Button-1>", clic)
fen.mainloop()