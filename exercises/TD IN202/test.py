def afficherTableau2d(l):
    for ligne in l:
        for element in ligne:
            print('{: <3}'.format(element),end='')
        print()


def pivoter(liste):
    
    nbLignes = len(liste)
    nbColonnes = len(liste[0])
    resultat = [[0*nbLignes] for i in range(nbColonnes)]
    afficherTableau2d(resultat)
    for i in range(nbColonnes-1,0,-1):
        for j in range(0,nbLignes):
            resultat[i][j] = l[j][i]
    return resultat



l = [[i]*3 for i in range(5)]

afficherTableau2d(l)

print(pivoter(l))

""" M = [[200,200,200],[200,200,200]]

def rouge(M):
    for pixel in M:
        pixel[0] = int(pixel[0]*1.1)
    return M
M_rouge = rouge(M)
print(M_rouge) """