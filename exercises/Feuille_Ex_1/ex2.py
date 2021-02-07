import tkinter as tk

def clic(event):
    global points
    global cpt
    
    x = event.x
    y = event.y
    if not pause:
        cpt += 1
        points.append([x,y])
        if cpt == 2:
            c.create_line(points,fill="blue")
            points.clear()
        if cpt == 4:
            c.create_line(points,fill="red")
            points.clear()
        if cpt == 5:
            c.delete("all")
            points.clear()
            cpt = 0

def btPause():
    global pause
    pause = not pause
    if b.cget("text") == "Pause":
        b.config(text="Restart")
    else:
        b.config(text="Pause")


fen = tk.Tk()
fen.title("Exercice 2")
c = tk.Canvas(fen,width=500,height=500,bg="white")
b = tk.Button(fen,text="Pause",command=btPause)
points = []
cpt = 0
pause = False
c.grid(row=0,column=0)
b.grid(row=1,column=0)
c.bind("<Button-1>", clic)
fen.mainloop()