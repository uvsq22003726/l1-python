import tkinter as tk
import math

class Graphique(tk.Toplevel): 
    fonction = 1
    def __init__(self, fonction, master = None): 
        super().__init__(master = master)
        largeurCanvas = 500
        hauteurCanvas = 500
        echelleX = 10
        echelleY = 10
        pasGraduationX = 1
        pasGraduationY = 1
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
                print("x=",x)
            if math.modf(x)[0] == 0 and x%pasGraduationX == 0:
                print(x)
                c.create_text(i-15,hauteurCanvas/2+10,text=x)
                c.create_line(i,hauteurCanvas/2-5,i,hauteurCanvas/2+5)
                if x != 0:
                    c.create_line(i,0,i,hauteurCanvas,fill=couleurGrille)
        for j in range(0,hauteurCanvas):
            y = (j - hauteurCanvas/2)/(hauteurCanvas/echelleY)
            if math.modf(y)[0] == 0  and y%pasGraduationY == 0 and y != 0:
                c.create_text(largeurCanvas/2-15,hauteurCanvas-j+10,text=y)
                c.create_line(largeurCanvas/2-5,hauteurCanvas-j,largeurCanvas/2+5,hauteurCanvas-j)
                c.create_line(0,hauteurCanvas-j,largeurCanvas,hauteurCanvas-j,fill=couleurGrille)
        c.create_line(listePoints,fill="red",width=2)
        c.pack()


#la partie de kubi
CANVAS_WIDTH, CANVAS_HEIGHT = 400, 550 


root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg= "blue")

ecran = canvas.create_rectangle(20, 20, 380, 180, fill = "white")
bouton1 = canvas.create_rectangle(20, 240, 105, 180+40+80, fill = "white", outline = "grey")
bouton2 = canvas.create_rectangle(105, 240, 190, 180+40+80, fill = "white", outline = "grey")
bouton3 = canvas.create_rectangle(190, 240, 275, 180+40+80, fill = "white", outline = "grey")
boutonplus = canvas.create_rectangle(190 + 20 + 85, 240, 275 + 85 + 20, 180+40+80, fill = "white", outline = "grey")

canvas.create_text((62.5, 270), text="1")
canvas.create_text(((105 + 190) / 2, (240 + 180+40+80) / 2 ), text="2")
canvas.create_text(((190 + 275) / 2, (240 + 180+40+80) / 2 ), text="3")
canvas.create_text(((190 + 20 + 85 + 275 + 85 + 20) / 2, (240 + 180+40+80) / 2 ), text="+")

bouton4 = canvas.create_rectangle(20, 240 + 60 , 105, 180+40+80 + 60, fill = "white", outline = "grey")
bouton5 = canvas.create_rectangle(105, 240 + 60, 190, 180+40+80 + 60, fill = "white", outline = "grey")
bouton6 = canvas.create_rectangle(190, 240 + 60, 275, 180+40+80 + 60, fill = "white", outline = "grey")
boutonmoins = canvas.create_rectangle(190 + 20 + 85, 240 + 60, 275 + 85 + 20, 180+40+80 + 60, fill = "white", outline = "grey")

canvas.create_text(((20 + 105) / 2, (300 + 180+40+80 + 60) / 2 ), text="4")
canvas.create_text(((190 + 105) / 2, (300 + 180+40+80 + 60) / 2 ), text="5")
canvas.create_text(((190 + 275) / 2, (300 + 180+40+80 + 60) / 2 ), text="6")
canvas.create_text(((190 + 20 + 85 + 275 + 85 + 20) / 2, (300 + 180+40+80 + 60) / 2 ), text="-")



bouton7 = canvas.create_rectangle(20, 240 + 60 + 60, 105, 180+40+80 + 60 + 60, fill = "white", outline = "grey")
bouton8 = canvas.create_rectangle(105, 240 + 60 + 60, 190, 180+40+80 + 60 + 60, fill = "white", outline = "grey")
bouton9 = canvas.create_rectangle(190, 240 + 60 + 60, 275, 180+40+80 + 60 + 60, fill = "white", outline = "grey")
boutondivise = canvas.create_rectangle(190 + 20 + 85, 240 + 60 + 60, 275 + 85 + 20, 180+40+80 + 60 + 60, fill = "white", outline = "grey")


canvas.create_text(((20 + 105) / 2, (240 + 60 + 60 + 180+40+80 + 60 + 60) / 2 ), text="7")
canvas.create_text(((105 + 190) / 2, (240 + 60 + 60 + 180+40+80 + 60 + 60) / 2 ), text="8")
canvas.create_text(((275 + 190) / 2, (240 + 60 + 60 + 180+40+80 + 60 + 60) / 2 ), text="9")
canvas.create_text(((190 + 20 + 85 + 275 + 85 + 20) / 2, (240 + 60 + 60 + 180+40+80 + 60 + 60) / 2 ), text="/")


