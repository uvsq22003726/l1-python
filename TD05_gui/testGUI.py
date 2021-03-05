import tkinter as tk

def dessin():
    x = int(champ1.get())
    y = int(champ2.get())
    c.create_oval(x,y,x+100,y+50,fill="red")

fenetre = tk.Tk()
c = tk.Canvas(fenetre,width=500,height=500,bg="yellow")
l1 = tk.Label(fenetre,text="x",bg="cyan")
l2 = tk.Label(fenetre,text="y",bg="cyan")
champ1 = tk.Entry(fenetre)
champ1.insert(0,"200")
champ2 = tk.Entry(fenetre,text="200")
champ2.insert(0,"200")
b = tk.Button(fenetre,text="Bouton",command=dessin)
l1.grid(row=0,column=1)
l2.grid(row=0,column=3)
champ1.grid(row=0,column=2)
champ2.grid(row=0,column=4)
c.grid(row=1,column=1,columnspan=4)
b.grid(row=1,column=0)
fenetre.mainloop()