# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import * 
import math
  
class Graphique(Toplevel): 
    fonction = 1
    def __init__(self, fonction, master = None): 
        super().__init__(master = master)
        largeurCanvas = 500
        hauteurCanvas = 500
        echelleX = 10
        echelleY = 25
        pasGraduationX = 2
        pasGraduationY = 2
        coordEtiquette = [40,20]
        calculPossible = True
        listePoints = []
        couleurGrille = '#{:02x}{:02x}{:02x}'.format(200, 200, 200)
        self.resizable(width=False,height=False)
        self.title("Courbe")
        c = Canvas(self,width=largeurCanvas,height=hauteurCanvas,bg="white")
        c.create_line(0,hauteurCanvas/2,largeurCanvas,hauteurCanvas/2)
        c.create_line(largeurCanvas/2,hauteurCanvas,largeurCanvas/2,0)
        for i in range(0,largeurCanvas+1):
            x = (i - largeurCanvas/2)/(largeurCanvas/echelleX)
            y = 0
            if fonction == 1:
                y = math.pow(x,2)
                c.create_text(coordEtiquette,text="y = x^2")
            elif fonction == 2:
                if x >= 0:
                    y = math.sqrt(x)
                    calculPossible = True
                    c.create_text(coordEtiquette,text="Racine carrée")
                else:
                    calculPossible = False
            elif fonction == 3:
                if x > 0:
                    y = math.log(x)
                    calculPossible = True
                    c.create_text(coordEtiquette,text="y = ln(x)")
                else:
                    calculPossible = False
            else:
                y = math.exp(x)
                c.create_text(coordEtiquette,text="y = exp(x)")
            j = hauteurCanvas/2 - (y*hauteurCanvas/echelleY)
            #print("x=",x,"y=","{:.2f}".format(y),"i=","{:.0f}".format(i),"j=","{:.0f}".format(j))
            if calculPossible:
                listePoints.append([int(i),int(j)])
            if math.modf(x)[0] == 0 and x%pasGraduationX == 0:
                c.create_text(i,hauteurCanvas/2+10,text=x)
                c.create_line(i,hauteurCanvas/2-5,i,hauteurCanvas/2+5)
                c.create_line(i,0,i,hauteurCanvas,fill=couleurGrille)
        for j in range(0,hauteurCanvas):
            y = (j - hauteurCanvas/2)/(hauteurCanvas/echelleY)
            if math.modf(y)[0] == 0  and y%pasGraduationY == 0 and y != 0:
                c.create_text(largeurCanvas/2-15,hauteurCanvas-j,text=y)
                c.create_line(largeurCanvas/2-5,hauteurCanvas-j,largeurCanvas/2+5,hauteurCanvas-j)
                c.create_line(0,hauteurCanvas-j,largeurCanvas,hauteurCanvas-j,fill=couleurGrille)
        print(listePoints)
        c.create_line(listePoints,fill="red",width=2)
        c.pack()
fen = Tk() 
fen.geometry("200x200") 
label = Label(fen, text ="This is the main window") 
label.pack(side = TOP, pady = 10) 
btn = Button(fen,text ="Click to open a new window") 
btn.bind("<Button>",lambda e: Graphique(1,fen))
btn.pack(pady = 10)
nouvFen = Graphique(1,fen)
fen.mainloop()

