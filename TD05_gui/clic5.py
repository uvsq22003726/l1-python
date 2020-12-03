from tkinter import *

def clic(event):
    global nbClics
    nbClics += 1
    x = event.x
    y = event.y
    if nbClics <= 8:
        c.create_oval(x-25,y-25,x+25,y+25,outline="red",fill="red")
    if nbClics == 9:
        for i in c.find_all():
            c.itemconfigure(i,outline="yellow",fill="yellow")
    if nbClics == 10:
        c.delete("all")
        nbClics = 0

largeur = 500
hauteur = 500
nbClics = 0

fen = Tk()
fen.title("Clic 2")
c = Canvas(fen,width=largeur,height=hauteur,bg="black")
c.grid()

c.bind("<Button-1>", clic)
fen.mainloop()