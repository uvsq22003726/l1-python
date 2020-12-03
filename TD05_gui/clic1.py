from tkinter import *

def clic(event):
    c.create_rectangle((event.x,event.y)*2,outline="red")

largeur = 500
hauteur = 500

fen = Tk()
fen.title("Clic 1")
c = Canvas(fen,width=largeur,height=hauteur,bg="black")
c.grid()
c.bind("<Button-1>", clic)
fen.mainloop()