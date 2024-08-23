import tkinter
from tkinter import *
import mysql.connector

config = mysql.connector.connect(
    host="localhost",
    password= "",
    username="root",
    database="contacts"

)

# config = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="contacts"
# )
# cusor = config.cursor()
#
# select= "SELECT * FROM user"
# cusor.execute(select)
# data= cusor.fetchall()
# for x in data:
#     print(x)
# config.close()

def select():
    cusor= config.cursor()
    select= "SELECT * FROM user"
    cusor.execute(select)
    data=cusor.fetchall()

    return data


m= select()
# print(m)
for x in m :
    print(x)