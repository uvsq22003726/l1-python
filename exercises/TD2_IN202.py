#définir la matrice sans utiliser de boucles
mat= [
[3,0,9,0],
[0,6,0,0],
[0,2,0,46]]

def afficheCarre(carre):
    for i in carre:
        for j in i:
            print('{:5}'.format(j),end='')
        print("\n")

def nbrCol(matrice):
    return len(matrice[0])#a compléter

def nbrLig(matrice):
    return(len(matrice))#a compléter

afficheCarre(mat)
matRenversee = [[0]*3 for i in range(4)]
for i in range(0,4):
    for j in range(0,3):
        matRenversee[i][j] = mat[nbrCol]
print()
afficheCarre(matRenversee)
