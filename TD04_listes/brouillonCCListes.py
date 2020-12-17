""" def max_element(liste1, liste2):
    if max(liste1) >= max(liste2):
        return max(liste1)
    else:
        return max(liste2)

print(max_element([9],[1]))
 """
""" def plus_3(liste):
    return [i+3 for i in liste] """

""" listeEntiers = [i for i in range(1,100)]
listeNbPairs = []
for i in range(100,1,-2):
    listeNbPairs.append(i)

print(listeEntiers)
print(listeNbPairs) """


""" def carre_decroissant( n ):
    l = []
    for i in range(0,n):
        l.append([j for j in range(n-i,2*n-i)])
    return l

print(carre_decroissant(8)) """

""" def crypter(s,n):
    for i in s:
        print(chr(ord(i)+n))

crypter("abcdefghijklmnopqrstuvxyz",5) """

liste1 = [[3,4],[3,4]]
u = [3,4]
liste2 = [u,u]
liste1[0][0] = 0
liste2[0][0] = 0
print(liste1[1][0],liste1[1][0])