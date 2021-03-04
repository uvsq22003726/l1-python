from tkinter import *
import random


def afficheCarre(carre):
    for i in carre:
        for j in i:
            print('{:^10}'.format(j),end='')
        print("\n")

def modif():
    c.itemconfigure(1,fill="black")

def AllumerClic(event):
    x, y = event.x, event.y
    source = c.find_closest(x,y)[0]
    bruler(source)
    print(source)

def bruler(tag):
    if cases[tag-1][1] != "red":
        c.itemconfig(tag,fill="red")
        cases[tag-1][1] = "red"
    casesModif.append(tag)
    

def simuler():
    for i in casesModif:
        if cases[i-1][1] == "red":
            casesVoisines = [i-1,i+1,i-nbParcellesLargeur,i+nbParcellesLargeur]
            for x in casesVoisines:
                print(cases[x-1][1])
                if cases[x-1][1] == "yellow":
                    nouvellesCasesFeu.append(x)
                if cases[x-1][1] == "green":
                    if random.random() < 0.1:
                        nouvellesCasesFeu.append(x)
    for i in nouvellesCasesFeu:
        bruler(i)
    nouvellesCasesFeu.clear()


largeurCanvas = 500
hauteurCanvas = 500
nbParcellesLargeur = 10
nbParcellesHauteur = 10
largeurParcelle = largeurCanvas/nbParcellesLargeur
hauteurParcelle = hauteurCanvas/nbParcellesHauteur
couleurs = ["green","yellow","blue"]
poidsForet = 4
poidsPrairie = 4
poidsEau = 2
casesModif = []
nouvellesCasesFeu = []
dureeFeu = 4
dureeCendre = 4

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
    c.create_rectangle(j*hauteurParcelle,i*largeurParcelle,j*hauteurParcelle+hauteurParcelle,i*largeurParcelle+largeurParcelle,fill=couleur,width=0)
    c.create_text(j*hauteurParcelle+hauteurParcelle/2,i*largeurParcelle+largeurParcelle/2,text=(n+1,i,j))
    cases.append([n+1,couleur,duree,i,j])
i,j = 0,0
print("i,j",j*hauteurParcelle,i*largeurParcelle,j*hauteurParcelle+hauteurParcelle,i*largeurParcelle+largeurParcelle)
print(cases)
afficheCarre(cases)
print(c.find_all())
bouton.grid(row=0)
c.grid(row=1)

#afficheCarre(cases)

fen.mainloop()