bouton0 = canvas.create_rectangle(20, 240 + 60 + 60 + 60 + 20, 105, 180+40+80 + 60 + 60 + 60 + 20, fill = "white", outline = "grey")
boutonmultiplier = canvas.create_rectangle(105, 240 + 60 + 60 + 60 + 20, 190, 180+40+80 + 60 + 60 + 60 + 20, fill = "white", outline = "grey")
boutoneffacer = canvas.create_rectangle(190, 240 + 60 + 60 + 60 + 20, 275, 180+40+80 + 60 + 60 + 60 + 20, fill = "white", outline = "grey")
boutonegal = canvas.create_rectangle(190 + 20 + 85, 240 + 60 + 60 + 60 + 20, 275 + 85 + 20, 180+40+80 + 60 + 60 + 60 + 20, fill = "white", outline = "grey")

canvas.create_text(((20 + 105) / 2, (240 + 60 + 60 + 60 + 20 + 180 + 40 + 80 + 60 + 60 + 60 + 20) / 2 ), text="0")
canvas.create_text(((190 + 105) / 2, (240 + 60 + 60 + 60 + 20 + 180 + 40 + 80 + 60 + 60 + 60 + 20) / 2 ), text="X")
canvas.create_text(((190 + 275) / 2, (240 + 60 + 60 + 60 + 20 + 180 + 40 + 80 + 60 + 60 + 60 + 20) / 2 ), text="C")
canvas.create_text(((190 + 20 + 85 + 275 + 85 + 20) / 2, (240 + 60 + 60 + 60 + 20 + 180 + 40 + 80 + 60 + 60 + 60 + 20) / 2 ), text="=")

numerouncarre = 2
numerountexte = 6
numerodeuxcarre = 3
numerodeuxtexte = 7
numerotroiscarre = 4
numerotroistexte = 8
numeropluscarre = 5
numeroplustexte = 9
numeroquatrecarre = 10
numeroquatretexte = 14
numerocinqcarre = 11
numerocinqtexte = 15
numerosixcarre = 12
numerosixtexte = 16
numeromoinscarre = 13
numeromoinstexte = 17
numeroseptcarre = 18
numeroseptexte = 22
numerohuitcarre = 19
numerohuittexte = 23
numeroneufcarre = 20
numeroneuftexte = 24
numerozerocarre = 26
numerozerotexte = 30
numerodivisecarre = 21
numerodivisetexte = 25
numerofoiscarre = 27
numerofoistexte = 31
numeroeffacercarre = 28
numeroeffacertexte = 32
numeroegalcarre = 29
numeroegaltexte = 33

def click(event):
    item = canvas.find_closest(event.x, event.y)
    print(item)
    if item[0] == numerouncarre or item[0] == numerountexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "1")
    if item[0] == numerodeuxcarre or item[0] == numerodeuxtexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "2")
    if item[0] == numerotroiscarre or item[0] == numerotroistexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "3")
    if item[0] == numeroquatrecarre or item[0] == numeroquatretexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "4")
    if item[0] == numerocinqcarre or item[0] == numerocinqtexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "5")
    if item[0] == numerosixcarre or item[0] == numerosixtexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "6")
    if item[0] == numeroseptcarre or item[0] == numeroseptexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "7")
    if item[0] == numerohuitcarre or item[0] == numerohuittexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "8")
    if item[0] == numeroneufcarre or item[0] == numeroneuftexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "9")
    if item[0] == numerozerocarre or item[0] == numerozerotexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "0")
    if item[0] == numeropluscarre or item[0] == numeroplustexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "+")
    if item[0] == numeromoinscarre or item[0] == numeromoinstexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "-")
    if item[0] == numerodivisecarre or item[0] == numerodivisetexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "/")
    if item[0] == numerofoiscarre or item[0] == numerofoistexte:
        canvas.itemconfigure(34, text = canvas.itemcget(34, "text" ) + "*")
    if item[0] == numeroeffacercarre or item[0] == numeroeffacertexte:
        canvas.itemconfigure(34, text = "")
        canvas.itemconfigure(35, text = "")
    if item[0] == numeroegalcarre or item[0] == numeroegaltexte:
        canvas.itemconfigure(35, text=eval(canvas.itemcget(34, "text" )))

canvas.create_text((40, 50), text="",font=("Courier", 14),anchor='w')
canvas.create_text((360, 150), text="",font=("Courier", 14,'bold'),anchor='e')

canvas.bind('<Button-1>', click)
canvas.grid(row = 0, column = 0, rowspan=1)
root.mainloop()