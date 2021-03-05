import tkinter as tk

create=False

def charger(widg):
    global create
    global photo
    global img
    global canvas
    filename= tk.filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    print(photo)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.pack()
        create=False
        
    else:
        canvas.pack_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.pack()

fen = tk.Tk()
b = tk.Button(fen,text="Afficher l'image",command=lambda:charger(fen))
b.grid()
fen.mainloop()