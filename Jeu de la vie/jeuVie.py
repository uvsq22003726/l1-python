from tkinter import *

fen = Tk()
b = [[Button()for j in range(0,10)] for i in range(0,10)]

for i in range(0,10):
    for j in range(0,10):
        b[i][j].grid(row=i,column=j)

fen.mainloop()