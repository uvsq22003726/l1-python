from tkinter import *

def clic(event):
    global nbClics
    nbClics += 1
    if nbClics % 2:
        c.itemconfigure(1,fill="green")
    else:
        c.itemconfigure(1,fill='')
    if nbClics == 10:
        fen.destroy()

largeur = 500
hauteur = 500
nbClics = 0

fen = Tk()
fen.title("Clic 2")
c = Canvas(fen,width=largeur,height=hauteur,bg="black")
c.grid()
c.create_rectangle(largeur/2-50,hauteur/2-50,largeur/2+50,hauteur/2+50,outline="yellow")
c.bind("<Button-1>", clic)
fen.mainloop()