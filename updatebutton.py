import tkinter
from tkinter import *
from update import num_exist

main= tkinter.Tk()

data= num_exist()
entry_name= tkinter.Entry(main, font=("poppins", 12))
entry_firstname= tkinter.Entry(main, font=("poppins", 12))
entry_phone= tkinter.Entry(main, font=("poppins", 12))
if data:
    entry_name.insert(0, data[0])
    entry_firstname.insert(0, data[1])
    entry_phone.insert(0, data[2])
else:
    print("non")
main.mainloop()


