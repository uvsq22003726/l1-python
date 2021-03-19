def match_size(mot,i,j): #renvoie la valeur du plus grand sous-mot commun,
                       #dans le mot aux positions position i et j avec j < i
    k = 0
    while(mot[i+k]==mot[j+k] and i+k < len(mot)):
        k+=1
    return k
print(match_size("ab00abc",4,0))