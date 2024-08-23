import tkinter

import tkinter as tk


from afficher import select
main= tkinter.Tk()
i=1
data= select()
for users in data:
    for j in range(len(users)):
        user= tkinter.Label(main, width=10, text='numero', borderwidth=2, relief='sunken', anchor='w', bg='yellow')
        user.grid(row=0, column=0)
        user = tkinter.Label(main, width=10, text='nom', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        user.grid(row=0, column=1)
        user = tkinter.Label(main, width=10, text='prenom', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        user.grid(row=0, column=2)
        user = tkinter.Label(main, width=10, text='tel', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
        user.grid(row=0, column=3)
        user=tkinter.Entry(main, width=10, fg='blue')
        user.grid(row=i, column=j)
        user.insert(1, str(users[j]))

    i=i+1
    print()


main.mainloop()
