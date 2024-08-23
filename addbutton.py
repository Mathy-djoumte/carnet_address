

import tkinter
from insert2 import ajouter_contact

def ajouterContact():
    name= entry_name.get()
    firstname= entry_firstname.get()
    phone= entry_phone.get()

    ajouter_contact(name, firstname, phone)

    entry_name.delete(0, tkinter.END)
    entry_firstname.delete(0, tkinter.END)
    entry_phone.delete(0, tkinter.END)



main= tkinter.Tk()
main.geometry("800x600")
label_title= tkinter.Label(main, text="Ajouter un contact", font=("poppins", 20, "bold") , fg="green")
label_title.place(x=280, y= 100)

label_name= tkinter.Label(main, text="Nom:", font=("poppins", 13, "bold"))
entry_name= tkinter.Entry(main, font=("poppins", 12))
label_name.place(x=200, y=200)

entry_name.place(x=300, y=200)

label_firstname= tkinter.Label(main, text="prenom:", font=("poppins", 13, "bold"))
entry_firstname= tkinter.Entry(main , font=("poppins", 12))
label_firstname.place(x=200,y=250)
entry_firstname.place(x=300, y=250)

label_phone= tkinter.Label(main, text="tel:",font=("poppins", 13, "bold"))
entry_phone= tkinter.Entry(main, font=("poppins", 12))
label_phone.place(x=200, y= 300)
entry_phone.place(x=300, y=300)

button_add= tkinter.Button(main, text="Ajouter", font=("poppins", 12, "bold"),
                           background="white", width=10, activebackground="green",
                           command=ajouterContact

                           )
button_add.place(x=320, y= 350)

main.mainloop()






