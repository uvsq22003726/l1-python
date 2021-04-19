import tkinter as tk


def decalage(lettre_message,lettre_cle,sens):
    return chr((ord(lettre_message) + sens * ord(lettre_cle))%256)



def chiffre():
    texte = entree_texte.get()
    cle = entree_cle.get()
    resultat.delete(0,tk.END)
    if len(texte)>0 and len(cle)>0:
        res = dec_texte(texte,cle,1)
        resultat.insert(0,res)
    else:
        resultat.insert(0,"Il manque quelque chose")

def dechiffre():
    texte = entree_texte.get()
    cle = entree_cle.get()
    resultat.delete(0,tk.END)
    if len(texte)>0 and len(cle)>0:
        res = dec_texte(texte,cle,-1)
        resultat.insert(0,res)
    else:
        resultat.insert(0,"Il manque quelque chose")

def dec_texte(msg,cle,sens):
    msgChiffre = ""
    for i in range(len(msg)):
        msgChiffre += decalage(msg[i],cle[i%len(cle)],sens)
    return msgChiffre

""" def dechiffrer(msg,cle):
    msgDechiffre = ""
    for i in range(len(msg)):
        msgDechiffre += decalage(msg[i],cle[i%len(cle)])
    return msgDechiffre """

racine=tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

entree_cle = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_cle.grid(row = 1, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

label_cle = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer la clé ici.")
label_cle.grid(row = 1, column = 1)

bouton_coder=tk.Button(racine, text="Chiffrer texte",fg="black", width=15, command=chiffre)
bouton_coder.grid(row=2, column=0)

bouton_decoder=tk.Button(racine,text="Déchiffrer texte",fg="black",  width=15, command=dechiffre)
bouton_decoder.grid(row=2, column=1)

resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)


racine.mainloop()

