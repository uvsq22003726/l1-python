# def nbPremiers(n):
#     for i in range(2,n+1):
#         premier = True
#         for j in range(2,i):
#             if i%j == 0:
#                     premier = False
#         if premier :
#             print(i)
#     return

# nbPremiers(20)

# n = int(input("Entrez un nombre entier"))
# if n >= 12 and n<1000 :
#     print("Gagné")

# n = 6
# for i in range(0,10):
#     print(n,"*",i,"=",n*i)

# n = 20
# while n != 1:
#     print(int(n))
#     if n%2 == 0:
#         n /= 2
#     else:
#         n = n * 3 +1

# class Test:
#     a = 0

#     def __init__(self,a):
#         self.a = a
#         return

# def comp(s1,s2):
#     l1 = s1.split()
#     l2 = s2.split()
#     motsCommuns = []
#     for i in l1:
#         if i in l2 and i not in motsCommuns:
#             motsCommuns.append(i) 
#     return motsCommuns

# print(comp("a b a c","c d a"))

# def Carre(x):
#     """Affiche le carré de son argument + 1 si l'argument est inférieur à 1"""
#     if x < 1:
#         print(x*x+1)
    
# help(Carre)

# var_glob = 5

# def produit(var_loc ):
#     return var_loc * var_glob

# print(produit(3))

# def f(nom = "Dupont", prenom, ville = "Paris"):
#     print(nom ,prenom, "Habite à", ville)

# f(prenom = "Clément", nom = "Maouche")

""" 1. définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
– triez et affichez la liste ;
– ajoutez l’élément 12 à la liste et affichez la liste ;
– renversez et affichez la liste ;
– affichez l’indice de l’élément 17 ;
– enlevez l’élément 38 et affichez la liste ;
– affichez la sous-liste du 2eau 3eélément ;
– affichez la sous-liste du début au 2eélément ;
– affichez la sous-liste du 3eélément à la fin de la liste ;
– affichez la sous-liste complète de la liste ;
BC v2.1 - 3 - 2008 - 2009
Énoncés
– affichez le dernier élément en utilisant un indiçage négatif.
Bien remarquer que certaines méthodes de liste ne retournent rien.
2. Initialisez truc comme une liste vide, et machin comme une liste de cinq flottants nuls.
Affichez ces listes.
Utilisez la fonction range() pour afficher :
– les entiers de 0 à 3 ;
– les entiers de 4 à 7 ;
– les entiers de 2 à 8 par pas de 2.
Définir chose comme une liste des entiers de 0 à 5 et testez l’appartenance des éléments 3 et 6 à chose.
3. Utilisez une liste en compréhension pour ajouter 3 à chaque élément d’une liste d’entiers de 0 à 5.
4. Utilisez une liste en compréhension pour ajouter 3 à chaque élément d’une liste d’entiers de 0 à 5, mais seulement si l’élément est supérieur ou égal à 2.
◃ 5. Utilisez une liste en compréhension pour obtenir la liste ['ad', 'ae', 'bd', 'be',
'cd', 'ce'] à partir des chaînes "abc" et "de".
Indication : utilisez deux boucles for imbriquées.
6. Utilisez une liste en compréhension pour calculer la somme d’une liste d’entiers de 0
à 9. """

""" liste = [17, 38, 10, 25, 72]
liste.sort()
print(liste)
liste.append(12)
print(liste)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)
print(liste[1:3])
print(liste[:2])
print(liste[2:])
print(liste[:])
print(liste[-1])

truc = []
machin = [0.0]*5
chose = []
print(chose) """

l = [1,2,3,2]
print(l)
print(l.index(2))
