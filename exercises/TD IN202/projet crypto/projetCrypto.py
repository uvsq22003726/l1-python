import tkinter as tk
texte1 = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
texte2 = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
#le prochain fichier est code par un mot de passe de taille inconnue et contient l'indice. les lettres du mot de passe permettent de decaler les lettres du message original modulo 26. seules les lettres de a a z sont chiffrees.
texte3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
texte4 = ""
textes = [texte1,texte2,texte3,texte4]
listeTextes = ["Texte 1","Texte 2","Texte 3","Texte 4"]
typesCryptage = ["Code César","Substitution","Décalage avec mot de passe","Inconnu"]
fonte = ("Helvetica",18)
fonte2 = ("Helvetica",14)
global strTexteDecrypte
global indexTexte
texteDefaut = 2
indexTexte = texteDefaut
texteCrypte = textes[texteDefaut]
strTexteDecrypte = texteCrypte
print(texteCrypte)


def frequence(texte):
    resultat = []
    resultatTrie = []
    listeFreq = []
    nbLettres = 0
    for c in texte:
        if 97 <= ord(c) < 123:
            nbLettres += 1
    for i in range(97, 123):
        if chr(i) in texte:
            resultat.append((chr(i), round(texte.count(chr(i))/nbLettres*100,2)))

    for i in resultat:
        listeFreq.append(i[1])
    while(len(listeFreq)):
        indexMax = listeFreq.index(max(listeFreq))
        resultatTrie.append(resultat[indexMax])
        resultat.remove(resultat[indexMax])
        listeFreq.remove(listeFreq[indexMax])
    return resultatTrie

def frequence2(texte):
    resultat = []
    listeLettres = []
    for i in range(len(texte)):
        c = texte[i]
        if c not in listeLettres:
            resultat.append((c,texte.count(c)/len(texte)))
            listeLettres.append(c)
    return resultat


def substituer(texteInitial,texteAModifier,a,b):
    resultat = ""
    for i in range(len(texteInitial)):
        if texteInitial[i] == a:
            resultat += b
        else:
            resultat += texteAModifier[i]
    return resultat


def decrypterCesar(texte, cle):
    print(cle)
    resultat = []
    n = 0
    i = 0
    while len(resultat) != len(texte):
        rang = ord(texte[i]) - 97
        rangCle = ord(cle[n%len(cle)]) -97
        if 0 <= rang <= 25:
            resultat.append(chr((rang+rangCle)%26+97))
            n += 1
        else:
            resultat.append(texte[i])
        i += 1
    return "".join(resultat)

def genererCle(mot1,mot2):
    cle = []
    for i in range(len(min(mot1,mot2))):
        rang1 = ord(mot1[i])-97
        rang2 = ord(mot2[i])-97
        print(rang1,rang2)
        if 0 <= rang1 < 26 and 0 <= rang2 < 26:
            cle.append(chr((rang2-rang1)%26+97))
        #print((rang2-rang1)%26)
    #print("clé: ",cle)
    return "".join(cle)


def afficherResultat():
    global strTexteDecrypte
    
    mot1 = champ1.get()
    mot2= champ2.get()
    if typesCryptage[indexTexte] == typesCryptage[0] or typesCryptage[indexTexte] == typesCryptage[2]:
        
        cle = genererCle(mot1, mot2)
        """ for i in range(26):
            strTexteDecrypte = strTexteDecrypte + "\n\n" + decrypterCesar(texteCrypte, chr(i+97) +"h")  """
        texteDecrypte.config(text=decrypterCesar(texteCrypte, cle))
    elif typesCryptage[indexTexte] == typesCryptage[1]:
        if len(mot1) == len(mot2):
            champ1.delete(0)
            champ2.delete(0)
            for i in range(len(mot1)):
                strTexteDecrypte = substituer(texteCrypte,strTexteDecrypte, mot1[i], mot2[i])
            texteDecrypte.config(text=strTexteDecrypte)


def changerTexte(e):
    global indexTexte, texteCrypte
    if len(choixTexte.curselection()):
        
        indexTexte = listeTextes.index(choixTexte.get(choixTexte.curselection()))
        texteCrypte = textes[indexTexte]
        labelTypeCryptage.config(text=typesCryptage[indexTexte])
        msgTexteCrypte.config(text=texteCrypte)
        labelFreq.config(text=affichageFreq(texteCrypte))


def affichageFreq(texte):
    listeFreq = frequence(texte)
    tabFreq = []
    for c in listeFreq:
        tabFreq.append(c[0]+"  "+str(c[1])+"\n")
    tabFreq = "Lettres les plus fréquentes\n"+"".join(tabFreq)
    return tabFreq
    


def decouper(texte,nbSegments):
    segments = []
    t = []
    tailleSegment = int(len(texte)/nbSegments)
    for i in range(0,nbSegments):
        segments.append(texte[i*tailleSegment:i*tailleSegment+tailleSegment])
    if len(texte) % nbSegments :
        segments[-1] = segments[-1] + texte[-1]
    return segments



fen = tk.Tk()
fen.title("Projet cryptographie")
panneauGauche = tk.Frame(fen)
panneauCentral = tk.Frame(fen)

msgTexteCrypte = tk.Message(panneauCentral,text=texteCrypte,relief="groove",font=fonte,width=1200)
texteDecrypte = tk.Message(panneauCentral,relief="groove",font=fonte,width=1400)
choixTexte = tk.Listbox(panneauGauche,font=fonte2)
for t in listeTextes:
    choixTexte.insert(tk.END,t)
choixTexte.config(height=len(listeTextes))
choixTexte.select_set(texteDefaut)
choixTexte.bind("<<ListboxSelect>>",changerTexte)
labelTypeCryptage = tk.Label(panneauGauche,text=typesCryptage[indexTexte],font=fonte)
labelFreq = tk.Label(panneauGauche,relief="groove",font=fonte2)
labelFreq.config(text=affichageFreq(texteCrypte))
boutonCorresp = tk.Button(panneauCentral,text="correspond à",command=afficherResultat,font=fonte2)
champ1 = tk.Entry(panneauCentral,font=fonte2)
champ2 = tk.Entry(panneauCentral,font=fonte2)


choixTexte.grid(row=0)
labelTypeCryptage.grid(row=1)
labelFreq.grid(row=2)

msgTexteCrypte.grid(row=0,columnspan=3)
texteDecrypte.grid(row=2,columnspan=3)
champ1.grid(row=1,column=0)
champ2.grid(row=1,column=2)
boutonCorresp.grid(row=1,column=1)

panneauGauche.grid(row=0,column=0)
panneauCentral.grid(row=0,column=1)
#print(decrypterCesar(texteCrypte, 1))
print("\n")
""" cle = input()
print(decrypterCesar(texteCrypte, cle)) """

segments = decouper(texteCrypte, 5)
""" for seg in segments:
    print(affichageFreq(seg))
print("test",affichageFreq("bateau")) """

print(len(texteCrypte))
for i in range(1,22):
    print(i,"segments de",len(texteCrypte)/i,"lettres")
    somme = 0
    for seg in decouper(texteCrypte,i):
        print(frequence(seg)[0])
        somme += frequence(seg)[0][1]
    print("Somme /nbr de seg",somme/i)

for i in range(1,50):
    if not 168%i:
        print(i)
#fen.mainloop()