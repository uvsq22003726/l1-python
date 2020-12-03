def afficheCarre(carre):
    for i in carre:
        for j in i:
            print('{:5}'.format(j),end='')
        print("\n")


def testLignesEgales(carre):
    somme1 = sum(carre[0])
    for i in carre:
        if sum(i) != somme1:
            return -1
    return somme1


def testColonnesEgales(carre):
    somme = 0
    sommePremiereColonne = 0
    for i in range(0,len(carre)):
        sommePremiereColonne += carre[i][0]
    for j in range(0,len(carre)):
        for i in range(0,len(carre)):
            somme += carre[i][j]
        if somme != sommePremiereColonne:
            return -1
        somme = 0   
    return sommePremiereColonne


def testDiagonalesEgales(carre):
    sommeDiag1 = 0
    sommeDiag2 = 0
    for i in range(len(carre)):
        for j in range(len(carre)):
            if i==j:
                sommeDiag1 += carre[i][j]
            if i+j == 3:
                sommeDiag2 += carre[i][j]
    if sommeDiag1 == sommeDiag2:
        return sommeDiag1
    else:
        return -1


def estCarreMagique(carre):
    return testLignesEgales(carre) == testColonnesEgales(carre) == testDiagonalesEgales(carre)


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n = len(carre)
    listeEntiers = [i for i in range(1,n*n+1)]
    for ligne in carre:
        for case in ligne:
            if case in listeEntiers:
                listeEntiers.remove(case)
    if len(listeEntiers) == 0:
        return True
    else:
        return False


carreMag = [[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carrePasMag = [[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]

afficheCarre(carreMag)
print(estCarreMagique(carreMag))
print(estCarreMagique(carrePasMag))
print(estNormal(carreMag))
print(estNormal(carrePasMag))
