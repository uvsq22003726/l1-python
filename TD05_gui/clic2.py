from tkinter import *

def clic(event):
    x = event.x
    y = event.y
    if x<largeur/2:
        couleur = "blue"
    else:
        couleur = "red"
    c.create_oval(x-50,y-50,x+50,y+50,outline=couleur,fill=couleur)

largeur = 500
hauteur = 500

fen = Tk()
fen.title("Clic 2")
c = Canvas(fen,width=largeur,height=hauteur,bg="black")
c.grid()
c.create_line(largeur/2,0,largeur/2,hauteur,fill="white")
c.bind("<Button-1>", clic)
fen.mainloop()