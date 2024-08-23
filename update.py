# import mysql.connector
# import tkinter
# config = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="contacts"
# )
#
# def num_exist():
#
#     cursor = config.cursor()
#     num = int(input('Entrer le numéro: '))
#     query = "SELECT * FROM user WHERE id = %s"
#     cursor.execute(query, (num,))
#
#     result = cursor.fetchall()
#
#     if result:
#         return result
#     else:
#         print("le  numero n'existe pas")
#
# main = tkinter.Tk()
#
# m= num_exist()
# print(m)
# main.mainloop()

import mysql.connector
import tkinter as tk

# Connexion à la base de données
config = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="contacts"
)


def num_exist():
    cursor = config.cursor()
    num = int(input('Entrer le numéro: '))
    data = "SELECT *  FROM user WHERE id = %s"
    cursor.execute(data, (num,))
    result = cursor.fetchone()

    if result:
        entry_name.delete(0, tk.END)
        entry_firstname.delete(0, tk.END)
        entry_phone.delete(0, tk.END)

        entry_name.insert(0, result[0])
        entry_firstname.insert(0, result[1])
        entry_phone.insert(0, result[2])
    else:
        print("Le numéro n'existe pas")



main = tk.Tk()

entry_name = tk.Entry(main, font=("poppins", 12))
entry_firstname = tk.Entry(main, font=("poppins", 12))
entry_phone = tk.Entry(main, font=("poppins", 12))

entry_name.pack()
entry_firstname.pack()
entry_phone.pack()


num_exist()

main.mainloop()


