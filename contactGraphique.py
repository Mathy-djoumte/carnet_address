
#
import tkinter

import tkinter as tk
from afficher import select

def afficher_data():
    data = select()
    for x in data:
        label = tk.Label(main, text=x)
        label.place(x=200, y=200)

    return x

main = tkinter.Tk()

m=afficher_data()

for x in m:
    print(m)

main.mainloop()










