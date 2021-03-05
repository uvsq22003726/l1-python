import tkinter as tk
""" import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog """

lCanvas = 300
hCanvas = 300
compt = 0



def fermer_fenetre():
    fen.destroy()

def clic(event):
    global compt
    compt += 1
    l.config(text=compt)
    print("clic")

def affiche(event):
    source = event.widget
    l.config(text=source.cget("bg"))
    print("double clic")

fen = tk.Tk()
fen.title("Rappel du premier semestre")
l = tk.Label(fen,text=compt)
b = tk.Button(fen,text="Fermer",command=fermer_fenetre)
canvas = tk.Canvas(width=lCanvas,height=hCanvas,bg="red")
canvas.bind('<Button-1>', clic)
canvas.bind('<Double-1>', affiche)
canvas2 = tk.Canvas(width=lCanvas,height=hCanvas,bg="black")
canvas2.bind('<Double-1>', affiche)
l.grid(row=0,column=0)
b.grid(row=1,column=0)
canvas.grid(row=0,column=1)
canvas2.grid(row=1,column=1)

fen.mainloop()