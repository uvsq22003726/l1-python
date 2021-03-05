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
    #print(casesModif)
    #Changement de couleur des cases avec duree = 0
    for i in casesModif:
        cases[i][2] -= 1
        if cases[i][2] == 0:
            if cases[i][1] == "red":
                cases[i][1] = "grey"
                cases[i][2] = dureeCendre
                c.itemconfig(cases[i][0],fill="grey")
                #print(i,"devient gris")
            else:
                cases[i][1] = "black"
                c.itemconfig(cases[i][0],fill="black")
                casesNoires.append(i)
        
        #Propagation du feu
        if cases[i][1] == "red":
            casesVoisines = [i-1,i+1,i-nbParcellesLargeur,i+nbParcellesLargeur]
            for x in casesVoisines:
                if x >= 0 and x < nbParcellesLargeur*nbParcellesHauteur and x not in nouvellesCasesFeu:
                    if cases[x][1] == "yellow":
                        nouvellesCasesFeu.append(x)
                    if cases[x][1] == "green":
                        if random.random() < 0.1:
                            nouvellesCasesFeu.append(x)
    #Les cases noires deviennent inertes
    for i in casesNoires:
        casesModif.remove(i)
        casesNoires.clear()

    for i in nouvellesCasesFeu:
        bruler(i)
    nouvellesCasesFeu.clear()
    #afficheCarre(cases)


largeurCanvas = 500
hauteurCanvas = 500
nbParcellesLargeur = 50
nbParcellesHauteur = 50
largeurParcelle = largeurCanvas/nbParcellesLargeur
hauteurParcelle = hauteurCanvas/nbParcellesHauteur
couleurs = ["green","yellow","blue"]
couleursPerso = [get_color(130,200,80),get_color(230,230,100),get_color(0,200,240)]
poidsForet = 1
poidsPrairie = 10000
poidsEau = 1
casesModif = []
nouvellesCasesFeu = []
casesNoires = []
dureeFeu = 1
dureeCendre = 1
id = 0

fen = Tk()
cases = []
fen.title("test")
c = Canvas(fen,width=largeurCanvas,height=hauteurCanvas,bg="white")
c.bind('<Button-1>',AllumerClic)
bouton = Button(text="Simuler",command=simuler)
for n in range(0,nbParcellesLargeur*nbParcellesHauteur):
    i = n // nbParcellesLargeur
    j = n % nbParcellesHauteur
    couleur = random.choices(couleurs,[poidsForet,poidsPrairie,poidsEau])[0]
    duree = 0
    id = c.create_rectangle(j*largeurParcelle,i*hauteurParcelle,j*largeurParcelle+largeurParcelle,i*hauteurParcelle+hauteurParcelle,fill=couleur,width=0)
    cases.append([id,couleur,duree,i,j])
    #c.create_text(j*hauteurParcelle+hauteurParcelle/2,i*largeurParcelle+largeurParcelle/2,text=(id))
    
i,j = 0,0
#print("i,j",j*hauteurParcelle,i*largeurParcelle,j*hauteurParcelle+hauteurParcelle,i*largeurParcelle+largeurParcelle)
#print(cases)
#afficheCarre(cases)
#print(c.find_all())
bouton.grid(row=0)
c.grid(row=1)

#afficheCarre(cases)

fen.mainloop()