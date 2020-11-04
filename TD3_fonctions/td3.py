#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    return temps[0]*60*60*24+temps[1]*60*60+temps[2]*60+temps[3]
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    pass

# temps = (1,1,1,1)
# print(type(temps))
# print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde // (60*60*24)
    seconde = seconde % (60*60*24)
    heures = seconde // (60*60)
    seconde = seconde % (60*60)
    minutes = seconde // 60
    secondes = seconde % 60
    return (jours, heures, minutes, secondes)
    pass

# temps = secondeEnTemps(tempsEnSeconde(temps))
# print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici

def afficheTemps(temps):
    if temps[0] > 0 :
        print(temps[0],"jour"+pluriel(temps[0]),end=" ")
    if temps[1] > 0 :
        print(temps[1],"heure"+pluriel(temps[1]),end=" ")
    if temps[2] > 0 :
        print(temps[2],"minute"+pluriel(temps[2]),end=" ")
    if temps[3] > 0 :
        print(temps[3],"seconde"+pluriel(temps[3]))
    pass

def pluriel(n) :
    if n>1 :
        return("s")
    else :
        return("")

# temps = (10,1,4,23)
# afficheTemps(temps)

def demandeTemps():
    jours = int(input("Nombre de jours:"))
    heures = int(input("Nombre d'heures:"))
    minutes = int(input("Nombre de minutes:"))
    secondes = int(input("Nombre de secondes:"))
    return (jours, heures, minutes, secondes)
    pass

# temps = demandeTemps()
# if temps[0] >= 0 and temps[1] >= 0 and temps[1] <= 24 and temps[2] >= 0 and temps[2] <= 60 and temps[3] >= 0 and temps[3] <= 60 :
#     afficheTemps(temps)
# else :
#     print("Erreur dans le format du temps")


def sommeTemps(temps1,temps2):
    return secondeEnTemps(tempsEnSeconde(temps1)+tempsEnSeconde(temps2))
    pass

# afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))


def proportionTemps(temps,proportion):
    return secondeEnTemps(int(tempsEnSeconde(temps)*proportion))
    pass

# afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments

def tempsEnDate(temps):
    annees = 1970 + temps[0] // 365
    jours = temps[0] % 365
    heures = temps[1]
    minutes = temps[2]
    secondes = temps[3]
    return (annees, jours, heures, minutes, secondes)
    pass

def afficheDate(date):
    
    print(date[0],"",end="")
    if date[1] > 0 :
        print(date[1],"jour"+pluriel(temps[0]),end=" ")
    if date[2] > 0 :
        print(date[2],"heure"+pluriel(temps[1]),end=" ")
    if date[3] > 0 :
        print(date[3],"minute"+pluriel(temps[2]),end=" ")
    if date[4] > 0 :
        print(date[4],"seconde"+pluriel(temps[3]))
    
    pass
    
# temps = secondeEnTemps(263748)
# afficheTemps(temps)
# afficheDate(tempsEnDate(temps))

#tester ici les fonctions de la librairie time
import time
# print(time.gmtime())
# print(time.localtime())

def bisextile(jour):
    annees = jour // 365
    print(annees)
    for i in range(2020,anees) :
        if (a%4 == 0 and a%100!=0) or a%400 == 0 :
            print(annees,": bissextile")
        else :
            print(anees,": non bissextile")
    pass
        
# bisextile(20000)

def nombreBisextile(jour):
    pass

def tempsEnDateBisextile(temps):
    pass
   
# temps = secondeEnTemps(1000000000)
# afficheTemps(temps)
# afficheDate(tempsEnDateBisextile(temps))


def verifie(liste_temps):
    total = 0
    validiteSemaine = True
    nbHeures = [0,0,0,0]
    for i in range(0,4):
        for j in range(0,4):
            nbHeures[i] += liste_temps[i][j]
            total += liste_temps[i][j]
        print(str(nbHeures[i])+"h ",end="")
        if nbHeures[i]>48:
            validiteSemaine = False
    if not validiteSemaine:
        print("Trop d'heures par semaine.",end=" ")
    if total > 148:
        print("Trop d'heures dans le mois."+"("+str(total)+"h)")
        
    pass


liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
verifie(liste_temps)