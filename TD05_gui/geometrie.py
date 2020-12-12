from tkinter import *
import random
import math

def hexagone(canvas,x,y,rayon,couleur="white",remplissage="white"):
    h = math.sqrt(3)/2*rayon
    """ canvas.create_line(x,y-rayon,x+h,y-rayon/2,fill=couleur,width=epaisseur)
    canvas.create_line(x+h,y-rayon/2,x+h,y+rayon/2,fill=couleur,width=epaisseur)
    canvas.create_line(x+h,y+rayon/2,x,y+rayon,fill=couleur,width=epaisseur)
    canvas.create_line(x,y+rayon,x-h,y+rayon/2,fill=couleur,width=epaisseur)
    canvas.create_line(x-h,y+rayon/2,x-h,y-rayon/2,fill=couleur,width=epaisseur)
    canvas.create_line(x-h,y-rayon/2,x,y-rayon,fill=couleur,width=epaisseur) """
    pts = [(x,y-rayon,x+h,y-rayon/2),(x+h,y-rayon/2,x+h,y+rayon/2),(x+h,y+rayon/2,x,y+rayon),(x,y+rayon,x-h,y+rayon/2),(x-h,y+rayon/2,x-h,y-rayon/2),(x-h,y-rayon/2,x,y-rayon)]
    canvas.create_polygon(pts,outline=couleur,fill=remplissage)

def figure(canvas,x,y,rayon,couleur="red",epaisseur=5):
    h = math.sqrt(3)/2*rayon
    hexagone(c,x,y,rayon)
    c.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,outline=couleur)
    c.create_oval(x-h,y-h,x+h,y+h,outline=couleur)

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def paveHexa(canvas,x,y,rayon,nbHexaX,nbHexaY,couleur="green",remplissage="white"):
    h = math.sqrt(3)/2*rayon
    listeCouleurs = ["blue","grey","black"]
    for i in range(0,nbHexaX):
        for j in range(0,nbHexaY):
            """ echelleGris = random.randint(0,255)
            couleurAleat = get_color(echelleGris,echelleGris,echelleGris)
            remplissage = couleurAleat
            couleur = couleurAleat """
            if j%2 == 0:
                couleur = listeCouleurs[i%3]
                remplissage = listeCouleurs[i%3]
            else:
                couleur = listeCouleurs[(i+2)%3]
                remplissage = listeCouleurs[(i+2)%3]
            hexagone(canvas,x+2*h*i+j%2*h,y+3*rayon/2*j,rayon,couleur,remplissage)
            #c.create_text(x+2*h*i+j%2*h,y+3*rayon/2*j,text=("i=",i,"j=",j))


largeur = 800
hauteur = 800
couleurFond = "black"
fen = Tk()
fen.title("Géométrie")
c = Canvas(fen,width=largeur,height=hauteur,bg=couleurFond)
c.grid()

# """ hexagone(c,300,300,100)
# hexagone(c,300+2*87,300,100)
# hexagone(c,300+87,300+100+100/2,100) """
# """ paveHexa(c,0,0,150,5,5,epaisseur=1) """
# hexagone(c,largeur/2,hauteur/2,largeur/4)
paveHexa(c,0,0,50,15,15)

fen.mainloop()
