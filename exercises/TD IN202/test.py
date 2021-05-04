l = [(0,1),(1,0),(1,1)]
print((0,1) in l)
from tkinter import *


def afficherPan1():
    panMenu.destroy()
    pan1.pack()

def afficherPan2():
    panMenu.destroy()
    pan2.pack()



fen = Tk()
fen.geometry("300x300")
panMenu = Frame(fen)
pan1 = Frame(fen)
pan2 = Frame(fen)
c1 = Canvas(pan1,width=300,height=300,bg="yellow")
c2 = Canvas(pan2,width=300,height=300,bg="green")

b1 = Button(panMenu,text="Panneau 1",command=afficherPan1)
b2 = Button(panMenu,text="Panneau 2",command=afficherPan2)

b1.grid(row=0)
b2.grid(row=1)
c1.pack()
c2.pack()
panMenu.pack()

fen.mainloop()
