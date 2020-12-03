from tkinter import *

fen = Tk()
fen.title("Fenêtre")
l1 = Label(fen,text="12",borderwidth=2, relief="raised")
l2 = Label(fen,text="+",borderwidth=2, relief="raised")
l3 = Label(fen,text="25",borderwidth=2, relief="raised")
l4 = Label(fen,text="=",borderwidth=2, relief="raised")
l5 = Label(fen,text="37",borderwidth=2, relief="raised")
l6 = Label(fen,text="choisir une valeur pour l'opérande gauche",borderwidth=2, relief="raised")
l7 = Button(fen,text="calculer",borderwidth=2, relief="raised")
l8 = Label(fen,text="choisir une valeur pour l'opérande droite",borderwidth=2, relief="raised")

l1.grid(column=1, row=0)
l2.grid(column=2,row=0)
l3.grid(column=3, row=0)
l4.grid(column=4,row=0)
l5.grid(column=5, row=0)
l6.grid(column=0,row=1) 
l7.grid(column=1, row=1, columnspan=5)
l8.grid(column=0, row=2)
fen.mainloop()

# fenLarg = 800
# fenHaut = 800
# nbCasesX = 8
# nbCasesY = 8
# fen = Tk()
# fen.title("Fenêtre")
# canva = Canvas(width=fenLarg,height=fenHaut)
# canva.grid()
# for i in range(0,8):
#     for j in range(0,8):
#         if(i+j)%2:
#             couleur = "black"
#         else:
#             couleur = "white"
#         canva.create_rectangle(i*fenLarg/nbCasesX,j*fenHaut/nbCasesY,i*fenLarg/nbCasesX+fenLarg/nbCasesX,j*fenHaut/nbCasesY+fenHaut/nbCasesY,fill=couleur)
# fen.mainloop()