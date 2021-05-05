import time

def tache():
    for i in range(0,10000000):
        a = 0

tempsDebut = time.time()
tache()
duree = time.time() - tempsDebut
print(round(duree*1000))
print("fait")