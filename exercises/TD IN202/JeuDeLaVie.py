import tkinter as tk

def ChangerCase(event):
    x, y = event.x, event.y
    i,j = y // COTE, x // COTE
    if not etatGrille[i][j]:
        devientVivant(i,j)
    else:
        meurt(i,j)
    #print(nbVoisinsVivants(i,j))


def devientVivant(x,y):
    source = listeId[x][y]
    voisins = casesVoisines(x,y)
    etatGrille[x][y] = True
    c.itemconfig(source,fill=COULEURVIVANT)
    if (x,y) not in casesATester:
        casesATester.append((x,y))
    for case in voisins:
        if case not in casesATester:
            ajouterATester(case[0],case[1])
    #print("taille",len(casesATester))
        

def ajouterATester(x,y):
    casesATester.append((x,y))
    c.itemconfig(listeId[x][y],fill="yellow")

def supprimerATester(x,y):
    casesATester.remove((x,y))
    c.itemconfig(listeId[x][y],fill="red")


def meurt(x,y):
    source = listeId[x][y]
    etatGrille[x][y] = False
    if (x,y) not in casesATester:
        c.itemconfig(source,fill=COULEURMORT)


def casesVoisines(i,j):
    casesVoisines = []
    if i-1 >= 0:
        casesVoisines.append((i-1,j))
    if i+1 < len(etatGrille):
        casesVoisines.append((i+1,j))
    if j-1 >= 0:
        casesVoisines.append((i,j-1))
    if j+1 < len(etatGrille[0]):
        casesVoisines.append((i,j+1))
    if i-1 >= 0 and j-1 >= 0:
        casesVoisines.append((i-1,j-1))
    if i+1 < len(etatGrille) and j+1 < len(etatGrille[0]):
        casesVoisines.append((i+1,j+1))
    if i-1 >= 0 and j+1 < len(etatGrille[0]):
        casesVoisines.append((i-1,j+1))
    if i+1 < len(etatGrille) and j-1 >= 0:
        casesVoisines.append((i+1,j-1))
    return casesVoisines


def nbVoisinsVivants(i,j):
    nbVoisinsVivants = 0
    if i-1 >= 0 and etatGrille[i-1][j]:
        nbVoisinsVivants += 1
    if i+1 < len(etatGrille) and etatGrille[i+1][j]:
        nbVoisinsVivants += 1
    if j-1 >= 0 and etatGrille[i][j-1]:
        nbVoisinsVivants += 1
    if j+1 < len(etatGrille[0]) and etatGrille[i][j+1]:
        nbVoisinsVivants += 1
    if i-1 >= 0 and j-1 >= 0 and etatGrille[i-1][j-1]:
        nbVoisinsVivants += 1
    if i+1 < len(etatGrille) and j+1 < len(etatGrille[0]) and etatGrille[i+1][j+1]:
        nbVoisinsVivants += 1
    if i-1 >= 0 and j+1 < len(etatGrille[0]) and etatGrille[i-1][j+1]:
        nbVoisinsVivants += 1
    if i+1 < len(etatGrille) and j-1 >= 0 and etatGrille[i+1][j-1]:
        nbVoisinsVivants += 1
    return nbVoisinsVivants




def simuler():
    nouvellesCasesVivantes = []
    nouvellesCasesMortes = []
    casesIsolees = []
    for i in range(len(casesATester)):
        case = casesATester[i]
        x, y = case[0], case[1]
        n = nbVoisinsVivants(x,y)
        if not etatGrille[x][y]:
            if n == 3:
                nouvellesCasesVivantes.append((x,y))
            else:
                if not n:
                    casesIsolees.append((x,y))
        else:
            if not (n == 2 or n == 3):
                nouvellesCasesMortes.append((x,y))

    """ for i in range(CASES):
        for j in range(CASES):
            n = nbVoisinsVivants(i,j)
            if not etatGrille[i][j]:
                if n == 3:
                    nouvellesCasesVivantes.append((i,j))
            else:
                if not (n == 2 or n == 3):
                    nouvellesCasesMortes.append((i,j)) """
    for case in nouvellesCasesMortes:
        meurt(case[0],case[1])
    for case in nouvellesCasesVivantes:
        devientVivant(case[0],case[1])
    for case in casesIsolees:
        supprimerATester(case[0], case[1])
    print(len(casesATester))
    print(casesATester,"\n")

def simulerAuto():
    if etatSimulation:
        simuler()
        fen.after(DELAI,simulerAuto)


def activerSimulationAuto():
    global etatSimulation
    etatSimulation = not etatSimulation
    if etatSimulation:
        btAuto.config(bg=couleurSimulerMarche)
    else:
        btAuto.config(bg=couleurSimulerArret)
    simulerAuto()
    
    



CASES = 35
COULEURVIVANT = "black"
COULEURMORT = "white"
couleurGrille = "grey"
DELAI = 30
fonte = ("TkDefaultFont",14)
etatGrille = [[False]*CASES for i in range(CASES)]
listeId = [[0]*CASES for i in range(CASES)]
casesATester = []
global etatSimulation
etatSimulation = False
couleurSimulerArret = "SystemButtonFace"
couleurSimulerMarche = "green"


fen = tk.Tk()
fen.title("Jeu de la vie")

tailleCanvas = min(fen.winfo_screenwidth(),fen.winfo_screenheight())*0.7
COTE = int(tailleCanvas/CASES)
""" print(tailleCanvas/CASES)
print(COTE)
print("decalage",tailleCanvas-CASES*COTE)
print(fen.winfo_screenwidth(),fen.winfo_screenheight())
print(tailleCanvas) """
tailleCanvas = CASES*COTE

barreSup = tk.Frame(fen)

btPasserEtape = tk.Button(barreSup,text="Passer une étape",command=simuler,font=fonte)
btAuto = tk.Button(barreSup,text="Simuler",command=activerSimulationAuto,font=fonte)

c = tk.Canvas(fen,width=tailleCanvas, height=tailleCanvas)


btPasserEtape.grid(row=0,column=0)
btAuto.grid(row=0,column=1)
barreSup.grid(row=0)
c.grid(row=1)

for i in range(CASES):
    for j in range(CASES):
        listeId[i][j] = c.create_rectangle(j*COTE,i*COTE,j*COTE+COTE,i*COTE+COTE,fill=COULEURMORT,outline=couleurGrille)
        #print(listeId)

c.bind('<Button-1>',ChangerCase)


fen.mainloop()

