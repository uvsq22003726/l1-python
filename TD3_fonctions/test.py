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

print(type(range(1,10)))