# import tkinter as tk
# import tkinter
# from tkinter import messagebox
# from research_num import research_data  #
#
# def num_exist():
#     num = entry_num.get()
#
#     # if not num.isdigit():
#     #     messagebox.showerror("Erreur", "Veuillez entrer un numéro valide.")
#     #     return
#
#
#     result = research_data(num)
#
#     if result:
#         entry_name.delete(0, tk.END)
#         entry_name.insert(0, result[0])
#
#         entry_firstname.delete(0, tk.END)
#         entry_firstname.insert(0, result[1])
#
#         entry_phone.delete(0, tk.END)
#         entry_phone.insert(0, result[2])
#     else:
#         messagebox.showerror("Erreur", "Le numéro n'existe pas")
#
#
# main = tkinter.Tk()
# main.title("Recherche de contact")
#
# tk.Label(main, text="Numéro:").pack()
# entry_num = tk.Entry(main, font=("poppins", 12))
# entry_num.pack()
#
# tk.Label(main, text="Nom:").pack()
# entry_name = tk.Entry(main, font=("poppins", 12))
# entry_name.pack()
#
# tk.Label(main, text="Prénom:").pack()
# entry_firstname = tk.Entry(main, font=("poppins", 12))
# entry_firstname.pack()
#
# tk.Label(main, text="Téléphone:").pack()
# entry_phone = tk.Entry(main, font=("poppins", 12))
# entry_phone.pack()
#
# btn_search = tk.Button(main, text="Rechercher", command=num_exist)
# btn_search.pack()
#
#
# main.mainloop()

import tkinter
from research_num import research_data

main= tkinter.Tk()

label_entry= tkinter.Entry(main)
label_entry.get()
label_entry.pack()

def num_exit():

    num= label_entry.get()
    research_data(num)

button= tkinter.Button(main, text="rechercher", command=num_exit)
button.pack()

main.mainloop()


