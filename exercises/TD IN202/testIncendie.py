from tkinter import *
import random


def afficheCarre(carre):
    for i in carre:
        for j in i:
            print('{:^10}'.format(j),end='')
        print("\n")

def modif():
    c.itemconfigure(1,fill="black")

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def AllumerClic(event):
    x, y = event.x, event.y
    source = c.find_closest(x,y)[0]
    #bruler(source)
    print("ID:",source)
    for i in range(0,len(cases)):
        if cases[i][0] == source:
            print("Index:",i)
            bruler(i)
            return
   

def bruler(index):
    if cases[index][1] != "red":
        c.itemconfig(cases[index][0],fill="red")
        cases[index][1] = "red"
        cases[index][2] = dureeFeu
    casesModif.append(index)
    

def simuler():
    print(len(casesModif))
    for i in casesModif:
        if cases[i][1] == "red" and cases[i][2] > 0:
            casesVoisines = [i-1,i+1,i-nbParcellesLargeur,i+nbParcellesLargeur]
            for x in casesVoisines:
                if x >= 0 and x < nbParcellesLargeur*nbParcellesHauteur:
                    if cases[x][1] == "yellow":
                        nouvellesCasesFeu.append(x)
                    if cases[x][1] == "green":
                        if random.random() < 0.1:
                            nouvellesCasesFeu.append(x)
            cases[i][2] -= 1
        elif cases[i][1] == "red" and cases[i][2] == 0:
            cases[i][1] = "grey"
            cases[i][2] = dureeCendre
            c.itemconfig(cases[i][0],fill="grey")
        elif cases[i][1] == "grey" and cases[i][2] > 0:
            cases[i][2] -= 1
        elif cases[i][1] == "grey" and cases[i][2] == 0:
            cases[i][1] = "black"
            c.itemconfig(cases[i][0],fill="black")
            casesModif.remove(i)
        
    for i in nouvellesCasesFeu:
        bruler(i)
    nouvellesCasesFeu.clear()


largeurCanvas = 500
hauteurCanvas = 500
nbParcellesLargeur = 1
nbParcellesHauteur = 1
largeurParcelle = largeurCanvas/nbParcellesLargeur
hauteurParcelle = hauteurCanvas/nbParcellesHauteur
couleurs = ["green","yellow","blue"]
couleursPerso = [get_color(130,200,80),get_color(230,230,100),get_color(0,200,240)]
poidsForet = 60
poidsPrairie = 1000
poidsEau = 10
casesModif = []
nouvellesCasesFeu = []
dureeFeu = 4
dureeCendre = 4
id = 0

fen = Tk()
cases = []
fen.title("test")
c = Canvas(fen,width=largeurCanvas,height=hauteurCanvas,bg="white")
c.bind('<Button-1>',AllumerClic)
bouton = Button(text="Simuler",command=simuler)
for n in range(0,nbParcellesLargeur*nbParcellesHauteur):
    i = n // nbParcellesLargeur
    j = n % nbParcellesLargeur
    couleur = random.choices(couleurs,[poidsForet,poidsPrairie,poidsEau])[0]
    duree = 0
    id = c.create_rectangle(j*hauteurParcelle,i*largeurParcelle,j*hauteurParcelle+hauteurParcelle,i*largeurParcelle+largeurParcelle,fill=couleur,width=0)
    #c.create_text(j*hauteurParcelle+hauteurParcelle/2,i*largeurParcelle+largeurParcelle/2,text=(id,i,j))
    cases.append([id,couleur,duree,i,j])
i,j = 0,0
#print("i,j",j*hauteurParcelle,i*largeurParcelle,j*hauteurParcelle+hauteurParcelle,i*largeurParcelle+largeurParcelle)
#print(cases)
#afficheCarre(cases)
#print(c.find_all())
bouton.grid(row=0)
c.grid(row=1)

#afficheCarre(cases)

fen.mainloop()